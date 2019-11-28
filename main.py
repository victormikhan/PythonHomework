from session_2 import *
from session_3 import *


def main():

    """session 2"""
    print(quote_replacement('replaced quote \' \" '))
    print(palindrome_checker('Able was I ere I saw Elba'))
    print(custom_str_split('Able was I ere I saw Elba', separator=' '))
    print(split_by_index('pythoniscool,isn\'tit?', [6,8,12,13,18]))
    print(get_digits(12125231523456789))
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



if __name__ == '__main__':
    main()
