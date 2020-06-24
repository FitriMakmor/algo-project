from gmplot import gmplot
import webbrowser
import os
from geopy.distance import geodesic
from Problem1.tsp2 import tsp2
from Problem3.textRoute import textRoute
from Problem3.heapSort import heapSort
import platform
import itertools
import sys


def distance(origin, dest):
    return geodesic(origin, dest).km


def total_distance(city_route):
    sum_dist = 0
    for i in range(len(country)-1):
        sum_dist = sum_dist + city_distance[country.index(city_route[i])][country.index(city_route[i+1])]
    return sum_dist


def get_dict_key(val, dict):
    for key, value in dict.items():
        if val == value:
            return key

    return "key doesn't exist"


def route_score(city_route, tot_distance, highest, lowest):
    no_of_edges = len(country)-1
    middle = (highest+lowest)/2
    # Route scoring is subjective, hence the existence of constants
    A = 2
    B = 0.5
    sum_score = 0
    for i in range(len(country)):
        sum_score = sum_score + (A * (econ[city_route[i]]) * (no_of_edges-i))
    sum_score = sum_score + (B * ((middle/tot_distance) * no_of_edges))
    return sum_score


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


city_distance = [[0]*countries for i in range(countries)]
for i in range(countries):
    for j in range(countries):
        city_distance[i][j] = distance(cd[country[i]], cd[country[j]])

# change tsp2 to tsp if traveller returns to starting country
city_c = 0
planned_route = tsp2(city_distance, 0, country)
route = planned_route.get_route()

# # Uncomment the code below to view the distance matrix between the 8 countries (8 X 8)
print(city_distance)


econ = {
    "Malaysia": 0.99,
    "Beijing": 0.0,
    "Hong Kong": 0.0,
    "Jakarta": 0.0,
    "Tokyo": 0.0,
    "Seoul": 0.0,
    "Taipei": 0.0,
    "Bangkok": 0.0
}

cities = ["Beijing", "Hong Kong", "Jakarta", "Tokyo", "Seoul", "Taipei", "Bangkok"]

pos_url, neg_url = "", ""
os_type = platform.system()
if os_type == "Windows":
    econ_url = os.path.normpath(os.getcwd() + os.sep + os.pardir)+"\\Problem2\\econs.txt"
elif os_type == "Linux" or "Max":
    econ_url = os.path.normpath(os.getcwd() + os.sep + os.pardir)+"/Problem2/econs.txt"

econs_file = open(econ_url, "r")

economic = econs_file.read().split()
economic = economic[1:]

i=0
while i<len(cities):
    val = float(economic[i])
    percent = "{:.2f}".format(val)
    f = float(percent)
    cur_city = cities[i]
    econ.update({cur_city : f})
    i += 1

# # comment/uncomment the code below to view the economic score of each country
print(econ)

val_list = list(econ.values())
val_list.sort(reverse=True)
best_econ_route = []
for i in range(countries):
    best_econ_route.append(get_dict_key(val_list[i], econ))


# Getting the optimised route from the previous shortest distance route
potential_city = route.copy()
new_route = [potential_city.pop(0)]
city_b = 0
city_check = 1


# city_c: current starting city to compare distance
# city_b: current "best" city to be the next destination
# city_check: city being checked with candidate city ("best" city) as suitable replacement

for h in range (len(potential_city)-1):
    while city_check < len(potential_city):
        if city_check != city_b and econ[potential_city[city_b]]+.02 < econ[potential_city[city_check]] and city_distance[city_c][country.index(potential_city[city_b])]*1.4 >= city_distance[city_c][country.index(potential_city[city_check])]:
            city_b = city_check
            city_check = -1
        city_check += 1
    city_c = country.index(potential_city[city_b])
    new_route.append(potential_city.pop(city_b))
    city_b = 0
    city_check = 1
new_route.append(potential_city.pop(0))

print("New route with given parameters:", new_route)
print("Total distance: ", total_distance(new_route))


max = -sys.maxsize
min = sys.maxsize

# ---------------Generate all possible routes and append to routes.txt----------------
possible_routes = list(itertools.permutations(country[1:]))
f = open("routes.txt", "w")
for i in range(len(possible_routes)):
    modified_possible_route = list(possible_routes[i])
    modified_possible_route.insert(0, "Malaysia")
    tot_dist = total_distance(modified_possible_route)
    if tot_dist > max:
        max = tot_dist
    if tot_dist < min:
        min = tot_dist

    f.writelines("Route %4d          -> %s\n" % (i+1, str(modified_possible_route)))
    f.writelines("Total distance (km) -> %s\n" % tot_dist)
    route_econ = []
    for j in range (countries):
        route_econ.append(econ[modified_possible_route[j]])
    f.writelines("Economy score       -> %s\n\n" % route_econ)

print("\nMax Distance: ", max, "\nMin Distance: ", min)
f.close()
# ------------------------------------------------------------------------------------


