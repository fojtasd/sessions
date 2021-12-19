import sys
from typing import Generator


def my_generator(end: int) -> Generator[int, None, None]:
    start = 0
    while start < end:
        yield start
        start += 1


def fibonacci() -> Generator[int, None, None]:
    yield 0
    yield 1
    yield 1
    first_value = 1
    second_value = 1
    while True:
        third_value = first_value + second_value
        yield third_value
        first_value = second_value
        second_value = third_value


def main():
    """
    my_range = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(sys.getsizeof(my_range))
    for n in my_range:
        print(n)

    my_range = my_generator(10)
    print(sys.getsizeof(my_range))
    for n in my_range:
        print(n)
    """

    for n in fibonacci():
        print(n)
        if n > 100:
            break


if __name__ == "__main__":
    main()
