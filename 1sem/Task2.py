def right_size(x, y):
    size_x = len(str(x))
    size_y = len(str(y))
    size = max(size_y, size_x)
    if size % 2 != 0:
        size += 1
    return size


def karatsuba(num1, num2):
    # print(num1, num2)
    size = right_size(num1, num2)

    if size <= 2 or not num1 or not num2:
        return num1 * num2
    n = size // 2

    num1_left = num1 // 10 ** n
    num1_right = num1 % 10 ** n
    num2_left = num2 // 10 ** n
    num2_right = num2 % 10 ** n

    step1 = karatsuba(num1_left, num2_left)
    step2 = karatsuba(num1_right, num2_right)
    step3 = karatsuba(num1_left + num1_right, num2_left + num2_right)
    step4 = step3 - step2 - step1

    return step1 * 10 ** size + step2 + step4 * 10 ** (size // 2)