# ---------------Generate all routes WITH SCORE and append to scored_routes.txt-----
f = open("scored_routes.txt", "w")
for i in range(len(possible_routes)):
    modified_possible_route = list(possible_routes[i])
    modified_possible_route.insert(0, "Malaysia")
    tot_dist = total_distance(modified_possible_route)

    f.writelines("Route %4d          -> %s\n" % (i+1, str(modified_possible_route)))
    f.writelines("Total distance (km) -> %s\n" % tot_dist)
    route_econ = []
    for j in range(countries):
        route_econ.append(econ[modified_possible_route[j]])
    f.writelines("Economy score       -> %s\n" % route_econ)
    rte_score = route_score(modified_possible_route, tot_dist, max, min)
    f.writelines("Route score         -> %s\n\n" % rte_score)
f.close()
# ------------------------------------------------------------------------------------

f = open("scored_routes.txt")
lines = f.readlines()
routes = []

for i in range(len(lines)//5):
    content = ""
    score = 0
    for j in range(5):
        content += str(lines[j + 5 * i])
    score = float(lines[3+5*i].split("Route score         -> ", 1)[1].strip("\n"))
    routes.append(textRoute(content, score))
f.close()

# Sort the routes using Heap Sort Algorithm
heapSort(routes)

# # ----------------Inserted the newly sorted routes into sorted_routes.txt-------------
f = open("sorted_routes.txt", "w")
for i in range(len(lines)//5):
    f.writelines("Ranking             -> %4d\n" % (i+1))
    f.writelines(routes[i].content)
f.close()
# # ------------------------------------------------------------------------------------

# -------------Masukkan Data shortest route ke dalam text file----------------------
f = open("compare_three_routes.txt", "w")
f.writelines("Route Shrt          -> %s\n" % str(route))
f.writelines("Total distance (km) -> %s\n" % total_distance(route))
route_econ = []
for i in range (countries):
    route_econ.append(econ[route[i]])
f.writelines("Economy score       -> %s\n\n" % route_econ)
# # -----------------------------------------------------------------------------------

# # -------------Masukkan Data best econ route ke dalam text file----------------------

f.writelines("Route Econ          -> %s\n" % str(best_econ_route))
f.writelines("Total distance (km) -> %s\n" % total_distance(best_econ_route))
route_econ = []
for i in range (countries):
    route_econ.append(econ[best_econ_route[i]])
f.writelines("Economy score       -> %s\n\n" % route_econ)
# # -----------------------------------------------------------------------------------

# # -------------Masukkan optimised route ke dalam text file----------------------

f.writelines("Route Opti          -> %s\n" % str(new_route))
f.writelines("Total distance (km) -> %s\n" % total_distance(new_route))
route_econ = []
for i in range (countries):
    route_econ.append(econ[new_route[i]])
f.writelines("Economy score       -> %s\n\n" % route_econ)
f.close()
# # -----------------------------------------------------------------------------------


# # ------------------View best_econ_route through Google Map API--------------------
# # Polyline
# gmap1 = gmplot.GoogleMapPlotter(18.496610, 115.147213, 4, "AIzaSyD803CsvDwLLM-f2exIrQdC1e_M1d7nnYg")
#
# route_lats, route_lons = [], []
# for i in range(countries):
#     route_lats.append(cd[best_econ_route[i]][0])
#     route_lons.append(cd[best_econ_route[i]][1])
#
# gmap1.plot(route_lats, route_lons,'darkorchid', edge_width = 4.5)
#
# gmap1.draw("mapPolyline.html")
#
# # open the HTML file in a web browser
# url1 = os.getcwd()+"\mapPolyline.html"
# webbrowser.open(url1, new=2)
# # -----------------------------------------------------------------------

# # ------------------View optimised route through Google Map API-----------
# # Polyline
# gmap1 = gmplot.GoogleMapPlotter(18.496610, 115.147213, 4, "AIzaSyD803CsvDwLLM-f2exIrQdC1e_M1d7nnYg")
#
# route_lats, route_lons = [], []
# for i in range(countries):
#     route_lats.append(cd[new_route[i]][0])
#     route_lons.append(cd[new_route[i]][1])
#
# gmap1.plot(route_lats, route_lons,'darkorchid', edge_width = 4.5)
#
# gmap1.draw("mapPolyline.html")
#
# # open the HTML file in a web browser
# url1 = os.getcwd()+"\mapPolyline.html"
# webbrowser.open(url1, new=2)
# # -----------------------------------------------------------------------

# ------------------View BEST route through Google Map API--------------------
best_route = ["Malaysia","Taipei","Seoul","Tokyo","Beijing","Hong Kong","Bangkok","Jakarta"]
gmap1 = gmplot.GoogleMapPlotter(18.496610, 115.147213, 4, "AIzaSyD803CsvDwLLM-f2exIrQdC1e_M1d7nnYg")

route_lats, route_lons = [], []
for i in range(countries):
    route_lats.append(cd[best_route[i]][0])
    route_lons.append(cd[best_route[i]][1])

gmap1.plot(route_lats, route_lons,'darkorchid', edge_width = 4.5)

gmap1.draw("mapPolyline.html")

# open the HTML file in a web browser
url1 = os.getcwd()+"\mapPolyline.html"
webbrowser.open(url1, new=2)
# -----------------------------------------------------------------------
