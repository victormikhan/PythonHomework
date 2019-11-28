from functools import reduce


def lower_string(func):
    def wrapper(string: str):
        return func(string.lower())
    return wrapper


def quote_replacement(string: str) -> str:
    return string.translate(
        string.maketrans({'\'': '"','"': '\''})
    )


@lower_string
def palindrome_checker(string: str) -> bool:
    return string == string[::-1]


def custom_str_split(string: str, separator: str=' ') -> list:

    output = []
    last = 0

    for index, char in enumerate(string+separator):
        if char == separator:
            output.append(
                string[last:index]
            )

            last = index + 1

    return output


def split_by_index(string: str, indexes:list) -> list:

    string_length = len(string)

    if indexes[-1] < string_length:
        indexes.append(string_length)

    indexes = [0] + indexes

    return [string[prev:current] for prev, current in zip(indexes, indexes[1:]) ]


def get_digits(num: int) -> tuple:

    output = []

    while num:
        num, remainder = divmod(num, 10)
        output.append(remainder)

    return tuple(reversed(output))


def get_shortest_word(string: str) -> str:
    split_data = sorted(string.split(' '), key=len)

    return split_data[0]


def foo(num_list: list) -> list:

    output = []

    for num in num_list:
        temp = num_list[:]
        temp.remove(num)

        output.append(
            reduce(lambda x, y: x * y, temp)
        )

    return output


def get_pairs(lst: list) -> list:

    if len(lst) <= 1:
        return None

    return [tuple([prev, current]) for prev, current in zip(lst,lst[1:]) ]


