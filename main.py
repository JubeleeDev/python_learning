import os

from text_tools.lines import read_lines
from text_tools.words import count_words, normalize_spaces

if __name__ == "__main__":
    path = "./demo_data/notes.txt"
    folder_path: str = os.path.dirname(path)

    if not os.path.isdir(folder_path):
        print("create dir demo_data close to execution file before execute")
    else:
        lines: list[str] = read_lines(path)
        print(len(lines))
        words: str = " ".join(lines)
        normalized_words: str = normalize_spaces(words)
        print(count_words(normalized_words))