class Employee:
    language = "Python"
    salary = 50000

    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    def greet(self):
        print("Hello, welcome to the company!") 

sagar = Employee()
sagar.greet()
sagar.language = "Java"
sagar.getInfo()