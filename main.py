from geopy.distance import geodesic
from sys import maxsize

cd = {
    "Malaysia": (2.745564, 101.707021),
    "Jakarta": (-6.126928, 106.653502),
    "Bangkok": (13.697766, 100.751978),
    "Taipei": (25.081791, 121.237306),
    "Hong Kong": (22.308000, 113.918500),
    "Tokyo": (35.549400, 139.779800),
    "Beijing": (40.079900, 116.603100),
    "Seoul": (37.460200, 126.440700),
}
countries = 8

country = [
    "Malaysia",
    "Jakarta",
    "Bangkok",
    "Taipei",
    "Hong Kong",
    "Tokyo",
    "Beijing",
    "Seoul"
]

# Traveling Salesman Problem: https://www.geeksforgeeks.org/traveling-salesman-problem-tsp-implementation/
# implementation of traveling Salesman Problem
def travellingSalesmanProblem(graph, s):
    # store all vertex apart from source vertex
    vertex = []
    for i in range(countries):
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

        for i in range(len(vertex)):
            current_pathweight += graph[k][vertex[i]]
            k = vertex[i]
            current_route += "->" + country[k]

        current_pathweight += graph[k][s]


        # update minimum
        if current_pathweight<min_path:
            shortest_route = current_route
        min_path = min(min_path, current_pathweight)

        if not next_permutation(vertex):
            break

    return min_path, shortest_route


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


def distance(origin, dest):
    return geodesic(origin, dest).km


graph = [[0]*countries for i in range(10)]
for i in range(countries):
    for j in range(countries):
        graph[i][j] = distance(cd[country[i]], cd[country[j]])

# print(graph)
s = 0
print(
distance(
    cd["Malaysia"], cd["Jakarta"]
) + distance(
    cd["Jakarta"], cd["Bangkok"]
) + distance(
    cd["Bangkok"], cd["Taipei"]
) + distance(
    cd["Taipei"], cd["Hong Kong"]
) + distance(
    cd["Hong Kong"], cd["Tokyo"]
) + distance(
    cd["Tokyo"], cd["Beijing"]
) + distance(
    cd["Beijing"], cd["Seoul"]
) + distance(
    cd["Seoul"], cd["Malaysia"]
)
)
print(travellingSalesmanProblem(graph, s))

# # With Google Distance Matrix API (no flight routes)
# import googlemaps
#
#
# def get_distance(origin, dest):
#     gmaps = googlemaps.Client(key='AIzaSyADPWVyNFbG-E0rpvNF6qnL6XBdIy48L94')
#     distance = gmaps.distance_matrix(origin, dest)["rows"][0]["elements"][0]
#     return distance
#
#
# cd = {
#     "Malaysia": "2.745564,101.707021",
#     "Jakarta": "-6.126928,106.653502",
#     "Bangkok": "13.697766,100.751978",
#     "Taipei": "25.081791,121.237306",
#     "Hong Kong": "22.308000,113.918500",
#     "Tokyo": "35.549400,139.779800",
#     "Beijing": "40.079900,116.603100",
#     "Seoul": "37.460200,126.440700",
# }
# result = get_distance(cd["Malaysia"], cd["Jakarta"])
# print(result['distance']['text'])
