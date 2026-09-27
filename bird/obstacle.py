from bird import RedBirds, BlueBirds, YellowBirds

class Obstacle:

    def __init__(self, name,strength):
        self.name = name
        self.strength = strength


    def be_attacked(self,bird):
        print(f"{bird.name} 冲向了 {self.name}")
        bird.use_skill()

        if isinstance(bird,RedBirds):
                damage = 80
        elif isinstance(bird,YellowBirds):
                damage = 70
        elif isinstance(bird,BlueBirds):
                damage = 30*3
        else:
            print('类型错误')

        self.strength -= damage;

        if self.strength <= 0:
            print(f'{self.name}被摧毁了')
        else:
            print(f"{self.name}被{bird.name}造成了{damage}点伤害")


red_bird = RedBirds("小红","red","火焰攻击")
yellow_bird = YellowBirds("小黄","yellow","艳阳冲击")
blue_bird  = BlueBirds('小蓝','blue',"分裂攻击，分裂成3只")

obs_1 = Obstacle('木桩',100)

obs_2 = Obstacle('石头',200)

obs_3 = Obstacle('金刚',300)


obs_1.be_attacked(red_bird)
obs_2.be_attacked(yellow_bird)
obs_3.be_attacked(blue_bird)
