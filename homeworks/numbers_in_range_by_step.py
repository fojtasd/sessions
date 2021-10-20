import sys


def numbers_in_range_by_step(a: float, b: float, step: float):
    while a < b:
        a = a + step
        print(a)


def numbers_in_range_by_amount_of_steps(a: float, b: float, amount_of_steps: float):
    range = b - a
    step_size = range / amount_of_steps
    while a < b:
        a = a + step_size
        print(a)


def main():
    numbers_in_range_by_step(0, 5, 0.1)
    numbers_in_range_by_amount_of_steps(0, 10, 1)


if __name__ == "__main__":
    main()
