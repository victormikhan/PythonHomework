a = "I am global variable!"


def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():

        global a  # or 'nonlocal a' for enclosed scope
        print(a)

    return inner_function

