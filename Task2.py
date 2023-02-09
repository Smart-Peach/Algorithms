def right_length(x, y):
    size_x = len(x)
    size_y = len(y)
    if size_y == size_x and size_y % 2 == 0:
        return x, y, size_x
    size = max(size_x, size_y)
    if size_y < size_x:
        y = y.zfill(size)
    else:
        x = x.zfill(size)
    if size % 2 != 0:
        x = x.zfill(size + 1)
        y = y.zfill(size + 1)
        size += 1
    return x, y, size


def karatsuba(num1, num2):
    num1, num2, size = right_length(str(num1), str(num2))

    if size == 2:
        return int(num1) * int(num2)
    n = size // 2

    num1_left = int(num1[:n])
    num1_right = int(num1[n:])
    num2_left = int(num2[:n])
    num2_right = int(num2[n:])

    step1 = karatsuba(num1_left, num2_left)
    step2 = karatsuba(num1_right, num2_right)
    step3 = karatsuba(num1_left + num1_right, num2_left + num2_right)
    step4 = step3 - step2 - step1

    return step1 * 10 ** size + step2 + step4 * 10 ** (size // 2)
