class FreqStack:

    def __init__(self):
        self.counter = {}  # Counter of repeats for each element (key: element, value: repeats)
        self.repeats = {}  # Dict of elements with the same frequancy (key: repeats, value: list of elements)

    def push(self, val: int) -> None:
        if not val in self.counter:
            self.counter[val] = 1
        else:
            self.counter[val] += 1

        if not self.counter[val] in self.repeats:
            self.repeats[self.counter[val]] = [val]
        else:
            self.repeats[self.counter[val]].append(val)

    def pop(self) -> int:
        frequency = max(self.repeats.keys())  # The biggest amount of repeats
        suitable_element = self.repeats[frequency].pop()

        if not self.repeats[frequency]:
            self.repeats.pop(frequency)

        self.counter[suitable_element] -= 1
        return suitable_element