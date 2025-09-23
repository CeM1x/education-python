import json
from student import Student
from group import Group

def save_group(group: Group, filename: str):
    data = [
        {"name": s.name,
         "age": s.age,
         "grade": s.grade,
         } for s in group.students
    ]
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_group(filename: str):
    group = Group()
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        for item in data:
            group.add_student(Student(item["name"], item["age"], item["grade"]))
        return group
