import itchat
from echarts import Echart, Legend, Pie

# itchat.login()

# 获取好友列表
# friends = itchat.get_friends(update=True)[0:]

# print(friends[0].__dict__)
#
# for f in friends[:1]:
#     for attr in f.__dict__:
#         print(getattr(f, attr))

# 初始化计数器，有男有女，当然，有些人是不填的
# male = female = other = 0

# 遍历这个列表，列表里第一位是自己，所以从"自己"之后开始计算
# 1表示男性，2女性
# for i in friends[1:]:
#     sex = i["Sex"]
#     if sex == 1:
#         male += 1
#     elif sex == 2:
#         female += 1
#     else:
#         other += 1
#
# # 总数算上，好计算比例啊～
# total = len(friends[1:])
# print(male)
# print(female)
# male = 142
# female = 63
# other = 20
# total = male + female + other
#
# chart = Echart(u'%s的微信好友性别比例' % u'止水', 'from WeChat')
# chart.use(Pie('WeChat',
#               [{'value': male, 'name': u'男性 %.2f%%' % (float(male) / total * 100)},
#                {'value': female, 'name': u'女性 %.2f%%' % (float(female) / total * 100)},
#                {'value': other, 'name': u'其他 %.2f%%' % (float(other) / total * 100)}],
#               radius=["50%", "70%"]))
# chart.use(Legend(["male", "female", "other"]))
# # del chart.json["xAxis"]
# # del chart.json["yAxis"]
# chart.plot()


# coding:utf-8
import itchat
import re
# jieba分词
import jieba
# wordcloud词云
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import PIL.Image as Image
import os
import numpy as np

itchat.login()
friends = itchat.get_friends(update=True)[0:]

# tList = []
# for i in friends:
#     # with open('./Signature.txt', 'a') as f:
#     #     f.write(i['NickName'])
#     #     f.write(i['Signature'])
#     #     f.write('\n')
#     signature = i["Signature"].replace(" ", "").replace("span", "").replace("class", "").replace("emoji", "")
#     rep = re.compile("1f\d.+")
#     signature = rep.sub("", signature)
#     tList.append(signature)

