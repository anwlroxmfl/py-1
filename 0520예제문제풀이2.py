print("9012번")

a = int(input())

for _ in range(a): 
    b = str(input())
    count = 0

    for char in b:
        if char == "(":
            count += 1
        else:
            count -= 1
        
    if count == 0:
        print("YES")
    else:
        print("NO")