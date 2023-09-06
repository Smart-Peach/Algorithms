class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:

        def check(graph, result):
            return len(graph) == len(result)

        def toposort(graph, amount_befores):
            sources = set()  # Истоки

            for item in range(len(graph)):  # Выбираем истоки
                if not amount_befores[item]:
                    sources.add(item)

            result = []
            while sources:  # Пока есть истоки продолжаем -- ака есть вершниы
                vertex = sources.pop()  # Выбрали рандомную вершину из истоков и удалили
                result.append(vertex)
                if graph[vertex]:  # Если из этой вершины выходили дороги
                    for edge in graph[vertex]:
                        amount_befores[edge] -= 1
                        if not amount_befores[edge]:
                            sources.add(edge)
            return result

        items = [i for i in range(n)]
        groups = [i for i in range(m)]

        # Unique groups for lonely elements
        for item in items:
            if group[item] == -1:
                group[item] = m
                m += 1

        # m - new amount of groups

        items_graph = [[] for _ in range(n)]  # Graph of elements
        groups_graph = [[] for _ in range(m)]  # Graph of groups
        amount_befores_items = [0 for _ in range(n)]
        amount_befores_groups = [0 for _ in range(m)]

        # ITEMS GRAPH
        for item in items:
            if beforeItems[item]:  # if there're predeccessors
                # print(item)
                for edge in beforeItems[item]:
                    # print('edge:', edge)
                    items_graph[edge].append(item)
                amount_befores_items[item] = len(beforeItems[item])

        # GROUPS GRAPH
        for item in items:
            item_group = group[item]
            if beforeItems[item]:  # If it has predeccessors
                for edge in beforeItems[item]:
                    previous_group = group[edge]
                    if previous_group != item_group:
                        groups_graph[previous_group].append(item_group)
                        amount_befores_groups[item_group] += 1

        sorted_items = toposort(items_graph, amount_befores_items)
        if not check(sorted_items, items_graph):
            return []

        sorted_groups = toposort(groups_graph, amount_befores_groups)
        if not check(sorted_groups, groups_graph):
            return []

        # Словарь групп, с отсортированными элементами
        group_dict = {}
        for item in sorted_items:
            exact_group = group[item]
            if exact_group in group_dict:
                group_dict[exact_group].append(item)
            else:
                group_dict[exact_group] = [item]

        result = []
        for group in sorted_groups:
            if group in group_dict:
                result += group_dict[group]
        return result
