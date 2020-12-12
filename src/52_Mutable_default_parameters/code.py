# ...(and why they're a bad idea)

from typing import List, Optional


class Student:
    def __init__(self, name: str, grades: Optional[List[int]] = None) -> None:
        # def __init__(self, name: str, grades: List[int] = []) -> None: -> THIS IS BAD!!!
        self.name = name
        self.grades = grades or []

    def take_exam(self, result: int):
        self.grades.append(result)


bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(95)
print(bob.grades)
print(rolf.grades)