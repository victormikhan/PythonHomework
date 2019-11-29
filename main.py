from session_2 import *
from session_3 import *
from session_4 import *

def main():

    """session 2"""
    print(quote_replacement('replaced quote \' \" '))
    print(palindrome_checker('Able was I ere I saw Elba'))
    print(custom_str_split('Able was I ere I saw Elba', separator=' '))
    print(split_by_index('pythoniscool,isn\'tit?', [6,8,12,13,18]))
    print(get_digits(123456789))
    print(get_shortest_word('Python is simple and effecti\'ve!'))
    print(foo([1,2,3,4,5]))
    print(get_pairs(['need', 'to', 'sleep', 'more']))

    print("\n")

    """session 3"""
    string = ['hello', 'world', 'python']
    print(characters_appear.all_strings(*string))
    print(characters_appear.at_least_one_string(*string))
    print(characters_appear.at_least_two_string(*string))
    print(characters_appear.not_using(*string))
    print(generate_squares(5))
    print(count_letters('stringsample'))
    print(combine_dicts({'a': 100, 'b': 200}, {'a': 200, 'c': 300}, {'a': 300, 'd': 100}))

    print("\n")

    """session 4"""
    write_sorted_names()  # look for results in session_4/results folder
    print(most_common_words('session_4/data/lorem_ipsum.txt', 2))
    print(get_top_performers('session_4/data/students.csv', 5))
    write_students_descending('session_4/data/students.csv') # look for results in session_4/results folder

    print("\n")

    enclosing = enclosing_funcion()
    enclosing()

    print("\n")

    sum_list("a", "b")
    sum_list("abc", "cde")

    sum_of_numbers(13,42)
    sum_of_numbers(13,42)
    sum_of_numbers(13,42)

if __name__ == '__main__':
    main()
