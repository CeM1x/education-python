from typing import Generator


def read_file_by_words(file_name: str) -> Generator[str | list[str], int | None, None]:
    with open(file_name, "r") as file:
        words = (word for line in file for word in line.split())
        while True:
            try:
                word = next(words)
            except StopIteration:
                return
            n = yield word
            if n is not None:
                lst = []
                for _ in range(n):
                    try:
                        lst.append(next(words))
                    except StopIteration:
                        break
                yield lst

rfbw = read_file_by_words("text")
print(rfbw)
print(next(rfbw))
print(rfbw.send(5))
