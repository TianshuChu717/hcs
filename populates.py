import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'hcs.settings')

django.setup()
from app.models import *
import _sqlite3
import random
import time
import requests
import os
import re
import itertools
import urllib
import sys

goods_list = ['Biscuits饼干类', 'Snacks零嘴', 'Crisps各式洋芋片', 'Confectionery糖业类',
              'Pet.Food宠物食品', 'Toiletries厕所用品', 'Pickles各式腌菜',
              'meet肉品类', 'FreshGradeLegs大鸡腿', 'FreshGradeBreast鸡胸肉',
              'ChickenDrumsticks小鸡腿', 'ChickenWings鸡翅膀', 'MincedSteak绞肉',
              'PigsLiver猪肝', 'Pigsfeet猪脚', 'PigsKidney猪腰', 'PigsHearts猪心',
              'PorkSteak没骨头的猪排', 'PorkChops连骨头的猪排',
              'RolledPorkBelly卷好的腰部瘦肉', 'Porksausagemeat做香肠的绞肉', 'SmokedBacon醺肉',
              'PorkFillet小里肌肉', 'SpareRibPorkchops带骨的瘦肉', 'SpareRibofPork小排骨肉',
              'Porkribs肋骨', 'BlackPudding黑香肠', 'PorkBurgers汉堡肉', 'Pork-pieces一块廋肉',
              'PorkDripping猪油滴', 'Lard猪油', 'Hock蹄膀', 'CasserolePork中间带骨的腿肉', 'Joint有骨的大块肉',
              '牛肉', 'StewingBeef小块的瘦肉', 'Steak&Kidney牛肉块加牛腰', 'Fryingsteak可煎食的大片牛排',
              'MimcedBeef牛绞肉', 'RumpSteak大块牛排', 'LegBeef牛键肉', 'OX-Tail牛尾', 'OX-heart牛心',
              'OX-Tongues牛舌', 'BarnsleyChops带骨的腿肉', 'ShoulderChops肩肉',
              'PorterHouseSteak腰上的牛排肉', 'ChuckSteak头肩肉筋', 'TenderisedSteak牛排',
              'Roll牛肠', 'Cowhells牛筋', 'Pigbag猪肚', 'HomeycomeTripe蜂窝牛肚',
              'TripePieces牛肚块', 'Bestthickseam白牛肚', 'Herring鲱', 'Salmon鲑',
              'Cod鳕', 'Tuna鲔鱼', 'Plaice比目鱼', 'Octopus鱆鱼', 'Squid乌贼', 'Dressedsquid花枝',
              'Mackerel鲭', 'Haddock鳕鱼', 'Trout鳟鱼', 'Carp鲤鱼',
              'CodFillets鳕鱼块', 'Conger(Eel)海鳗', 'SeaBream海鲤', 'Hake鳕鱼类',
              'RedMullet红鲣', 'SmokedSalmon熏鲑',
              'Smokedmackerelwithcrushedpeppercorn熏鲭', 'Herringroes鲱鱼子',
              'BoiledCodroes鳕鱼子', 'Oyster牡蛎',
              'Mussel蚌', 'Crab螃蟹', 'Prawn虾', 'Crabstick蟹肉条',
              'PeeledPrawns虾仁', 'KingPrawns大虾', 'Winkles田螺', 'WhelksTops小螺肉',
              'Shrimps小虾米', 'Cockles小贝肉', 'Lobster龙虾', '蔬果类','Potato马铃薯', 'Carrot红萝卜',
              'Onion洋葱', 'Aubergine茄子', 'Celery芹菜', 'WhiteCabbage包心菜', 'Redcabbage紫色包心菜',
              'Cucumber大黄瓜', 'Tomato蕃茄', 'Radish小红萝卜', 'Mooli白萝卜', 'Watercress西洋菜',
              'Babycorn玉米尖', 'Sweetcorn玉米', 'Cauliflower白花菜', 'Springonions葱',
              'Garlic大蒜', 'Ginger姜', 'Chineseleaves大白菜', 'Leeks大葱', 'Mustard&cress芥菜苗',
              'GreenPepper青椒', 'Redpepper红椒', 'Yellowpepper黄椒', 'Mushroom洋菇',
              'Broccoliflorets绿花菜', 'Courgettes绿皮南瓜', 'Coriander香菜', 'DwarfBean四季豆',
              'FlatBeans长形平豆', 'Iceberg透明包心菜', 'Lettuce莴苣菜', 'SwedeorTurnip芜菁',
              'Okra秋葵', 'Chillies辣椒', 'Eddoes小芋头', 'Taro大芋头', 'Sweetpotato蕃薯', 'Spinach菠菜',
              'Beansprots绿豆芽', 'Peas碗豆', 'Corn玉米粒', 'Sprot高丽小菜心', '水果', 'Lemon柠檬', 'Pear梨子',
              'Banana香蕉', 'Grape葡萄', 'Goldenapple黄绿苹果', 'Grannysmith绿苹果', 'Bramleys可煮苹果', 'Peach桃子',
              'Orange橙', 'Strawberry草莓', 'Mango芒果', 'Pineapple菠萝', 'Kiwi奇异果', 'Starfruit杨桃', 'Honeydew-melon蜜瓜',
              'Cherry樱桃', 'Date枣子', 'lychee荔枝', 'Grapefruit葡萄柚']


