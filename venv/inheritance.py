# Inheritance

# Parent class
class Person:

    # Constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id

    # To get name
    def getName(self):
        return self.name

    # To get ID
    def getID(self):
        return self.id

    # To check if this person is employee
    def isEmployee(self):
        return false

    def display(self):
        print(self.name)
        print(self.id)

# Child class
class Employee( Person ):

    # Constructor
    def __init__(self, name, id, salary, post):
        # invoking the __init__ of the parent class
        Person.__init__(self, name, id)
        self.salary = salary
        self.post = post

    def getSalary(self):
        return self.salary

    def getPost(self):
        return self.post

    # To check if this person is employee
    def isEmployee(self):
        return true


# creation of an object of Person
p = Person('Rahul', 886012)
p.display()

# creation an object of Employee
emp = Employee('Rahul', 886012, '100000', 'xyz')
print(emp.getID(), emp.getName(), emp.getSalary(), emp.getPost())