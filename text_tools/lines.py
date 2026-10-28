def write_lines(path: str, lines: list[str]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        for line in lines:
            print(line, file=f)

def read_lines(path: str) -> list[str]:
    with open(path, encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]

def count_lines(path: str) -> int:
    return len(read_lines(path))
