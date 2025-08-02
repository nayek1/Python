def patterns(n):
    if(n==0):
        return
    print("*" * n)
    patterns(n-1)

patterns(5)

