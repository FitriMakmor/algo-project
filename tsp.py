from sys import maxsize


class tsp():
    # Ref link untuk Traveling Salesman Problem:
    # https://www.geeksforgeeks.org/traveling-salesman-problem-tsp-implementation/
    # implementation of traveling Salesman Problem
    def __init__(self, graph, s, country):
        # store all vertex apart from source vertex
        self.route = [s]
        vertex = []
        for i in range(len(graph)):
            if i != s:
                vertex.append(i)

                # store minimum weight Hamiltonian Cycle
        min_path = maxsize

        while True:

            # store current Path weight(cost)
            current_pathweight = 0

            # compute current path weight
            k = s
            current_route = country[s]
            test_route = [country[s]]

            for i in range(len(vertex)):
                current_pathweight += graph[k][vertex[i]]
                k = vertex[i]
                current_route += "->" + country[k]
                test_route.append(country[k])

            current_pathweight += graph[k][s]

            # update minimum
            if current_pathweight < min_path:
                shortest_route = current_route
                self.route = test_route
            min_path = min(min_path, current_pathweight)

            if not next_permutation(vertex):
                break

        print("Distance:", min_path, "\nRoute:", shortest_route,"\n")

        return None

    def get_route(self):
        return self.route


# next_permutation implementation
def next_permutation(L):
    n = len(L)

    i = n - 2
    while i >= 0 and L[i] >= L[i + 1]:
        i -= 1

    if i == -1:
        return False

    j = i + 1
    while j < n and L[j] > L[i]:
        j += 1
    j -= 1

    L[i], L[j] = L[j], L[i]

    left = i + 1
    right = n - 1

    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

    return True
