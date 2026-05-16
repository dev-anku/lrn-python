from typing import TypedDict


class CharacterCount(TypedDict):
    char: str
    num: int


def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)


def get_char_dict(text: str) -> dict[str, int]:
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(dict: CharacterCount) -> int:
    return dict["num"]


def sorted_list(char_dict: dict[str, int]) -> list[CharacterCount]:
    sorted_list: list[CharacterCount] = []
    for ch in char_dict:
        sorted_list.append({"char": ch, "num": char_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
