class UnionFind:
    def __init__(self, vertex_amount):
        self.vertex_amount = vertex_amount
        self.classes_amount = vertex_amount

        self.position = []  # indexes --> deadlines
        for i in range(vertex_amount):
            self.position.append(i)

    def find(self, vert: int) -> int:
        """Returns the equivalence class (~parent) of vertex"""

        while self.position[vert] != vert:
            vert = self.position[vert]

        return vert

    def union(self, vert1: int, vert2: int) -> None:
        """Merges vertex equivalence classes"""
        self.classes_amount -= 1

        eq_class1 = self.find(vert1)  # int
        eq_class2 = self.find(vert2)  # int

        left_class = min(eq_class1, eq_class2, key=lambda x: self.position[x])
        right_class = max(eq_class2, eq_class1, key=lambda x: self.position[x])

        self.position[right_class] = left_class


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
            deadline = tasks_complete.find(deadline) - 1  # Find the most left free day
            if deadline < 0:  # If we ruined the deadline --> we get fine
                total_fine += fine
                deadline = tasks_complete.find(tasks_amount - 1)  # Another equivalence class (at the end)
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
