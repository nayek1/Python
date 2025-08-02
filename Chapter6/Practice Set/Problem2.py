m1 = int(input("Enter marks1: "))
m2 = int(input("Enter marks2: "))   
m3 = int(input("Enter marks3: "))


total_percentage =(100* (m1 + m2 + m3)) / 300

if(total_percentage >= 40 and m1 >= 33 and m2 >= 33 and m3 >= 33):
    print("Student is pass:", total_percentage)
else:
    print("Student is fail , better luck next time:", total_percentage)