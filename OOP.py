# Python Object-Oriented Programming

# Class is a blueprint for creating instances (objects)
class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

emp_1.first = 'Dan'
emp_1.last = 'Boakye'
emp_1.email = 'dan@test.com'
emp_1.pay = 1250000

emp_2.first = 'Qweku'
emp_2.last = 'Sarfo'
emp_2.email = 'qweku@test.com'
emp_2.pay = 158400

print(emp_1.email)
print(emp_2.email)