def populate():
    conn = _sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    dele2 = "delete from app_userprofile"
    dele3 = "delete from app_goods"
    dele4 = "delete from app_likes"
    cursor.execute(dele2)
    cursor.execute(dele3)
    cursor.execute(dele4)
    conn.commit()
    add_user("admin", "admin")
    add_goods_list = []
    for i in range(len(goods_list)):
        good_name = goods_list[i]
        add_goods_list.append(good_name)
        if i % 10 == 0:
            name = "customer" + str(i / 10)
            user = add_user(name, name)
            for j in range(10):
                if len(add_goods_list) > 0:
                    try:
                        gname = add_goods_list.pop()
                        # 已经爬取完了，只要生成对应关系就好了
                        # crawler(gname)
                        goods = Goods.objects.create(name=gname, price=random.randint(0, 100),
                                                     number=random.randint(0, 100),picture=gname+".jpg")
                        Likes.objects.create(likes_from=user, likes_to=goods, create_time=generate_date())
                        goods.likes_num = 1
                        goods.save()
                    except Exception as e:
                        print(str(e))
    for item in goods_list:
        Goods.objects.get_or_create(name=item)


def add_user(username, password):
    user_profile = UserProfile.objects.create(username=username,password=password)
    return user_profile


def generate_date():
    """⽣成随机时间YYYY-MM-DD"""
    a1 = (2021, 5, 1, 0, 0, 0, 0, 0, 0)  # 设置开始⽇期时间元组
    a2 = (2022, 3, 19, 23, 59, 59, 0, 0, 0)  # 设置结束⽇期时间元组（
    start = time.mktime(a1)  # ⽣成开始时间戳
    end = time.mktime(a2)  # ⽣成结束时间戳
    t = random.randint(start, end)  # 在开始和结束时间戳中随机取出⼀个
    date_touple = time.localtime(t)  # 将时间戳⽣成时间元组
    date = time.strftime("%Y-%m-%d", date_touple)  # 将时间元组转成string
    return date


# URL decode
str_table = {
    '_z2C$q': ':',
    '_z&e3B': '.',
    'AzdH3F': '/'
}

char_table = {
    'w': 'a',
    'k': 'b',
    'v': 'c',
    '1': 'd',
    'j': 'e',
    'u': 'f',
    '2': 'g',
    'i': 'h',
    't': 'i',
    '3': 'j',
    'h': 'k',
    's': 'l',
    '4': 'm',
    'g': 'n',
    '5': 'o',
    'r': 'p',
    'q': 'q',
    '6': 'r',
    'f': 's',
    'p': 't',
    '7': 'u',
    'e': 'v',
    'o': 'w',
    '8': '1',
    'd': '2',
    'n': '3',
    '9': '4',
    'c': '5',
    'm': '6',
    '0': '7',
    'b': '8',
    'l': '9',
    'a': '0'
}
char_table = {ord(key): ord(value) for key, value in char_table.items()}


# 解码
def decode(url):
    for key, value in str_table.items():
        url = url.replace(key, value)
    return url.translate(char_table)


def buildUrls(word):
    word = urllib.parse.quote(word)
    url = r"http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&fp=result&queryWord={word}&cl=2&lm=-1&ie=utf-8&oe=utf-8&st=-1&ic=0&word={word}&face=0&istype=2nc=1&pn={pn}&rn=60"
    urls = (url.format(word=word, pn=x) for x in itertools.count(start=0, step=60))
    return urls


re_url = re.compile(r'"objURL":"(.*?)"')


def resolveImgUrl(html):
    imgUrls = [decode(x) for x in re_url.findall(html)]
    return imgUrls


def downImgs(imgUrl, dirpath, imgName, imgType):
    filename = os.path.join(dirpath, imgName)
    try:
        res = requests.get(imgUrl, timeout=15)
        if str(res.status_code)[0] == '4':
            print(str(res.status_code), ":", imgUrl)
            return False
    except Exception as e:
        print('抛出异常:', imgUrl)
        print(e)
        return False
    with open(filename + '.' + imgType, 'wb') as f:
        f.write(res.content)
    return True


# 创建文件路径
def mkDir(dirName):
    dirpath = os.path.join(sys.path[0], dirName)
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)
    return dirpath


def crawler(name):
    path = '../hcs/media/image'
    dirpath = mkDir(path)
    word = name
    imgType = 'jpg'
    strtag = name
    numIMGS = 1
    urls = buildUrls(word)
    index = 0
    for url in urls:
        print("request for：", name)
        headers = {"User-Agent": "User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
        html = requests.get(url=url, timeout=100, headers=headers).content.decode('utf-8')
        imgUrls = resolveImgUrl(html)
        # print(imgUrls)
        if len(imgUrls) == 0:  # 没有图片则结束
            break
        for url in imgUrls:
            if downImgs(url, dirpath, strtag, imgType):
                index += 1
                print("get %s number" % index)
                # 双 break 跳出下载循环
            if index == numIMGS:
                break
        if index == numIMGS:
            print('done')
            break


if __name__ == '__main__':
    print('Starting population script...')
    populate()
    print("done")
