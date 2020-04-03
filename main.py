from geopy.distance import geodesic
from tsp import tsp
from tsp2 import tsp2

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


def distance(origin, dest):
    return geodesic(origin, dest).km


graph = [[0]*countries for i in range(countries)]
for i in range(countries):
    for j in range(countries):
        graph[i][j] = distance(cd[country[i]], cd[country[j]])

# print(graph)
s = 0
print()
# print(
# distance(
#     cd["Malaysia"], cd["Jakarta"]
# ) + distance(
#     cd["Jakarta"], cd["Bangkok"]
# ) + distance(
#     cd["Bangkok"], cd["Taipei"]
# ) + distance(
#     cd["Taipei"], cd["Hong Kong"]
# ) + distance(
#     cd["Hong Kong"], cd["Tokyo"]
# ) + distance(
#     cd["Tokyo"], cd["Beijing"]
# ) + distance(
#     cd["Beijing"], cd["Seoul"]
# ) + distance(
#     cd["Seoul"], cd["Malaysia"]
# )
# )

# tsp(graph, s, country)
# tsp2(graph, s, country)

no_return = tsp2(graph, s, country)
route = no_return.get_route()
print(route)
#
# print()
#
# with_return = tsp(graph, s, country)
# route = with_return.get_route()
# print(route)








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
