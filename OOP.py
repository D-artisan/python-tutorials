# Python Object-Oriented Programming

# Class is a blueprint for creating instances (objects)
class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' + lname + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

emp_1 = Employee('Dan', 'Boakye', 1250000)
emp_2 = Employee('Qweku', 'Sarfo', 158400)

# print(emp_1)
# print(emp_2)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())

# When we run emp_1.fullname(), it is actually expanded as shown below
Employee.fullname(emp_1)
print(Employee.fullname(emp_1))
