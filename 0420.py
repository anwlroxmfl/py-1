class Animal: 
    def __init__(self,name):
        self.name = name

    def speak(self):
        print("동물이 소리를 낸다")

class Dog(Animal):
    def __init__(self, name,age):
        super().__init__(name)
        self.age = age
    def wag_tail(self):
        print("꼬리를 흔든다")

class Cat(Animal):
    def speak(self):
        print("야옹!")

class Pig(Animal):
    def speak(self):
        print("꿀꿀!")



# dog = Dog("멍멍이")
# print(dog.name)
# dog.speak()
# dog.wag_tail()

dog = Dog("멍멍이",3)
print(dog.name)
print(dog.age)



# -----------------------------------------------------------------------


class Calaulator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        print(self.num1+self.num2)

c = Calaulator(10,5)
c.add()


class AdvancedCalculator(Calaulator):
    def __init__(self, num1):
        super().__init__(num1,10)
        self.num1 = num1

    def mul(self):
        print(self.num1 * self.num2)

    # def add(self):
    #     print(self.num1 + self.num2 + 100)


    def add(self):
        super().add()
        print("추가 계산 완료")

c = AdvancedCalculator(5)
c.add()
c.mul()


        

