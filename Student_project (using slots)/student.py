class Student:
    __slots__ = ("name", "age", "grade")

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __repr__(self):
        return f"Student(name = {self.name}, age = {self.age}, grade = {self.grade})"