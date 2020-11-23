class Student:
    def __init__(self, name, grades) -> None:
        self.name = name
        self.grades = grades

    def average_grade(self):
        """
        docstring
        """
        return sum(self.grades) / len(self.grades)


student1 = Student("Bob", (100, 100, 90, 89, 95))
student2 = Student("Rolf", (100, 98, 89, 91, 97))

print(Student.average_grade(student1))
print(student2.average_grade())
