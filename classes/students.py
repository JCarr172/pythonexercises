class Student:
    def __init__(self, name, age, class_ = 'Student'):
        self.name = name
        self.age = age
        self.class_ = class_

    def average(self, physics, maths, chemistry):
        average = (physics+maths+chemistry)/3
        return print(f"The average score is {average}")

meg = Student('Meg', 23)
will = Student('Will', 23, 'Steward')
alicia = Student('Alicia', 22)

print(meg.class_)
setattr(meg, 'class_', 'Prefect')

print(meg.class_)
print(will.class_)
print(alicia.class_)
meg.average(10,15,20)