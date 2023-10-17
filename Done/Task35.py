class UnionFind:
    def __init__(self, vertex_amount):
        self.vertex_amount = vertex_amount
        self.classes_amount = vertex_amount
        self.equivalence_class = []
        self.rank = []
        self.left_item = []
        for i in range(vertex_amount):
            self.equivalence_class.append(i)  # In the beginning all vertexes' eq. classes are themselves
            self.rank.append(0)
            self.left_item.append(i)

    def find(self, vert: int) -> int:
        """Returns the equivalence class (~parent) of vertex"""

        if self.equivalence_class[vert] != vert:
            self.equivalence_class[vert] = self.find(self.equivalence_class[vert])

        return self.equivalence_class[vert]

    def union(self, vert1: int, vert2: int) -> None:
        """Merges vertex equivalence classes"""
        self.classes_amount -= 1

        eq_class1 = self.find(vert1)  # int
        eq_class2 = self.find(vert2)  # int

        bigger_class = max(eq_class1, eq_class2, key=lambda x: self.rank[x])
        smaller_class = min(eq_class2, eq_class1, key=lambda x: self.rank[x])

        if self.rank[bigger_class] == self.rank[smaller_class]:
            self.rank[bigger_class] += 1

        self.equivalence_class[smaller_class] = bigger_class

        leftest_item = min(eq_class2, eq_class1, key=lambda x: self.left_item[x])

        self.left_item[bigger_class] = leftest_item


def greedy(tasks: list[list]) -> (int, int):
    tasks.sort(key=lambda x: x[2], reverse=True)  # Sort tasks array by fine

    result = []
    total_fine = 0

    for task, deadline, fine in tasks:
        result.append(task)
        if deadline < len(result):
            total_fine += fine

    return total_fine


def make_plan(tasks: list[list]) -> (int, int):
    """Returns amount of equivalent classes (minimum number of access points)
     and the shortest path (minimum network cable distance)"""

    tasks.sort(key=lambda x: x[2], reverse=True)  # Sort tasks array by fine
    tasks_amount = len(tasks)
    tasks_complete = UnionFind(tasks_amount)

    result = []
    for _ in range(tasks_amount):
        result.append(0)
    total_fine = 0

    for task, deadline, fine in tasks:
        deadline -= 1  # Deadlines = index + 1

        if result[deadline]:
            eq_class = tasks_complete.find(deadline)  # Find the most left free day
            deadline = tasks_complete.left_item[eq_class] - 1
            if deadline < 0:  # If we ruined the deadline --> we get fine
                total_fine += fine
                eq_class = tasks_complete.find(tasks_amount - 1)
                deadline = tasks_complete.left_item[eq_class]  # Another equivalence class (at the end)
                if result[deadline]:
                    deadline -= 1

        result[deadline] = task  # Put task on a free day
        if deadline - 1 >= 0 and result[deadline - 1] and tasks_complete.find(deadline) != tasks_complete.find(
                deadline - 1):
            tasks_complete.union(deadline - 1, deadline)

        if deadline + 1 < tasks_amount and result[deadline + 1] and tasks_complete.find(
                deadline) != tasks_complete.find(deadline + 1):
            tasks_complete.union(deadline + 1, deadline)

    return result, total_fine
