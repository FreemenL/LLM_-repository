

class Birds:
    def __init__(self,name,color,skill):
        self.name = name
        self.color = color
        self.skill = skill

    def fly(self):
        print(f"{self.name} fly!")

    def call(self):
        print(f"{self.name} 发出叫声!")

    def use_skill(self):
        print(f"{self.name}使用技能!")


class  RedBirds(Birds):
    # def __init__(self,name,color,skill,sex):
    #     self.sex = sex
    #     super().__init__(name,color,skill,)

    def fly(self):
        super().fly()
        print(f"{self.name} 以稳定的速度飞行!")

    def call(self):
        print(f"{self.name} 发出ji-ji-ji叫声!")



class YellowBirds(Birds):

    def fly(self):
        super().fly()
        print(f"{self.name} 以飞快的速度飞行!")

    def call(self):
        print(f"{self.name} 发出ga-ga-ga的叫声!")


class BlueBirds(Birds):

    def fly(self):
        super().fly()
        print(f"{self.name} 以光的速度飞行!")

    def call(self):
        print(f"{self.name} 发出jiu-jiu-jiu的叫声!")

