from text_tools.words import count_words

def get_sum(a: int, b: int) -> int:
    return a + b

def get_count(counts: dict[str, int], word: str) -> int | None:
    return counts.get(word)

if __name__ == "__main__":
    print(get_sum(5, 5))
    words: dict[str, int] = count_words("Hello my name is Alex")

    words_for_check: list[str] = ["alex", "john"]

    for word in words_for_check:
        count = get_count(words, word)      
        if count is not None:          
            count += 1
            print(f"Count for word {word} is {count}")
        else:
            print(f"Count for word {word} is not found")
        

