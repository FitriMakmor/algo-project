

from gmplot import gmplot
import webbrowser
import os
from geopy.distance import geodesic
from Problem3.tsp import tsp
from Problem3.tsp2 import tsp2

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

# Klu nak bandingkan distance antara dua country, boleh uncommment pastu refer list print(city_distance) bawah ni
# print(city_distance)


# economy ni untuk digantikan dgn data prob2 yang bebeno
econ = {
    "Malaysia": 0.99,
    "Jakarta": 0.0,
    "Bangkok": 0.0,
    "Taipei": 0.0,
    "Hong Kong": 0.0,
    "Tokyo": 0.0,
    "Beijing": 0.0,
    "Seoul": 0.0
}

cities = ["Bangkok", "Seoul", "Beijing", "Tokyo", "Hong Kong", "Jakarta", "Taipei"]

countpos = open("/Users/safi/PycharmProjects/MasterGit/Problem2/countpos.txt", "r")
countneg = open("/Users/safi/PycharmProjects/MasterGit/Problem2/countneg.txt", "r")
Parray = countpos.read().split()
Narray = countneg.read().split()
Parray = [int(i) for i in Parray]
Narray = [int(i) for i in Narray]
print(Parray, Narray)


for i in range(len(Parray)):
    Pnum = Parray[i]
    Nnum = Narray[i]
    percent = ((Pnum)/(Pnum+Nnum))
    percent = "{:.2f}".format(percent)
    f = float(percent)
    cur_city = cities[i]
    econ.update({cur_city : f})
    i += 1

print(econ)

# Bawah ni untuk soalan Problem 3 gunakan parameter yang dia bagi
potential_city = route.copy()
new_route = [potential_city.pop(0)]
city_b = 0
city_check = 1


# city_c: current starting city to compare distance
# city_b: current "best" city to be the next destination
# city_check: city being checked with candidate city as suitable replacement

for h in range (len(potential_city)-1):
    while city_check < len(potential_city):
        if city_check != city_b and econ[potential_city[city_b]]+.02 < econ[potential_city[city_check]] and city_distance[city_c][country.index(potential_city[city_b])] >= city_distance[city_c][country.index(potential_city[city_check])] - 800:
            city_b = city_check
            city_check = -1
        city_check += 1
    city_c = country.index(potential_city[city_b])
    new_route.append(potential_city.pop(city_b))
    city_b = 0
    city_check = 1
new_route.append(potential_city.pop(0))

print("New route:", new_route)

# Bawah ni utk tengok google map output.
# Boleh comment code bawah ni klu nak tengok output dekat console je
# Polyline
gmap1 = gmplot.GoogleMapPlotter(18.496610, 115.147213, 4, "AIzaSyD803CsvDwLLM-f2exIrQdC1e_M1d7nnYg")

route_lats, route_lons = [], []
for i in range(countries):
    route_lats.append(cd[new_route[i]][0])
    route_lons.append(cd[new_route[i]][1])

gmap1.plot(route_lats, route_lons,'darkorchid', edge_width = 4.5)

gmap1.draw("mapPolyline.html")

# open the HTML file in a web browser
url1 = os.getcwd()+"\mapPolyline.html"
webbrowser.open(url1, new=2)