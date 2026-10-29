
from text_tools.lines import read_lines
from text_tools.words import normalize_spaces, count_words

def get_report(filename: str) -> str:
    lines = read_lines(filename)
    count_lines = len(lines)
    total_words = count_words(normalize_spaces(" ".join(lines)))

    result = f"File: {filename}\nLines: {count_lines}\nWords:"
    
    for key, value in total_words.items():
        result += f"\n{key}: {value}"

    return result


