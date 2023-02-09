def find_factor(div, sor):
    """Finds the largest number not greater than div that is divisible by sor"""
    res = sor
    count = 0
    while res <= div:
        res += sor
        count += 1
    res -= sor
    return count, res


def div_column(dividend, n, divisor, m):
    if divisor == 0:
        raise ZeroDivisionError
    result = 0
    if divisor > dividend:
        print(f"Integer part: {result}, remainder of the division: {dividend}")
    else:
        # Неполное частное
        p = n - m  # Количество оставшихся цифр
        intermediary = dividend // 10 ** p
        if intermediary < divisor:
            intermediary = dividend // 10 ** (p - 1)
            p = p - 1

        while p >= 0:
            number, inter = find_factor(intermediary, divisor)
            result = result * 10 + number
            r = intermediary - inter
            if p == 0:
                intermediary = r
            else:
                next_number = (dividend % 10 ** p) // 10 ** (p - 1)
                intermediary = r * 10 + next_number
            p -= 1
        print(f"Integer part: {result}, remainder of the division: {intermediary}")


x = 25657
y = 3791
div_column(x, 5, y, 4)
