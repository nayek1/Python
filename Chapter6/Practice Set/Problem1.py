a = int(input("Enter number1: "))
b = int(input("Enter number2: "))
c = int(input("Enter number3: "))
d = int(input("Enter number4: "))

if a > b and a > c and a > d:
    print("Number1 is the greatest")
elif b > a and b > c and b > d:
    print("Number2 is the greatest")
elif c > a and c > b and c > d:
    print("Number3 is the greatest")
elif d > a and d > b and d > c:
    print("Number4 is the greatest")