
from collections.abc import Iterator

def countdown(n: int) -> Iterator[int]:
    for i in range(n, 0, -1):
        yield i


if __name__ == "__main__":
    for i in countdown(10):
        print(i)

    counter = countdown(10)
    print(next(counter))