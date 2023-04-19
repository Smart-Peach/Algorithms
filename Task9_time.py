from Task9 import matrix_multiply_classic
from Task9 import matrix_multiply_8recursions
from Task9 import matrix_multiplication_strassen
from Task9 import make_matrix
from benchmarks import format_table
from time import time


def calculations(time):
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

    average = '{0:.3f}'.format(average)
    standard_deviation = '{0:.3f}'.format(standard_deviation)
    geometric_mean = '{0:.3f}'.format(geometric_mean)

    return [average, standard_deviation, geometric_mean]


measurements = []
size = int(input())
matrix = make_matrix(size)
time_classic = []
for i in range(3):
    start_time = time()
    a = matrix_multiply_classic(matrix, matrix)
    finish_time = time()
    time_classic.append(finish_time - start_time)
time_classic.pop(0)
measurements.append(calculations(time_classic))

time_8_recursions = []
for i in range(3):
    start_time = time()
    a = matrix_multiply_8recursions(matrix, matrix)
    finish_time = time()
    time_8_recursions.append(finish_time - start_time)
time_8_recursions.pop(0)
measurements.append(calculations(time_8_recursions))

time_strassen = []
for i in range(3):
    start_time = time()
    a = matrix_multiplication_strassen(matrix, matrix)
    finish_time = time()
    time_strassen.append(finish_time - start_time)
time_strassen.pop(0)
measurements.append(calculations(time_strassen))

format_table(['classic', '8 recursions', 'Strassen'], ['sample mean', 'standard deviation', 'geometric mean'],
             measurements)
