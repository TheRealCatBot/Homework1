# Task 1
class Calculator:
    def __init__(self, calculatron):
        self.name = calculatron

    def Addition(self, a, b):
        return a + b

    def Subtraction(self, a, b):
        return a - b

    def Division(self, a, b):
        return a / b

    def Multiplication(self, a, b):
        return a * b


addition = Calculator("addition")
subtraction = Calculator("subtraction")
multiplication = Calculator("multiplication")
division = Calculator("division")
print(addition.Addition(2, 4))
print(subtraction.Subtraction(14, 2))
print(multiplication.Multiplication(9, 9))
print(division.Division(8, 4))


# Task 2
class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return (self.width + self.length) * 2

    def print_info(self):
        print(
            f"Length:{self.length}, Width: {self.width}, General Info: Area: "
            f"{self.width * self.length}" f" Perimeter: {(self.width + self.length) * 2}")


rectangle = Rectangle(7, 12)
print(rectangle.perimeter())
print(rectangle.area())
rectangle.print_info()

# Task 3

exeldocument = open("dataset1.csv", "r", encoding='utf-8')


class Employee:
    def __init__(self, name, surname, salary, age):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.age = age


employees = []
for i in range(0,100):
    temporary = exeldocument.readline()
    temporarylist = temporary.split(",")
    _name = temporarylist[0]
    _surname = temporarylist[1]
    _age = int(temporarylist[2])
    _salary = int(temporarylist[3])
    employees.append(Employee(_name,_surname,_salary,_age))

lowestSalaryIndex = 0
lowestSalary = employees[0].salary
oldestAgeIndex = 0
oldestAge = employees[0].age
for i in range(0, len(employees)):
    if employees[i].salary < lowestSalary:
        lowestSalary = employees[i].salary
        lowestSalaryIndex = i

    if employees[i].age > oldestAge:
        oldestAge = employees[i].age
        oldestAgeIndex = i

print("Employee With The Lowest Salary: \n"
f"{employees[lowestSalaryIndex].name, employees[lowestSalaryIndex].surname}"
f"{employees[lowestSalaryIndex].age, employees[lowestSalaryIndex].salary}")

print("Oldest Employee: \n"
f"{employees[oldestAgeIndex].name, employees[oldestAgeIndex].surname}"
f"{employees[oldestAgeIndex].age, employees[oldestAgeIndex].salary}")
