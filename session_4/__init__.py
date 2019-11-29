import os
import re
import csv
from collections import Counter
from .modules.legb import enclosing_funcion


def write_sorted_names() -> None:

    with open(os.path.join('session_4/data', 'unsorted_names.txt'), 'r') as file:
        names = [line.strip() for line in file]

    with open(os.path.join('session_4/results', 'sorted_names.txt'), 'w') as file:
        file.write("\n".join([name for name in sorted(names)]))


def most_common_words(filepath: str, number_of_words: int=3) -> list:

    with open(filepath, 'r') as file:
        words = [re.sub('\,\.+', '', line.lower()) for line in re.split('\s', file.read())]

    words = list(filter(bool, words))

    counter = Counter(
        {word: words.count(word) for word in words}
    )

    return [item[0] for item in counter.most_common(number_of_words)]


def get_top_performers(filepath: str, number_of_students: int=5) -> list:

    with open(filepath, 'r') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        students = [student for student in csv_data]
        students.pop(0)

    students = sorted(students, key=lambda x: (float(x[-1]), len(x[-1])), reverse=True)[:number_of_students]

    return [student[0] for student in students]


def write_students_descending(filepath: str) -> None:

    with open(filepath, 'r') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        students = [student for student in csv_data]

    students[1:] = sorted(students[1:], key=lambda x: (x[1]), reverse=True)

    with open(os.path.join('session_4/results', 'students_descending.csv'), 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerows(students)


def remember_result(func):
    last_result = None

    def wrapper(*args):
        nonlocal last_result

        print(f"Last result = '{last_result}'")

        last_result = func(*args)
    return wrapper


def call_once(func):
    func_state = True

    def wrapper(*args):
        nonlocal func_state

        if func_state:
            func(*args)
            func_state = False

    return wrapper


@remember_result
def sum_list(*args):
    result = ""

    for item in args:
        result += str(item)

    print(f"Current result = '{result}'")

    return result


@call_once
def sum_of_numbers(a, b):
    print(a + b)

