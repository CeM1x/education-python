from typing import Generator


def read_file_by_words(file_name: str) -> Generator[str | list[str], int | None, None]:
    with open(file_name, "r") as file:
        words = (word for line in file for word in line.split())
        try:
            while True:
                word = next(words)
                n = yield word
                if n is not None:
                    lst = [next(words) for _ in range(n)]
                    yield lst
        except StopIteration:
            return


rfbw = read_file_by_words("text")
print(rfbw)


print(next(rfbw)) # Вывод: one
print(rfbw.send(3)) # Вывод: ['two', 'three', 'four']
print(next(rfbw)) # Вывод: five
print(list(rfbw)) #Вывод: ['six', 'seven']