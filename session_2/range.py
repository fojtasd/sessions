from dataclasses import dataclass


@dataclass
class Range:
    min: float
    max: float


def main(input_range: Range, output_range: Range, input_value: float):
    k = (output_range.min - output_range.max) / (input_range.min - input_range.max)
    q = -k * input_range.max + output_range.max

    # input_value == x
    result = k * input_value + q

    # řešení:
    q2 = output_range.min
    k2 = (output_range.max - output_range.min) / (input_range.max - input_range.min)
    x = (input_value - input_range.min)
    result2 = k2 * x + q2

    print(k, k2)
    print(q, q2)
    print(result, result2)
    return result


if __name__ == "__main__":
    main(Range(100, 200), Range(-100, 0), 150)
