import requests
import json
import re
import pprint

APP_ID = 'dos'

# ENV = 'NDEV'
# ENV = 'QA'
ENV = 'PROD'

# APOLLO_UPDATE = False
APOLLO_UPDATE = True

APOLLO_RELEASE = False
# APOLLO_RELEASE = True

CFG_COOKIE = None
#CFG_COOKIE = "dsj=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImNoZW55aSIsImNoaW5lc2VOYW1lIjoiNlptSTZZQzQiLCJkZXB0IjoiRGV2ZWxvcG1lbnQgRW5naW5lZXIiLCJwaG9uZSI6IjEzNTY0NjM0MzMzIiwiZW1haWwiOiJjaGVueWlAaW1kYWRhLmNuIiwiYWRtaW4iOmZhbHNlLCJsb2dpblRpbWUiOiIxNTkyODA2MjcxIiwiZXhwIjoxNTkzNDExMDcxLCJpc3MiOiJjb3JwLmltZGFkYS5jbiJ9.H7bdJG9n2S0qWsYE4TRU7aOWVz4Q97lkJZhQJpwtTw4"
# ----------------------------------------------------------

CFG_HOSTS = {
    'NDEV': 'http://configapi.ndev.imdada.cn',
    'QA': 'http://configapi.qa.imdada.cn',
    'PROD': 'http://config.corp.imdada.cn/api'
}

CFG_HOST = CFG_HOSTS.get(ENV)

PRIVATE_TOKEN = "9fc35230e992509430b420d2e25289e4"

APOLLO_TOKEN = "433a0aa8f990bc441edd98a4c22510ce4f5c6789"

APOLLO_USER = "apollo"

APOLLO_HOST = "http://apollo.corp.imdada.cn"

CLUSTER = 'default'


class CfgService:
    def __init__(self):
        self.host = CFG_HOST
        self.token = PRIVATE_TOKEN

    def get(self, url):
        headers = {"private-token": self.token, "Content-Type": "application/json"}
        if CFG_COOKIE:
            headers.update({"Cookie": CFG_COOKIE})
        return requests.get(
            f"{self.host}{url}",
            headers=headers,
        )

    def post(self, url):
        headers = {"private-token": self.token, "Content-Type": "application/json"}
        if CFG_COOKIE:
            headers.update({"Cookie": CFG_COOKIE})
        return requests.post(
            f"{self.host}{url}",
            headers=headers,
        )

    def get_apps(self):
        return self.get("/config")

    def get_app_versions(self, app_cfg_id):
        return self.get(f"/version?limit=10&sysConfigId={app_cfg_id}")

    def get_version(self, versionId):
        return self.get(f"/version/{versionId}")

    def get_app_default_version(self, app_id):
        for app in (self.get_apps().json()).get("data"):
            app_name = app.get("name")
            if app.get("isSysConfig") and app_name == app_id:
                return app.get("defaultVersion")

        return None

    def get_default_version_configs(self, app_id):
        default_version = self.get_app_default_version(app_id)
        if not default_version:
            return None

        return self.get_version(default_version).json().get("data")


