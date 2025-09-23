import pytest
from student import Student
from group import Group


def test_student_slot():
    s = Student("Вика", 19, 4.5)
    assert s.name == "Вика"
    assert s.age == 19
    assert s.grade == 4.5

    with pytest.raises(AttributeError):
        s.city = "Москва"


def test_group_add_find_remove():
    g = Group()
    s1 = Student("Аня", 19, 4.5)
    s2 = Student("Иван", 20, 3.9)
    g.add_student(s1)
    g.add_student(s2)
    assert g.find_student("Иван") == s2
    g.remove_student("Иван")
    assert g.find_student("Иван") is None


def test_group_average_grade():
    g = Group()
    g.add_student(Student("Аня", 19, 4.0))
    g.add_student(Student("Мария", 18, 5.0))
    assert pytest.approx(g.average_grade(), 0.1) == 4.5
