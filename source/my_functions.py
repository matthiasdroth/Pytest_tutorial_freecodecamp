def add(number_one, number_two):
    return number_one + number_two

def divide(number_one, number_two):
    if number_two==0:
        raise ZeroDivisionError
    return number_one / number_two