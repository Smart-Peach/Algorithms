def maximum(data):
    """Returns maximum length in the list"""
    data = [str(y) for y in data]
    m = len(max(data, key=lambda x: len(x)))
    return m


def separator(s):
    print("|", end="")
    print("-" * s, end="")
    print("|")


def format_table(benchmarks, algos, results):
    print()
    benchmarks.insert(0, "Benchmark")
    algos.insert(0, "Benchmark")
    m = {}

    # Раскидываем данные по колонкам и ищем ширину каждого столбца
    columns = [benchmarks]
    m[0] = maximum(columns[0])
    for i in range(1, len(algos)):
        columns.append([algos[i]])
        for j in range(len(benchmarks) - 1):
            columns[i].append(results[j][i - 1])
        m[i] = maximum(columns[i])

    s = sum(m.values()) + 4 * len(algos) - 1

    # Первая строчка:
    print("|", end="")
    for i in range(len(algos)):
        print(" ", algos[i].ljust(m[i], " "), "|", end="")
    print()

    separator(s)

    # Остальные строчки:
    for i in range(1, len(benchmarks)):  # строки
        print("|", end="")
        for j in range(len(algos)):  # столбцы
            print(" ", str(columns[j][i]).ljust(m[j], " "), "|", end="")
        print()


# format_table(["b", "t"],
#              ["quick sort", "merge sort pam pam pam", "bubble sort"],
#              [[1.23, 1.56, 2.00000000000001], [3.3, 2.9, 3.9]])
