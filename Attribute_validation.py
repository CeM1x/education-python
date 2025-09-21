from string import ascii_letters


class Person:
    S_RUS = "абвгдеёжзийклмнопрстуфхцчшщьыъзюя-"
    RUS_UPPER = S_RUS.upper()
    def __init__(self, fio, old, passport, weight):
        self.validate_fio(fio)
        self.validate_old(old)
        self.validate_passport(passport)
        self.validate_weight(weight)

        self.__fio = fio.split()
        self.__old = old
        self.__passport = passport
        self.__weight = weight

    @classmethod
    def validate_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("ФИО должно быть строкой")

        f = fio.split()
        if len(f) != 3:
            raise TypeError("Неверный формат записи")

        letters = ascii_letters + cls.S_RUS + cls.RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError("В ФИО должен быть хотя бы 1 символ")
            if len(s.strip(letters)) != 0:
                raise TypeError("В ФИО можно использовать только буквы и дефис")


    @classmethod
    def validate_old(cls, old):
        if type(old) != int or 4 > old or old > 120:
            raise TypeError("Возраст должен быть целым числом от 4 до 120")

    @classmethod
    def validate_passport(cls, passport):
        if type(passport) != str:
            raise TypeError("Паспорт должен быть строкой")
        if len(passport.split()) != 2 or len(passport.split()[0]) != 4 or len(passport.split()[1]) != 6:
            raise TypeError("Неверный формат паспорта")

        for p in passport.split():
            if not p.isdigit():
                raise TypeError("Серия и номер паспорта должны быть числами")

    @classmethod
    def validate_weight(cls, weight):
        if type(weight) != float or weight < 20:
            raise TypeError("Вес должен быть вещественным числом от 20 и выше")

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, new_old):
        self.validate_old(new_old)
        self.__old = new_old

    @property
    def weight(self):
        return self.__old

    @weight.setter
    def weight(self, new_weight):
        self.validate_weight(new_weight)
        self.__weight = new_weight

    @property
    def passport(self):
        return self.__old

    @passport.setter
    def passport(self, new_passport):
        self.validate_passport(new_passport)
        self.__passport = new_passport

p = Person("Сыров Семён Сергеевич", 20, "1234 567890", 69.3)
print(p.__dict__)
p.old = 100
p.passport = "0987 654321"
p.weight = 70.6
print(p.__dict__)