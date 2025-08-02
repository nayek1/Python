class programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
        

p = programmer("Sagar", 100000, 123456)
print(p.name, p.salary, p.pin, p.company)

r = programmer("Ram", 500000, 12300456)
print(r.name, r.salary, r.pin, r.company)