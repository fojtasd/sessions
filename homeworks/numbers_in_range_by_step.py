def numbers_in_range_by_step(a: int, b: int, step: int):
    while a <= b:
        a = a + step
        print(a)

def numbers_in_range_by_amount_of_steps(a: int, b: int, amount_of_steps: int):
    range = b - a
    step_size = b / amount_of_steps
    while a <= b:
        a = a + step_size
        print(a)


def main():
    numbers_in_range_by_step()


if __name__ == "__main__":
    main()
