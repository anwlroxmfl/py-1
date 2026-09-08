print("예제 문제 1 딕셔너리")
print()
print("예제 3-1")
dic = {'name' : 'kim',
       'phone' : '010-1234-5678',
       'brith' : '2007-05-02'}
 
print (f"dic.values() : {dic.values()}")
print (f"dic.values() : {dic.items()}")

for key,value in dic.items():
    print(f"key : {key}")
    print(f"value : {value}")
print("----------------------------------")
print()
print("예제 문제 2 함수")
print()
print("예제 2-2-2")
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

result = add_many(1,2,3,4,5,6)
print(f"결과 : {result}")
print()
print("예제 3-2-2")
def kwargs_func(**kwargs):
    for key, value in kwargs.items():
        print(f"key : {key} / value : {value}")

kwargs_func(name='suwon', age='19', school='sishs')
print()
print("예제 문제 3 클래스")
class Person:
    def say_hello(self):
        print(f"self: {self}")

p1 = Person()
print(f"p1 : {p1}")
p1.say_hello()

p2 = Person()
print(f"p2 : {p2}")
p2.say_hello()

