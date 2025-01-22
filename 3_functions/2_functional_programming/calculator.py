from typing import Callable

def make_number(value: int) -> Callable[..., int]:
    def wrapper(operation: Callable[[int], int] = None):
        return operation(value) if operation else value
    return wrapper

zero = make_number(0)
one = make_number(1)
two = make_number(2)
three = make_number(3)
four = make_number(4)
five = make_number(5)
six = make_number(6)
seven = make_number(7)
eight = make_number(8)
nine = make_number(9)

def plus(rhs: int) -> Callable[[int], int]:
    return lambda lhs: lhs + rhs

def minus(rhs: int) -> Callable[[int], int]:
    return lambda lhs: lhs - rhs

def times(rhs: int) -> Callable[[int], int]:
    return lambda lhs: lhs * rhs

def divided_by(rhs: int) -> Callable[[int], int]:
    return lambda lhs: lhs // rhs if rhs != 0 else None