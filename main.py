#1-masala
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, new_grade):
        self.__grade = new_grade

s1 = Student("Ali", 5)

print(s1.grade)

s1.grade = 4
print(s1.grade)