class ApolloApi:
    def __init__(self):
        self.host = APOLLO_HOST
        self.token = APOLLO_TOKEN
        self.headers = {"Authorization": self.token}
        self.APOLLO_USER = APOLLO_USER

    def json(self, url, data):
        return requests.post(
            f"{self.host}/openapi/v1{url}", json=data, headers=self.headers
        )

    def get(self, url):
        return requests.get(
            f"{self.host}/openapi/v1{url}", headers=self.headers
        )

    def json_put(self, url, data):
        return requests.put(
            f"{self.host}/openapi/v1{url}", json=data, headers=self.headers
        )

    def create_namespace(self, appid, namespace, is_public=True):
        return self.json(
            f"/apps/{appid}/appnamespaces",
            {
                "name": namespace,
                "appId": appid,
                "format": "properties",
                "isPublic": is_public,
                "dataChangeCreatedBy": "apollo",
            },
        )

    def add_item(
        self,
        appid,
        key,
        value,
        env="dev",
        cluster_name="default",
        namespace="application",
        user=None
    ):
        if not user:
            user = self.APOLLO_USER
        return self.json(
            f"/envs/{env}/apps/{appid}/clusters/{cluster_name}/namespaces/{namespace}/items",
            {
                "key": key,
                "value": value,
                "comment": "init from cfgservice",
                "dataChangeCreatedBy": user,
            },
        )

    def update_item(
        self,
        appid,
        key,
        value,
        env="dev",
        cluster_name="default",
        namespace="application",
        user=None
    ):
        if not user:
            user = self.APOLLO_USER
        return self.json_put(
            f"/envs/{env}/apps/{appid}/clusters/{cluster_name}/namespaces/{namespace}/items/{key}",
            {
                "key": key,
                "value": value,
                "comment": "init from cfgservice",
                "dataChangeLastModifiedBy": user,
            },
        )

    def release_config(
        self, appid, env="dev", cluster_name="default", namespace="application", user="apollo"
    ):
        return self.json(
            f"/envs/{env}/apps/{appid}/clusters/{cluster_name}/namespaces/{namespace}/releases",
            {"releaseTitle": "init from cfgservice", "releasedBy": user},
        )

    def add_associate_namespace(
        self, appid, namespace, env="dev", cluster_name="default"
    ):
        return self.json(
            f"/dada/apps/{appid}/namespaces",
            [{"env":env,"namespace":{"appId":appid,"clusterName":cluster_name,"namespaceName":namespace}}]
        )

    def get_namespaces(
        self,
        appid,
        env="ndev",
        cluster_name="default",
    ):
        return self.get(
            f"/envs/{env}/apps/{appid}/clusters/{cluster_name}/namespaces"
        )

    def application_configs(self, appid, env="ndev", cluster_name="default"):
        namespaces = self.get_namespaces(appid, env, cluster_name).json()
        configs = {}
        for n in namespaces:
            if n.get('namespaceName') == 'application':
                for i in n.get('items'):
                    configs[i.get('key')] = i.get('value')

                return configs


class ConfigDiff:
    r_key = r"<[A-Z0-9_]+>"

    def __init__(self, cfg_origins, apollo_configs):
        self.cfg_origins = cfg_origins
        self.apollo_configs = apollo_configs
        self.diffs = []
        self.cfg_configs = {}

    def clear_configs(self):
        pass

    def clear_config(self):
        pass

    def generate_diff(self):
        self.cfg_configs = self.adjust_value(self.cfg_origins.get('staticConfig'))
        self.cfg_configs.update(self.adjust_value(self.cfg_origins.get('dynamicConfig')))

        for k, v in self.cfg_configs.items():
            if isinstance(v, str):
                dump_v = v
                try:
                    dump_v = "'" + str(int(dump_v)) + "'"
                except Exception as e:
                    pass
            else:
                dump_v = str(v)
            if k not in self.apollo_configs:
                self.diffs.append({"action": 'add', "key": k, "cfg_value": dump_v})
            elif dump_v != self.apollo_configs.get(k):
                self.diffs.append({"action": 'update', "key": k, "cfg_value": dump_v, 'apo_value': self.apollo_configs.get(k)})

    def adjust_value(self, value, root=True):
        result = {}
        for k, v in value.items():
            pos = k.rfind('_')
            key_name = k[:pos]
            if root and key_name.startswith("<") and key_name.endswith(">"):
                key_name = key_name[1:-1]

            key_type = k[pos + 1:]
            if key_type == 'num':
                key_name = int(key_name)
            elif key_type == 'str':
                pass
            if type(v) == dict:
                v = self.adjust_value(v, root=False)
            elif type(v) == list:
                r = []
                for item in v:
                    if type(item) == dict:
                        r.append(self.adjust_value(item))
                    else:
                        r.append(item)
                v = r
            elif isinstance(v, str):
                for m in re.findall(self.r_key, v):
                    v = v.replace(m, "${" + m[1:-1] + "}")
            result[key_name] = v
        return result


cfg_origins = CfgService().get_default_version_configs(APP_ID)

apollo_api = ApolloApi()

apollo_configs = apollo_api.application_configs(APP_ID, env=ENV)

d = ConfigDiff(cfg_origins, apollo_configs)

d.generate_diff()

pprint.pprint(d.diffs)

if APOLLO_UPDATE:
    for d in d.diffs:
        if d.get('action') == 'update':
            res = apollo_api.update_item(APP_ID, d.get('key'), d.get('cfg_value'), env=ENV)
            if res.status_code != 200:
                raise ValueError(f"{d.get('key')} update error")
        elif d.get('action') == 'add':
            res = apollo_api.add_item(APP_ID, d.get('key'), d.get('cfg_value'), env=ENV)
            if res.status_code != 200:
                raise ValueError(f"{d.get('key')} add error")
if APOLLO_RELEASE:
    apollo_api.release_config(APP_ID, env=ENV)
