a = int(input("Enter your age: "))
if(a%2 == 0):
    print("a is even.")

if(a>=18):
    print("You are eligible to vote.")

elif(a<0):
    print("Invalid age.")

else:
    print("You are not eligible to vote.")

print("End of program.")