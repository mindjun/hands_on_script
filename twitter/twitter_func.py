"""
模拟推特功能：
1 发布
2 关注
3 取消关注
4 查看关注的用户
"""
import time


class LinkedNode(object):
    def __init__(self, val, ne=None):
        self.data = val
        self.next = ne
        # val 代表一条消息
        self.time = val.timestamp

    def set_next(self, node):
        self.next = node


class TwitterFunc(object):
    user_map = dict()

    @staticmethod
    def create_user(name):
        user_id = int(time.time())
        user_obj = TwitterFunc.User(user_id, name)
        TwitterFunc.user_map.update({user_id: user_obj})
        return user_obj

    class User(object):
        def __init__(self, _id, name):
            self.name = name
            self.id = _id
            self.flower_set = set()
            # 发布的 twitter 用链表表示，链表头是最新的发布
            self.twitter = None
            self.flower_set.add(self.id)

        def flower(self, _id):
            self.flower_set.add(_id)

        def unflower(self, _id):
            if _id != self.flower_set:
                self.flower_set.remove(_id)

        def post(self, twitter_content):
            twitter_obj = TwitterFunc.TwitterContent(twitter_content, self.name)
            twitter_node = LinkedNode(twitter_obj)
            twitter_node.set_next(self.twitter)
            self.twitter = twitter_node

        def get_new_feed(self):
            """
            获取关注的 twitter 列表
            :return:
            """
            flower_twitter_list = [TwitterFunc.user_map.get(_id).twitter for _id in self.flower_set]
            node_list = list()
            for twitter in flower_twitter_list:
                while twitter:
                    node_list.append(twitter)
                    twitter = twitter.next
            node_list.sort(key=lambda x: getattr(x, 'time'))
            return [{node.data.user_name: [node.data.content, node.data.timestamp]} for node in node_list]

    class TwitterContent(object):
        def __init__(self, content, user_name):
            self.content = content
            self.user_name = user_name
            self.timestamp = int(time.time())


if __name__ == '__main__':
    user_1 = TwitterFunc.create_user('user_1')
    time.sleep(1)
    user_2 = TwitterFunc.create_user('user_2')
    # user_3 = TwitterFunc.create_user('user_3')

    user_1.post('user_1_0')
    time.sleep(1)
    user_2.post('user_2_1')
    time.sleep(1)
    user_1.post('user_1_2')
    time.sleep(1)
    user_2.post('user_2_3')
    time.sleep(1)
    user_1.post('user_1_4')

    print(user_1.get_new_feed())
    user_1.flower(user_2.id)
    print(user_1.get_new_feed())
    user_1.unflower(user_2.id)
    print(user_1.get_new_feed())
