# coding:utf-8
import random
import pandas as pd
import math


if __name__ == '__main__':
    # 取同一个社区内所有的商户
    out_data = pd.read_csv('./summary_3100046037496308.csv')
    members = out_data['member_id'].values
    print(len(out_data))
    members = set(members)
    src_data = pd.read_csv('./sub_graph_result_3100046037496308.csv')
    print(len(src_data))
    for i in range(10):
        check_range = math.floor(len(src_data)/10)
        rand_num = random.randrange(1, check_range)
        check_res_1 = src_data[rand_num*10: (rand_num+1)*10]
        print(check_res_1)
        for item in check_res_1:
            print(item)
            print(type(item))
        print([(item['member_id_a'] in set(members) and item['member_id_b'] in set(members))
               for item in check_res_1])
