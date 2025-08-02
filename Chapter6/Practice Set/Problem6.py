marks = int(input("Enter your marks: "))

if(marks<=100 and marks>=90):
    grade = "EX"
elif(marks<90 and marks>=80):
    grade = "A"
elif(marks<80 and marks>=70):
    grade = "B"
elif(marks<70 and marks>=60):
    grade = "C"
elif(marks<60 and marks>=50):
    grade = "D"
elif(marks<50 ):
    grade = "F"

print("Your grade is: ", grade)
# The program takes the marks as input and checks the range of marks to assign a grade.