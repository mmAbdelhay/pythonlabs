import random
import re
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Only_Me.88",
    database="office"
)

cur = mydb.cursor()
cur.autocommit = True
cur.execute('''CREATE SCHEMA IF NOT EXISTS office ''')
cur.execute("CREATE TABLE IF NOT EXISTS employee ( id INT AUTO_INCREMENT PRIMARY KEY, full_name VARCHAR(50), "
            "email VARCHAR(50), "
            "salary INT, is_manager INT, health_rate INT )")


class Person:
    full_name = None
    money = None
    sleep_mood = None
    healthRate = None

    def sleep(self, hours):
        pass

    def eat(self, meals):
        pass

    def buy(self, items):
        pass


class Employee(Person):
    ID = None
    Email = None
    Work_mood = None
    Salary = None
    Is_manager = None
    Health_rate = None

    def __init__(self, name, email, salary, is_manager, health_rate):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(regex, email):
            self.Email = email
        else:
            raise Exception("Sorry, email isn't valid")

        if salary >= 1000:
            self.Salary = salary
        else:
            raise Exception("Sorry, salary must be 1000 or more")

        if 0 < health_rate < 100:
            self.Health_rate = health_rate
        else:
            self.healthRate = random.randrange(1, 100, 1)

        if is_manager == 0 or is_manager == 1:
            self.Is_manager = is_manager
        else:
            raise Exception("Sorry, is_manager must be 0 or 1")

        self.full_name = name

        sql = "INSERT INTO office.employee (full_name, email, salary, is_manager, health_rate) VALUES " \
              "(%s, %s, %s, %s, %s) "
        val = (self.full_name, self.Email, self.Salary, self.Is_manager, self.Health_rate)
        cur.execute(sql, val)
        print("employee added")

    def sleep(self, hours):
        if hours < 7:
            print("tired")
        elif hours > 7:
            print("lazy")
        else:
            print("happy")

    def eat(self, meals):
        if meals == 3:
            print("health rate = 100")
        elif meals == 2:
            print("health rate = 75")
        elif meals == 1:
            print("health rate = 50")
        else:
            print("not human")

    def buy(self, items):
        for x in range(items):
            if self.Salary < 10:
                raise Exception("Sorry, is_manager must be 0 or 1")
            self.Salary -= 10

    def sendEmail(self, to, bodyreciever_name):
        f = open('email.txt', 'w')
        email = f'to : {to} \n' \
                f'subject : welcome email \n' \
                f'reciever : {bodyreciever_name} \n' \
                f'welcome to lab 2'
        f.write(email)
        f.close()


class Office:

    def get_all_employees(self):
        cur.execute("select * from office.employee")
        employees = cur.fetchall()
        return employees

    def get_employee(self, id):
        cur.execute("select * from office.employee where id = %s", (id,))
        employee = cur.fetchall()
        return employee

    def hire(self):
        print("hired")

    def fire(self):
        print("fired")
