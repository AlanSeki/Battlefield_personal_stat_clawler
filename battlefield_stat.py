# 爬取站地1的个人生涯数据
# coding=utf-8
# Author AlanSeki@复旦大学材料科学系
import requests
from lxml import etree

# 读取玩家ID并生成battlefieldtracker的链接
user_id = input("输入要查询的玩家ID（不区分大小写）：")
print("玩家ID是:  %s" % user_id)
str_url = 'https://battlefieldtracker.com/bf1/profile/pc/' + user_id
# print('数据来源：' + str_url)

# 爬取battlefieldtracker上的个人数据
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
}
url = str_url
resp = requests.get(url, headers=headers)
# 以下检查是否爬取成功
# if resp.status_code == 200:
#     print(resp.text)

# 列出HTML中所有标签
resp.encoding = resp.apparent_encoding
label = etree.HTML(resp.text)
content=label.xpath('//div[@class="value"]/text()')

# 整理数据 删除空格
str_12 = content[12]
cjjs = str_12.strip()
str_8 = content[8]
spm = str_8.strip()
str_13 = content[13]
kpm = str_13.strip()
str_15 = content[15]
zjbz = str_15.strip()
str_19 = content[19]
lose = str_19.strip()
str_20 = content[20]
win = str_20.strip()
str_35 = content[35]
bzkd = str_35.strip()
str_34 = content[34]
bzkp = str_34.strip()
str_21 = content[21]
jqf = str_21.strip()
str_22 = content[22]
mz = str_22.strip()
mz_1 = 100*float(mz)
mz_2 = int(mz_1)
mzl = str(mz_2)

# 输出相关数据
print("玩家的k/d数值是  "+content[2])
print("玩家每分钟击杀  "+kpm)
print("玩家场均击杀  "+cjjs)
print("玩家每分钟得分  "+spm)
print("玩家的胜率是  "+content[3]+"  胜 "+win+"  负 "+lose)
print("玩家的总游戏时长是  "+content[5])
print("玩家的最佳兵种是  "+zjbz)
print("玩家的命中率是  "+mzl+"%")
print("玩家的技巧分是  "+jqf)
print("玩家的步战kd、kp是  "+bzkd+" "+bzkp)

# 以下是为封装成exe文件所做的工作
print("\n按下Enter键退出......\n作者：AlanSeki@FDU")
input()