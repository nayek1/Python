l = ["Harry", "Ron", "Hermione", "Draco", "Neville"]

name = input("Enter your name: ")

if name in l:
    print(f"{name} is in the list.")

else:
    print(f"{name} is not in the list.")