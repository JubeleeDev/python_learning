
from collections.abc import Iterator

def countdown(n: int) -> Iterator[int]:
    for i in range(n, 0, -1):
        yield i


if __name__ == "__main__":
    for i in countdown(10):
        print(i)

    counter = countdown(10)
    print(next(counter))

    even_only = (y for y in countdown(10) if y % 2 == 0)
    squares = (y ** 2 for y in even_only)
    for i in squares:
        print(i)

    print("list comprehension")
    even_only = [y for y in range(10, 0, -1) if y % 2 == 0]
    print(even_only)
    squares = [y ** 2 for y in even_only]
    print(squares)