import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'hcs.settings')

django.setup()
from app.models import *
import _sqlite3
import random
import time

goods_list = ['Biscuits饼干类', 'Snacks 零嘴', 'Crisps 各式洋芋片', 'Confectionery糖业类',
              'Pet.Food 宠物食品', 'Toiletries 厕所用品', 'Poultry 家禽类', 'Pickles 各式腌菜',
              'meet肉品类', 'FreshGradeLegs大鸡腿', 'FreshGradeBreast鸡胸肉',
              'ChickenDrumsticks小鸡腿', 'ChickenWings鸡翅膀', '猪各部分名称：', 'MincedSteak绞肉',
              'PigsLiver猪肝', 'Pigsfeet猪脚', 'PigsKidney猪腰', 'PigsHearts猪心',
              'PorkSteak没骨头的猪排', 'PorkChops连骨头的猪排', 'RolledPorkloin卷好的腰部瘦肉',
              'RolledPorkBelly卷好的腰部瘦肉连带皮', 'Porksausagemeat做香肠的绞肉', 'SmokedBacon醺肉',
              'PorkFillet小里肌肉', 'SpareRibPorkchops带骨的瘦肉', 'SpareRibofPork小排骨肉',
              'Porkribs肋骨可煮汤食用', 'BlackPudding黑香肠', 'PorkBurgers汉堡肉', 'Pork-pieces一块块的廋肉',
              'PorkDripping猪油滴', 'Lard猪油', 'Hock蹄膀', 'CasserolePork中间带骨的腿肉', 'Joint有骨的大块肉',
              '牛肉', 'StewingBeef小块的瘦肉', 'Steak&Kidney牛肉块加牛腰', 'Fryingsteak可煎食的大片牛排',
              'MimcedBeef牛绞肉', 'RumpSteak大块牛排', 'LegBeef牛键肉', 'OX-Tail牛尾', 'OX-heart牛心',
              'OX-Tongues牛舌', 'BarnsleyChops带骨的腿肉', 'ShoulderChops肩肉',
              'PorterHouseSteak腰上的牛排肉', 'ChuckSteak头肩肉筋', 'TenderisedSteak拍打过的牛排',
              'Roll牛肠', 'Cowhells牛筋', 'Pigbag猪肚', 'HomeycomeTripe蜂窝牛肚',
              'TripePieces牛肚块', 'Bestthickseam白牛肚', '', '海产类', '鱼：', 'Herring鲱', 'Salmon鲑',
              'Cod鳕', 'Tuna鲔鱼', 'Plaice比目鱼', 'Octopus鱆鱼', 'Squid乌贼', 'Dressedsquid花枝',
              'Mackerel鲭', 'Haddock北大西洋产的鳕鱼', 'Trout鳟鱼、适合蒸来吃', 'Carp鲤鱼',
              'CodFillets鳕鱼块，可做鱼羹，或炸酥鱼片都很好吃', 'Conger(Eel) 海鳗', 'SeaBream海鲤', 'Hake鳕鱼类',
              'RedMullet红鲣，可煎或红烧来吃', 'SmokedSalmon熏鲑*',
              'Smokedmackerelwithcrushedpeppercorn带有黑胡椒粒的熏鲭*', 'Herringroes鲱鱼子',
              'BoiledCodroes鳕鱼子', '*以上两种鱼只需烤好手放柠檬汁就十分美味了', '海鲜', 'Oyster牡蛎',
              'Mussel蚌、黑色、椭圆形、没壳的即为淡菜', 'Crab螃蟹', 'Prawn虾', 'Crabstick蟹肉条',
              'PeeledPrawns虾仁', 'KingPrawns大虾', 'Winkles田螺、小螺丝', 'WhelksTops小螺肉',
              'Shrimps小虾米', 'Cockles小贝肉', 'Lobster龙虾', '蔬果类', '蔬菜：', 'Potato马铃薯', 'Carrot红萝卜',
              'Onion洋葱', 'Aubergine茄子', 'Celery芹菜', 'WhiteCabbage包心菜', 'Redcabbage紫色包心菜',
              'Cucumber大黄瓜', 'Tomato蕃茄', 'Radish小红萝卜', 'Mooli白萝卜', 'Watercress西洋菜',
              'Babycorn玉米尖', 'Sweetcorn玉米', 'Cauliflower白花菜', 'Springonions葱',
              'Garlic大蒜', 'Ginger姜', 'Chineseleaves大白菜', 'Leeks大葱', 'Mustard&cress芥菜苗',
              'GreenPepper青椒', 'Redpepper红椒', 'Yellowpepper黄椒', 'Mushroom洋菇',
              'Broccoliflorets绿花菜', 'Courgettes绿皮南瓜，形状似小黄瓜，但不可生食', 'Coriander香菜', 'DwarfBean四季豆',
              'FlatBeans长形平豆', 'Iceberg透明包心菜', 'Lettuce莴苣菜', 'SwedeorTurnip芜菁',
              'Okra秋葵', 'Chillies辣椒', 'Eddoes小芋头', 'Taro大芋头', 'Sweetpotato蕃薯', 'Spinach菠菜',
              'Beansprots绿豆芽', 'Peas碗豆', 'Corn玉米粒', 'Sprot高丽小菜心', '水果', 'Lemon 柠檬', 'Pear 梨子',
              'Banana 香蕉', 'Grape 葡萄', 'Golden apple 黄绿苹果、脆甜', 'Granny smith 绿苹果、较酸', 'Bramleys 可煮食的苹果', 'Peach 桃子',
              'Orange 橙', 'Strawberry 草莓', 'Mango 芒果', 'Pineapple 菠萝', 'Kiwi 奇异果', 'Starfruit 杨桃', 'Honeydew-melon 蜜瓜',
              'Cherry 樱桃', 'Date 枣子', 'lychee 荔枝', 'Grape fruit 葡萄柚']


def populate():
    conn = _sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    dele = "delete from auth_user;"
    dele2 = "delete from app_userprofile"
    dele3 = "delete from app_goods"
    dele4 = "delete from app_likes"
    cursor.execute(dele)
    cursor.execute(dele2)
    cursor.execute(dele3)
    cursor.execute(dele4)
    conn.commit()
    add_user("admin", "admin", "admin")
    add_goods_list = []
    for i in range(50):
        good_name = goods_list[random.randint(0, len(goods_list))]
        add_goods_list.append(good_name)
        if i % 10 == 0:
            name = "customer" + str(i / 10)
            user = add_user(name, name, name)
            for j in range(10):
                if len(add_goods_list) > 0:
                    try:
                        goods = Goods.objects.create(name=add_goods_list.pop(), price=random.randint(0, 100),
                                                     number=random.randint(0, 100))
                        Likes.objects.create(likes_from=user, likes_to=goods, create_time=generate_date())
                        goods.likes_num = 1
                        goods.save()
                    except Exception as e:
                        print(str(e))
    for item in goods_list:
        Goods.objects.get_or_create(name=item)


def add_user(username, password, name):
    user1 = User.objects.create(username=username, password=password)
    user_profile = UserProfile.objects.create(user=user1, name=name)
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


if __name__ == '__main__':
    print('Starting population script...')
    populate()
    print("done")
