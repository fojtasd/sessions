def calc(a, b, operator):
    a = int(a)
    b = int(b)
    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '/':
        result = a / b
    elif operator == '*':
        result = a * b
    else:
        raise RuntimeError("Chyba")
    return result
