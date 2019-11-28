from session_2 import *


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


if __name__ == '__main__':
    main()
