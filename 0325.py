result = 0 
def add(a, b):
    result = a + b
    print(result)

add(3,7)
add(3,9)
add(678,7)

def add(a, b, c):
    result = a + b + c
    return result

a = int(input("숫자 하나를 적으세요"))
b = int(input("숫자 하나를 적으세요"))
c = int(input("숫자 하나를 적으세요"))
result = add(a,b,c)
print (result)

def hello(a):
    print (a + " 안녕")

hello('홍길동')

#------------------------------------------------------

def add(*args):
    result = 0
    for i in args:
        result = result + i
    result = result / len(args)
    return result

result = add(1,3,5,7,8,9)

print("가변 매개변수를 이용한 결과:", result)

def even(*args):

    for i in args:
        if i % 2 ==1:
            print(i)

even(1,2,3,4,5,6,7)

def favor(*args):
    for i in args:
        print(i)
favor('탕수육','짬뽕')

def max(*args):
    max = 0
    for i in args:
        if( max < i ):
            max = i
    return max
print(max(1,2,3,4,5,6,7,8,9,9,11))

class calculator:
    def add(self, va1 , va2):
        return va1 + va2
 #--------------------------------------------------------------       
c1 = calculator()
c2 = calculator()
c3 = calculator()

result =  c1.add(3,5)
print(result)
