def limit_calls(limit):
    def wrapper(func):
        def inner():
            nonlocal limit
            if limit == 0:
                print("Функция не может быть вызвана")
                return
            func()
            limit -= 1
            print(f"Осталось использований {limit}")

        return inner
    return wrapper


@limit_calls(3)
def print1():
    pass

print1()
print1()
print1()
print1()