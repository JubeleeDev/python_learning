
import os

def write_lines(path: str, lines: list[str]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        for line in lines:
            print(line, file=f)

def read_lines(path: str) -> list[str]:
    with open(path, encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]

def count_lines(path: str) -> int:
    return len(read_lines(path))


if __name__ == "__main__":
    lines: list[str] = ["hello", "my name is Alex", "nice to meet you!"]
    path = "./demo_data/notes.txt"
    folder_path: str = os.path.dirname(path)

    if not os.path.isdir(folder_path):
        print("create dir demo_data close to execution file before execute")
    else:
        write_lines(path, lines)
        lines = read_lines(path)
        print(lines)
        print(count_lines(path))