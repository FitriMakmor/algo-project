from gmplot import gmplot
import webbrowser
import os
from geopy.distance import geodesic
from Problem1.tsp import tsp
from Problem1.tsp2 import tsp2

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
countries = len(cd)

country = [
    "Malaysia",
    "Jakarta",
    "Bangkok",
    "Taipei",
    "Hong Kong",
    "Tokyo",
    "Beijing",
    "Seoul",
]


def distance(origin, dest):
    return geodesic(origin, dest).km


city_distance = [[0]*countries for i in range(countries)]
for i in range(countries):
    for j in range(countries):
        city_distance[i][j] = distance(cd[country[i]], cd[country[j]])

# change tsp2 to tsp if traveller returns
city_c = 0
planned_route = tsp2(city_distance, 0, country)
route = planned_route.get_route()


print(city_distance)


# economy untuk diganti dgn data prob2
economy = [0.53, 0.70, 0.50, 0.49, 0.51, 0.47, 0.52, 0.50]

econ = {
    "Malaysia": 0.53,
    "Jakarta": 0.70,
    "Bangkok": 0.50,
    "Taipei": 0.49,
    "Hong Kong": 0.51,
    "Tokyo": 0.47,
    "Beijing": 0.52,
    "Seoul": 0.50
}

potential_city = route.copy()
new_route = [potential_city.pop(0)]
city_n = 0
city_check = 1

for h in range (len(potential_city)-1):
    while city_check < len(potential_city):
        if city_check != city_n and economy[potential_city[city_n]]+.02 < economy[potential_city[city_check]] and city_distance[city_c][city_n+1]*1.4 >= city_distance[city_c][city_check+1]:
            city_n = city_check
            city_check = -1
        city_check += 1
    new_route.append(potential_city.pop(city_n))
    city_c = city_n
    city_n = 0
new_route.append(potential_city.pop(0))

print(new_route)
