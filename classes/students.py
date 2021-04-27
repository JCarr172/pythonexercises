class Student:
    def __init__(self, name, age, class_ = 'student'):
        self.name = name
        self.age = age
        self.class_ = class_

    def average(self, physics, maths, chemistry):
        average = (physics+maths+chemistry)/3
        return print(f"The average score is {average}")

alicia = Student('Alicia', 22)
print(alicia.class_)
setattr(alicia, 'class_', 'Prefect')

print(alicia.class_)

alicia.average(10,15,20)