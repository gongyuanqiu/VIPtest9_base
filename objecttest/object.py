class master():
    def __init__(self):
        self.kongfu = "[五香煎饼果子]"
    def make_cake(self):
        print(f"运用{self.kongfu}制作")
class School():
    def __init__(self):
        self.kongfu = "[香辣煎饼锅子]"
    def make_cake(self):
        print(f"运用{self.kongfu}制作")
class Prentice(master,School):
    def __init__(self):
        self.kongfu = "[独创]"
    def make_cake(self):
        self.__init__()
        print(f"运用{self.kongfu}制作")
    def make_master_cake(self):
        master.__init__(self)
        master.make_cake(self)
    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)
xiaoming = Prentice()
print(xiaoming.kongfu)
xiaoming.make_cake()
xiaoming.make_school_cake()
xiaoming.make_master_cake()