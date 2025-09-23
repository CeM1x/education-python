from student import Student
from group import Group
from storage import save_group, load_group

def main():
    group = Group()

    # Добавляем студентов
    group.add_student(Student("Аня", 19, 4.5))
    group.add_student(Student("Иван", 20, 3.9))
    group.add_student(Student("Мария", 18, 4.8))

    print("Все студенты:", group.students)
    print("Средний балл:", group.average_grade())

    # Поиск
    print("Найден:", group.find_student("Иван"))

    # Удаление
    group.remove_student("Иван")
    print("После удаления:", group.students)

    # Сортировка по баллу
    print("Сортировка по баллу:", group.list_students(sort_by="grade", reverse=True))

    # Сохранение и загрузка
    save_group(group, "group.json")
    group2 = load_group("group.json")
    print("Загруженная группа:", group2.students)

    # Попробуем добавить несуществующее поле
    try:
        s = Student("Тест", 21, 4.1)
        s.city = "Москва"  # Ошибка
    except AttributeError as e:
        print("Ошибка:", e)


if __name__ == "__main__":
    main()
