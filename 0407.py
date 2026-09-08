class Animal: 
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def speak(self,sound):
        print(self.name,"이(가)",sound,"소리를 냅니다!")

dog = Animal("뽀삐", 3)
cat = Animal("야옹이", 2)

dog.speak("멍멍")
cat.speak("야옹")


class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    def attack(self):
        print(self.name,"이(가) 공격하였다")
    def damaged(self, damage):
        print(damage, "대미지 공격!")
        self.hp -= damage
        print("현재 남은 체력 : ",self.hp)
    def heal(self):
        self.hp += 10
        print("10만큼 체력이 회복되었습니다")
    
class Character:
    def __init__(self, name, hp):
        self.valid = 1
        self.name = name
        self.hp = hp
    def attack(self):
        print(self.name,"이(가) 공격하였다")
    def damaged(self, damage):
        print(damage, "대미지 공격!")
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print("현재 남은 체력 : ",self.hp)
        if self.hp == 0:
            self.valid = 0
            print("피가 없어 죽으셨습니다 heal을 통해 살아나세요")
    def heal(self, healing):
        print("힐을 받았다")
        self.hp += healing
        if self.valid == 0:
            self.hp = 100
            print("다시 생존")
            self.valid = 1
        else:
            print("현재 살아있습니다")
    def status(self):
        print("이름 : ",self.name,"현재 체력 : ",self.hp)
        if self.valid == 1:
            print("공격 가능")


class Character:
    def __init__(self, name, power, hp, max_hp):
        self.valid = 1
        self.power = power
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
    def attack(self):
        print(self.name,"이(가) 공격하였다")
    def damaged(self, damage):
        print(damage, "대미지 공격!")
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print("현재 남은 체력 : ",self.hp)
        if self.hp == 0:
            self.valid = 0
            print("피가 없어 죽으셨습니다 heal을 통해 살아나세요")
    def heal(self, healing):
        print("힐을 받았다")
        self.hp += healing
        if self.max_hp < self.hp:
            self.hp = self.max_hp
            print("체력이 가득찼습니다")
        if self.valid == 0:
            self.hp = 100
            print("다시 생존")
            self.valid = 1
        else:
            print("현재 살아있습니다")
    def status(self):
        print("이름 : ",self.name,"현재 체력 : ",self.hp)
        if self.valid == 1:
            print("공격 가능")
    def attack2(self, target):
        target.damaged(self.power)
        print(self.name,"이(가)",target.name,"을(를) 공격! 데미지 : ",self.power)
hero = Character("히어로",20,50,50)
captin_america = Character("캡턴어메리카",20,50,50)

captin_america.attack2(hero)


