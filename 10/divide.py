def positive_divide(numerator, denominator):
    if denominator == 0:
        return 0

    result = numerator / denominator

    if result < 0:
        raise ValueError("Result must not be negative")

    return result
