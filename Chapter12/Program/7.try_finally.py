try:
    a = int(input("Enter a number: "))
    print(a)
    

except Exception as e:
    print(e)
    
    
else:
    print("I am inside else")

finally:
    print("I am inside finally")
    print("This will always execute, regardless of whether an exception occurred or not.")

