class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Initialization~
        # A = [[0, 0]]  # Take a random vert (it doesn't matter, so take 0'st)
        inf = float('inf')
        vert_dict = {}
        # for i in range(1, n):
        #     A.append([i, inf])
        for edge in edges:
            from_, to_, weight = edge
            if from_ in vert_dict:
                vert_dict[from_].append([to_, weight])
            else:
                vert_dict[from_] = [[to_, weight]]
            if to_ in vert_dict:
                vert_dict[to_].append([from_, weight])
            else:
                vert_dict[to_] = [[from_, weight]]

        A = list()
        for i in range(n):
            A.append([])
            for j in range(n):
                A[i].append(inf)

        for i in range(n):
            A[i][i] = 0
        print(A)
        # Filling the array~

        for i in range(1, n):
            for v in vert_dict.keys():
                # m = inf
                for w, weight in vert_dict[v]:
                    if A[w][i - 1] + weight < A[v][i]:
                        # m = A[w][i - 1] + weight
                        A[v][i] = A[w][i - 1] + weight

        cnt = 0
        minN = inf
        res = 0
        for i in range(n):
            for j in range(n):
                if i != j and A[i][j] <= distanceThreshold:
                    cnt += 1
            if minN >= cnt:
                minN, res = cnt, i

        print(A)
        return res
