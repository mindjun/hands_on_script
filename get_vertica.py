import json
import vertica_python
import shutil
import os


conn_info = {'host': '127.0.0.1',
             'port': 5433,
             'user': 'user_name',
             'password': 'user_pwd',
             'database': 'db_name',
             # 10 minutes timeout on queries
             'read_timeout': 600,
             # default throw error on invalid UTF-8 results
             'unicode_error': 'strict',
             # SSL is disabled by default
             'ssl': False,
             'connection_timeout': 5
             }


def get_file_path(sql, save=False):
    file_path_list = list()
    # using with for auto connection closing after usage
    with vertica_python.connect(**conn_info) as connection:
        cur = connection.cursor()
        cur.execute(sql)
        print("Client redirects to node")
        file_path_list.extend([item[0] for item in cur.fetchall()])
        if save:
            with open('./file_path.txt', 'a') as f:
                f.write(json.dumps(file_path_list))
            return './file_path.txt'
        else:
            return file_path_list


def move_file(source_path, target_path, save=False):
    if save:
        with open('./file_path.txt', 'r') as f:
            source_path = json.loads(f.read())

    for item in source_path:
        if not os.path.exists(item):
            continue

        new_path = os.path.join(target_path, os.path.split(item)[-1])
        shutil.copy(item, new_path)


if __name__ == '__main__':
    sql_ = ""
    file_path_ = get_file_path(sql_, save=True)
    # 保存文件的路径
    target_path_ = '/data/www/'
    move_file(file_path_, target_path_, save=True)
