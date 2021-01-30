# 定义一个类
# class Washer():
#     # 方法
#     def wash(self):
#         print("我要洗衣服")
#         print(self)
#     def print_info(self):
#         print(f"gao{}")
# # 创建对象
# haier1 = Washer()
# print(haier1)   #self=haier1
# haier1.wash()

# 定义类
class Sweetpotato():
    def __init__(self):
        # 焙烤时间
        self.cook_time = 0
        self.cook_status = "生的"
        self.condiments = []
    def cook(self,time):
        # 烤地瓜的方法
        self.cook_time += time
        if 0 <= self.cook_time <3:
            self.cook_status = "生的"
        elif 3 <= self.cook_time < 5:
            self.cook_status = "半生不熟"
        elif 5 <= self.cook_time <8:
            self.cook_status = "熟了"
        elif self.cook_time > 8:
            self.cook_status = "糊了"
    