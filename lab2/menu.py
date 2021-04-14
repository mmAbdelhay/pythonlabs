from lab2 import *

print('welcome to lab 2')
flag = 1
while flag:
    print("what do ypu want ? \n1)get all employee\n2)get employee by ID\n3)add new employee\n4)exit")
    opration = input(">")
    if opration == '1':
        emps = Office().get_all_employees()
        print(emps)
    elif opration == '2':
        id = input('enter id : ')
        if int(id):
            emp = Office().get_employee(int(id))
            print(emp)
        else:
            print('id not valid')
    elif opration == '3':
        name = input('name : ')
        email = input('email : ')
        salary = input('salary : ')
        is_admin = input('is manager ?(1 : manager , 0 : isnt manager) :')
        health_rate = input('health rate (from 1 to 100) : ')
        Employee(name, email, int(salary), int(is_admin), int(health_rate))
    elif opration == '4':
        flag = 0
    else:
        print('opration not valid')
