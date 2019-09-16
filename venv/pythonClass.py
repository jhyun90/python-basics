
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age


Alex = Employee('Alex', 20)
Amanda = Employee('Amanda', 30)
David = Employee('David', 15)
L = [Alex, Amanda, David]

L.sort(key=lambda x: x.age)
print([item.name for item in L])
