from sys import maxsize
import copy

class tsp2():
    # Ref link for Traveling Salesman Problem:
    # https://www.geeksforgeeks.org/traveling-salesman-problem-tsp-implementation/
    # *This code has been heavily edited to fit current problem context
    # implementation of traveling Salesman Problem
    def __init__(self, graph, s, country):
        # store all vertex apart from source vertex
        self.route = [s]
        dummy_graph = copy.deepcopy(graph)
        dummy_country = copy.deepcopy(country)

        for i in range(len(dummy_country)):
            dummy_graph[i].append(0)
            if i == s:
                dummy_graph[i].append(0)
            else:
                dummy_graph[i].append(maxsize)

        dummy_country.append("All")
        dummy_country.append("StartEnd")
        dummy_graph.append([0]*len(dummy_country))
        dummy_graph.append([0])
        for i in range(len(dummy_country)-2):
            dummy_graph[len(dummy_country)-1].append(maxsize)
        dummy_graph[len(dummy_country)-1].append(0)

        vertex = []
        for i in range(len(dummy_graph)):
            if i != s:
                vertex.append(i)

                # store minimum weight Hamiltonian Cycle
        min_path = maxsize

        while True:

            # store current Path weight(cost)
            current_pathweight = 0

            # compute current path weight
            k = s
            current_route = dummy_country[s]
            test_route = [dummy_country[s]]

            for i in range(len(vertex)):
                current_pathweight += dummy_graph[k][vertex[i]]
                k = vertex[i]
                if (dummy_country[k] != "StartEnd") and (dummy_country[k] != "All"):
                    current_route += "->" + dummy_country[k]
                    test_route.append(dummy_country[k])

            current_pathweight += dummy_graph[k][s]

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
