a = 1
b = 2
c = 3
def gretest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
print(gretest(a, b, c))
