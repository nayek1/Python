class Employee:
    language = "Python"
    salary = 50000

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(F"The language is {self.language} and the salary is {self.salary}")


    def greet(self):

        print("Hello, welcome to the company!")

sagar = Employee("sagar", 100000, "C#")
sagar.name = "Sagar"
print(sagar.name, sagar.salary, sagar.language)