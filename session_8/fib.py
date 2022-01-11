from typing import Generator


def fibonacci() -> Generator[int, None, None]:
    a = 0
    b = 1
    yield a
    yield b
    while True:
        fib = a + b
        yield fib
        a = b
        b = fib
