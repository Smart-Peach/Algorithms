class UnionFind:
    def __init__(self, vertex_amount):
        self.vertex_amount = vertex_amount
        self.classes_amount = vertex_amount
        # self.equivalence_class = []
        self.position = []  # indexes --> deadlines
        for i in range(vertex_amount):
            # self.equivalence_class.append(i)  # In the beginning all vertexes' eq. classes are themselves
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

        # if self.rank[eq_class1] == self.rank[eq_class2]:
        #     self.rank[eq_class1] += 1
        #     self.rank[eq_class2] += 1

        self.position[right_class] = left_class


def kraskala(tasks: list[list]) -> (int, int):
    """Returns amount of equivalent classes (minimum number of access points)
     and the shortest path (minimum network cable distance)"""

    tasks.sort(key=lambda x: x[2], reverse=True)  # Sort edges array by weight
    print(tasks)
    tasks_amount = len(tasks)
    tasks_complete = UnionFind(tasks_amount)
    result = []
    for _ in range(tasks_amount):
        result.append(0)
    total_fine = 0

    for task, deadline, fine in tasks:
        deadline -= 1
        print('TASK:', task, deadline, fine)
        print('result and days before:', result, tasks_complete.position)

        if not result[deadline]:
            result[deadline] = task  # Put task on her deadline day
            if deadline - 1 >= 0 and result[deadline - 1] and tasks_complete.find(deadline) != tasks_complete.find(
                    deadline - 1):
                tasks_complete.union(deadline - 1, deadline)
            if deadline + 1 < tasks_amount and result[deadline + 1] and tasks_complete.find(
                    deadline) != tasks_complete.find(deadline + 1):
                tasks_complete.union(deadline + 1, deadline)
        else:
            most_left = tasks_complete.find(deadline) - 1
            if most_left < 0:
                total_fine += fine
                most_left = tasks_complete.find(tasks_amount - 1)
                if result[most_left]:
                    most_left -= 1
            result[most_left] = task  # Put task on her deadline day
            if most_left - 1 >= 0 and result[most_left - 1] and tasks_complete.find(most_left) != tasks_complete.find(
                    most_left - 1):
                tasks_complete.union(most_left - 1, most_left)
            if most_left + 1 < tasks_amount and result[most_left + 1] and tasks_complete.find(
                    most_left) != tasks_complete.find(most_left + 1):
                tasks_complete.union(most_left + 1, most_left)
            # if most_left < 0:
            #     total_fine += fine
        print('after:', result, tasks_complete.position)
    return result, total_fine


def solution(tasks: list):
    return kraskala(tasks)


# t = [['A', 5, 60], ['B', 1, 10], ['C', 1, 10], ['D', 1, 10], ['E', 1, 10]]  # [name, deadline, fine]
# t = [[1, 3, 25], [2, 4, 10], [3, 1, 30], [4, 3, 50], [5, 3, 20]]
t = [['A', 5, 60], ['B', 1, 10], ['C', 1, 10], ['D', 1, 10], ['E', 1, 10], ['F', 1, 10]]
print(solution(t))