tList = ['但凡不能杀死你的，最终都会使你更强大。',
 '',
 '我爱工作，工作使我美丽',
 'whereveryouare',
 'ibelievethatmyheartwillgoon',
 '希望找到我的真爱，',
 '大学四年其实就是和颓废战斗的四年。',
 '',
 '',
 '室内外装修，材料批发零售，欢迎咨询汤女士18744980741',
 'evendotobesydoto',
 '海润无声船行无限',
 'justdoing',
 '身临其境，极致视界！',
 '',
 '路太平坦，只能带你去到平淡的地方',
 '默默无声……',
 '',
 '',
 '君子欲讷于言而敏于行',
 '',
 '我要稳稳的幸福。。。。',
 '',
 '',
 '',
 'Seizetheday',
 '畅想未来，不如畅享当下',
 '',
 '',
 '每一个你讨厌的现在，都有一个不努力的曾经…………',
 '静宜修身，简以养德',
 '服务好您的孩子就是我们最大的任务',
 '',
 '',
 '',
 '',
 'miasanmia',
 '',
 '',
 '在平坦的路面上曲折前行。',
 '言念君子，温润如玉',
 '',
 '',
 '这世间，除了生死，其他都是小事。',
 '走在一起是缘分，一起在走是幸福',
 'newlifeopen!',
 '',
 '一杯清茶',
 '人不为己，天诛地灭。良言一句三冬暖，恶语伤人六月寒。',
 '新电话号码：13823104874',
 '',
 'Hopeyouhavethestrengthtostartalloveragain.',
 '爱的真谛',
 '幸福要靠自己去努力',
 '天助自助者!',
 '。。。。。',
 '我给你的快乐埋单',
 '',
 '岁月静好，皆因有人负重前行！',
 '',
 '我想我一个人在等一个人。',
 '把每一天让它充实而忙碌起来迎2018',
 '慎思，笃行，明辨，博学，审问',
 '低调而又不失内涵的流氓！',
 '生如夏花之灿烂，死如秋叶之静美。',
 '茶飘香，酒罢去，聚朋友，再回楼',
 '花开堪折直须折',
 '那一纸繁荒难描少年心间伤。',
 "Don'tbeanasshole",
 '别动，我只欣赏你的背影。',
 '平和喜悦',
 '',
 '越努力，越幸运~',
 '，',
 '',
 '哈哈',
 '',
 '有缘无缘、无缘有缘',
 '行走即是圆梦，回望亦是前行。',
 '我，回来了。',
 '经历了痛苦才能蜕变',
 'Don’tpartwithyourillusions',
 '停下来看看窗外也许便懂得了什么是生活',
 '',
 '冷静，执着，激情，向往，努力！',
 '你不坚强，谁替你勇敢！',
 '',
 '欲戴王冠，必承其重；欲承其重，必锻其身；欲锻其身，必立其志',
 '世界总是给予我们想象得到的美妙',
 '天气真好~',
 '18786635894',
 'Adversityintroducesamantohimself.',
 '灯红酒绿下清心寡欲行',
 '人若精彩，天自安排。',
 '你应该是一场梦，我应该是一阵风',
 '빡세',
 '唯有知识让我们免于平庸~~',
 '最使你轻松愉快的是。健全的信仰、睡眠、音乐和欢笑。',
 '麦吉丽护肤达人',
 '',
 '哀其不幸，怒其不争',
 'NobobyownsU',
 '',
 '',
 '',
 '',
 '',
 '',
 '既往不恋，不负将来',
 '',
 '懦夫',
 '',
 '闭关养伤。',
 '不管在何时何地，都应该保持一颗良好的心态！',
 '',
 '(⊙o⊙)…loveisachordinlife.notasolo.',
 '',
 '胡敢',
 '',
 '',
 '念念不忘，必有回响。',
 '',
 '一蓑烟雨任平生',
 '。。。',
 '阳光过于温热，心却是凉的忽远忽近',
 '',
 '',
 '做一个被自己喜欢的姑娘',
 '茕茕白兔，东走西顾……',
 '感谢不杀之恩',
 '有一种修养叫闭口不言',
 '',
 '',
 '哭我为了感动谁，笑又为了碰着谁。',
 '刚好遇见你~',
 '有梦想谁都了不起！',
 '',
 '',
 '我觉得我爱了你了，从此以后，无论何时我都不能对你无动于衷。',
 '面子是给别人看的，日子是自己感受的。',
 '',
 '你',
 'lessismore',
 '行至水穷处，坐看云起时',
 '自律才能自由。',
 '自律，使我自由',
 '我于杀戮之中盛放',
 '亦如黎明中的花朵。',
 '',
 '做人如果没有梦想和咸鱼有什么区别',
 '大道無門',
 '温柔，美丽，知性',
 '静以修身，俭以养德。',
 '今年定个小目标，先挣它个…………\U0001f92a',
 '',
 '大顺加油站',
 '陪伴是最长情的告白',
 '如果你需要身居高位的人的认可，那么你其实是一个卑贱的人。',
 '人生不能像做菜，等所有配料好了，才下锅',
 '人生若只如初见，何事悲风秋画扇。',
 '可怜的流浪狗！',
 '真正的速度是看不见的',
 '黄昏是小调的喷烟\n记忆乘着气息归来',
 '我愿面朝大海，春暖花开……',
 '电话：18502139092',
 '人生若只如初见，那一切该多好！',
 '',
 'stayhungry',
 'stayfoolish',
 '小熊飞飞飞飞飞',
 '冰',
 '打招呼是良好沟通的开始<="',
 '本人无聊',
 '南有乔木，不可休思。北有青蔓，不可断愁',
 '有追求，有梦想，做一个好高骛远的人',
 '怕她知道又怕她不知道，想让她知道，又怕她已经知道却假装不知道',
 '努力到无能为力<="2764"></>️<="2764"></>️拼搏到感动自己<="',
 '东森药妆专注无添加护肤诚招代理',
 '有态度，不辜负人生！',
 '当你想给予的时候，才知道自己是多么的贫穷~',
 '小可爱',
 '低调做人，高调做事。',
 '',
 '亚健康时代',
 '',
 '我本将心向明月。',
 '断舍离',
 'Status',
 '贵州宏盟敏锐装饰有限公司',
 '子非鱼，焉知鱼之乐',
 '生活，哪有那么多的如果……',
 '',
 '你心有猛虎，\n细嗅蔷薇，\n你野心优雅，\n你就能逐风而行。',
 '不问归期',
 '',
 '',
 '一辈子幸福',
 '我爱我的祖国，我爱共产党，永葆革命青春',
 '',
 '超过十块钱的活动暂时不要叫我了',
 '我在深渊，追求星星',
 '',
 '路很长，慢慢走！',
 '心中自有远方',
 '春捂秋冻！！春捂秋冻！！春捂秋冻！！',
 '兔子的猎人',
 '',
 '要阳光明媚呀！',
 '明心见性，自觉觉他',
 '',
 'whocantellmewhatisforever',
 '',
 '',
 '饮水思源',
 '谢谢你，远道而来',
 '是你给我一个梦，未知人生的苦涩',
 '',
 'Awholelife',
 'Andthensome.']


print(tList.index('我于杀戮之中盛放'))
# 拼接字符串
text = "".join(tList)

word_list_jieba = jieba.cut(text, cut_all=True)
wl_space_split = " ".join(word_list_jieba)

d = os.path.dirname(__file__)
alice_coloring = np.array(Image.open(os.path.join(d, "wechat.jpg")))


# 这里要选择字体存放路径，这里是Mac的，win的字体在windows／Fonts中
my_wordcloud = WordCloud(background_color="white", max_words=2000, mask=alice_coloring,
                         max_font_size=40, random_state=42,
                         font_path='C:\windows\Fonts\STXIHEI.TTF').generate(wl_space_split)

image_colors = ImageColorGenerator(alice_coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
