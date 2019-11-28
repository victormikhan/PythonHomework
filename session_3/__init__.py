from .characters_appear import *


def generate_squares(num: int) -> dict:
    return {i: i**2 for i in range(1, num + 1)}


def count_letters(string: str) -> dict:
    return {char: string.count(char) for char in string}


def combine_dicts(*args) -> dict:

    for dictionary in args[1:]:
        while dictionary:
            key, value = dictionary.popitem()

            if args[0].get(key) is not None:
                args[0][key] += value
            else:
                args[0].update({key: value})

    return args[0]
