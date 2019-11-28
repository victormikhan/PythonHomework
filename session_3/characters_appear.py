from string import ascii_lowercase as alphabet


def all_strings(*lst) -> set:
    return {char for char in alphabet
            if all(string.find(char) != -1 for string in lst)}


def at_least_one_string(*lst) -> set:
    return {char for char in alphabet
            if any(string.find(char) != -1 for string in lst)}


def at_least_two_string(*lst) -> set:
    return {char for char in alphabet if sum([ string.find(char) != -1 for string in lst ]) >= 2}


def not_using(*lst) -> set:
    return {char for char in alphabet
            if all(string.find(char) == -1 for string in lst)}

