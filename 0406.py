class Cal: 
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        return self.first + self.second
        
    

cal1 = Cal(2,4)
cal2 = Cal(2,5)

print("cal1.add() : ",cal1.add())
print("cal2.add() : ",cal2.add())

cal1.setdata(4,2)
cal2.setdata(3,5)

print("cal1.add() : ",cal1.add())
print("cal2.add() : ",cal2.add())

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print("안녕하세요, 저는",self.name,"이고",self.age,"입니다")
s20820 = Student("aka", 100)
s20820.introduce()


class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    def accelerate(self):
        print("속도 10 상승!")
        self.speed += 10
        print("현재 속도 : ",self.speed)
        
s20820 = Car("aka", 100)
s20820.accelerate()

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

        
c = Character("aka", 100)
c.attack()
c.damaged(10)


class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self,money):
        self.balance += money
        print(money,"만큼 잔액이 추가되어",self.balance,"원이 남으셨습니다")
    def withdraw(self, money):
        self.balance -= money
        print(money,"만큼 잔액이 감소되어",self.balance,"원이 남으셨습니다")
        

        
c = Bank("aka", 100)
c.deposit(10)
c.withdraw(10)


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
    def heal(self, healing):
        self.hp += healing
        print(healing,"만큼 체력이 회복되었습니다")
    def status(self):
        print("현재 체력 : ",self.hp)

        
c = Character("aka", 100)
c.attack()
c.heal(10)
c.status()
c.damaged(10)


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
        print("현재 체력 : ",self.hp)
        if self.valid == 1:
            print("공격 가능")


c = Character("aka", 100)
c.heal(10)
c.status()
c.attack()
c.damaged(200)










