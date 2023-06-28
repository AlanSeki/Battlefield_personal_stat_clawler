# 爬取站地1的个人生涯数据
# coding=utf-8
# Author AlanSeki@复旦大学材料科学系
import requests
from lxml import etree

str_y = 'r'
while str_y == 'r':
    # 读取玩家ID并生成battlefieldtracker的链接
    user_id = input("输入要查询的玩家ID（不区分大小写）：")
    print("玩家ID是:  %s" % user_id)
    str_url = 'https://battlefieldtracker.com/bf1/profile/pc/' + user_id
    # 20230628更新 加入步兵武器、载具（含飞机）的查询链接
    weapon_url = 'https://battlefieldtracker.com/bf1/profile/pc/' + user_id + '/weapons'
    vehicle_url = 'https://battlefieldtracker.com/bf1/profile/pc/' + user_id + '/vehicles'

    # 20230628更新 加入选择结构
    x = input("选择查询项目（0-综合数据；1-步战武器数据；2-载具数据）：")
    if (x == '0'):
        # 爬取battlefieldtracker上的个人综合数据
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
        }
        url = str_url
        resp = requests.get(url, headers=headers)
        # 以下检查是否爬取成功
        # if resp.status_code == 200:
        #     print(resp.text)
        # print('数据来源：' + str_url)

        # 列出HTML中所有数据标签
        resp.encoding = resp.apparent_encoding
        label = etree.HTML(resp.text)
        content = label.xpath('//div[@class="value"]/text()')

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
        mz_1 = 100 * float(mz)
        mz_2 = int(mz_1)
        mzl = str(mz_2)

        # 输出相关数据
        print("玩家的k/d数值是  " + content[2])
        print("玩家每分钟击杀  " + kpm)
        print("玩家场均击杀  " + cjjs)
        print("玩家每分钟得分  " + spm)
        print("玩家的胜率是  " + content[3] + "  胜 " + win + "  负 " + lose)
        print("玩家的总游戏时长是  " + content[5])
        print("玩家的最佳兵种是  " + zjbz)
        print("玩家的命中率是  " + mzl + "%")
        print("玩家的技巧分是  " + jqf)
        print("玩家的步战kd、kp是  " + bzkd + " " + bzkp)
        print("\n作者：AlanSeki@FDU")
        str_y = input("\n输入r再次查询，其他键退出：")
        if str_y != 'r':
            break

    else:
        if (x == "1"):
            # 爬取步战武器数据
            headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
            }
            url = weapon_url
            resp = requests.get(url, headers=headers)

            # 列出HTML中所有数据和武器类型标签
            resp.encoding = resp.apparent_encoding
            label = etree.HTML(resp.text)
            content = label.xpath('//div[@class="value"]/text()')
            content_1 = label.xpath('//div[@class="title"]/text()')

            # 整理数据 删除空格
            wq1 = content_1[25]
            wq_1 = wq1.strip()
            wq2 = content_1[27]
            wq_2 = wq2.strip()
            wq3 = content_1[29]
            wq_3 = wq3.strip()
            wq4 = content_1[31]
            wq_4 = wq4.strip()
            wq5 = content_1[33]
            wq_5 = wq5.strip()
            wq6 = content_1[35]
            wq_6 = wq6.strip()
            wq7 = content_1[37]
            wq_7 = wq7.strip()
            wq8 = content_1[39]
            wq_8 = wq8.strip()
            wq9 = content_1[41]
            wq_9 = wq9.strip()
            wq10 = content_1[43]
            wq_10 = wq10.strip()

            print("以下是玩家的个人常用武器数据:")
            print("1.  " + wq_1 + "  击杀  " + content[22] + "  kpm  " + content[23] + "  命中率  " + content[24])
            print("2.  " + wq_2 + "  击杀  " + content[25] + "  kpm  " + content[26] + "  命中率  " + content[27])
            print("3.  " + wq_3 + "  击杀  " + content[28] + "  kpm  " + content[29] + "  命中率  " + content[30])
            print("4.  " + wq_4 + "  击杀  " + content[31] + "  kpm  " + content[32] + "  命中率  " + content[33])
            print("5.  " + wq_5 + "  击杀  " + content[34] + "  kpm  " + content[35] + "  命中率  " + content[36])
            print("6.  " + wq_6 + "  击杀  " + content[37] + "  kpm  " + content[38] + "  命中率  " + content[39])
            print("7.  " + wq_7 + "  击杀  " + content[40] + "  kpm  " + content[41] + "  命中率  " + content[42])
            print("8.  " + wq_8 + "  击杀  " + content[43] + "  kpm  " + content[44] + "  命中率  " + content[45])
            print("9.  " + wq_9 + "  击杀  " + content[46] + "  kpm  " + content[47] + "  命中率  " + content[48])
            print("10.  " + wq_10 + "  击杀  " + content[49] + "  kpm  " + content[50] + "  命中率  " + content[51])
            print("\n作者：AlanSeki@FDU")
            str_y = input("\n输入r再次查询，其他键退出：")
            if str_y != 'r':
                break

        if (x == "2"):
            # 爬取载具数据
            headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
            }
            url = vehicle_url
            resp = requests.get(url, headers=headers)

            # 列出HTML中所有数据和武器类型标签
            resp.encoding = resp.apparent_encoding
            label = etree.HTML(resp.text)
            content = label.xpath('//div[@class="value"]/text()')
            content_1 = label.xpath('//div[@class="title"]/text()')

            # 整理数据 删除空格
            wq1 = content_1[3]
            wq_1 = wq1.strip()
            wq2 = content_1[5]
            wq_2 = wq2.strip()
            wq3 = content_1[7]
            wq_3 = wq3.strip()
            wq4 = content_1[9]
            wq_4 = wq4.strip()
            wq5 = content_1[11]
            wq_5 = wq5.strip()
            wq6 = content_1[13]
            wq_6 = wq6.strip()
            wq7 = content_1[15]
            wq_7 = wq7.strip()
            wq8 = content_1[17]
            wq_8 = wq8.strip()
            wq9 = content_1[19]
            wq_9 = wq9.strip()
            wq10 = content_1[21]
            wq_10 = wq10.strip()

            print("以下是玩家的个人常用载具数据（含定点武器、飞机）:")
            print("1.  " + wq_1 + "  击杀  " + content[0] + "  kpm  " + content[1])
            print("2.  " + wq_2 + "  击杀  " + content[2] + "  kpm  " + content[3])
            print("3.  " + wq_3 + "  击杀  " + content[4] + "  kpm  " + content[5])
            print("4.  " + wq_4 + "  击杀  " + content[6] + "  kpm  " + content[7])
            print("5.  " + wq_5 + "  击杀  " + content[8] + "  kpm  " + content[9])
            print("6.  " + wq_6 + "  击杀  " + content[10] + "  kpm  " + content[11])
            print("7.  " + wq_7 + "  击杀  " + content[12] + "  kpm  " + content[13])
            print("8.  " + wq_8 + "  击杀  " + content[14] + "  kpm  " + content[15])
            print("9.  " + wq_9 + "  击杀  " + content[16] + "  kpm  " + content[17])
            print("10.  " + wq_10 + "  击杀  " + content[18] + "  kpm  " + content[19])
            print("\n作者：AlanSeki@FDU")
            str_y = input("\n输入r再次查询，其他键退出：")
            if str_y != 'r':
                break