
def count_words(text: str) -> dict[str, int]:
    words: list[str] = text.split()
    result: dict[str, int] = dict()
    for word in words:
        normalized_word: str = word.lower().strip()
        result[normalized_word] = result.get(normalized_word, 0) + 1
    return result

def normalize_spaces(text: str) -> str:
    words = text.strip().split()
    result: list[str] = []
    for word in words:       
        result.append(word.strip())

    return " ".join(result)

if __name__ == "__main__":
    print(count_words("alo alo dva tri dva raz Dva DVA"))
    print(count_words(normalize_spaces(" Hi    hi HI  ")))