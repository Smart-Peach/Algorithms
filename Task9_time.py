from Task9 import matrix_multiply_classic
from Task9 import matrix_multiply_8recursions
from Task9 import matrix_multiplication_strassen
from Task9 import make_matrix
from benchmarks import format_table
from time import time
from typing import List


def calculations(time: List):
    standard_deviation = average = 0
    geometric_mean = 1
    length = len(time)

    for i in time:
        average += i
        standard_deviation += i * i
        geometric_mean *= i

    average = average / length
    standard_deviation = (standard_deviation / length - average ** 2) ** 0.5
    geometric_mean = geometric_mean ** (1 / length)

    average = '{0:.5f}'.format(average)
    standard_deviation = '{0:.5f}'.format(standard_deviation)
    geometric_mean = '{0:.5f}'.format(geometric_mean)

    return [average, standard_deviation, geometric_mean]


def measure(func, measure_array, matrix):
    def time_wrapper(func, matrix):
        time_array = []
        for i in range(7):
            start_time = time()
            func(matrix, matrix)
            finish_time = time()
            time_array.append(finish_time - start_time)
        time_array.pop(0)
        return time_array

    calcus = calculations(time_wrapper(func, matrix))
    measure_array.append(calcus)


measurements = []
size = int(input())
matrix = make_matrix(size)

measure(matrix_multiply_classic, measurements, matrix)
measure(matrix_multiply_8recursions, measurements, matrix)
measure(matrix_multiplication_strassen, measurements, matrix)

format_table(['classic', '8 recursions', 'Strassen'], ['sample mean', 'standard deviation', 'geometric mean'],
             measurements)
