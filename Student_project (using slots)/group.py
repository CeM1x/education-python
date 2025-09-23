from student import Student

class Group:
    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        if student not in self.students:
            self.students.append(student)

    def remove_student(self, name):
        for s in self.students:
            if s.name == name:
                self.students.remove(s)
                break

    def find_student(self, name):
        for s in self.students:
            if s.name == name:
                return s
        return None

    def average_grade(self):
        if not self.students:
            return 0
        else:
            return sum(s.grade for s in self.students) / len(self.students)

    def list_students(self, sort_by="name", reverse = False):
        return sorted(self.students, key=lambda s: getattr(s, sort_by), reverse=reverse)