def divide(a: float, b: float) -> float:
    return a / b

def test_division(label: str, a: float, b: float, expected_output: float) -> None:
    actual_output = divide(a, b)
    if actual_output != expected_output:
        print(f"{label}: FAIL!!!")
    else:
        print(f"{label}: PASS")

def main() -> None:
    test_division("deset děleno pěti je dva", 10, 5, 2)
    test_division("42 děleno 2 je 21", 42, 2, 21)
    test_division("test který neprojde", 10, 1, 123456789)

if __name__ == "__main__":
    main()
