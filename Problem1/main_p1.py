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


graph = [[0]*countries for i in range(countries)]
for i in range(countries):
    for j in range(countries):
        graph[i][j] = distance(cd[country[i]], cd[country[j]])

s = 0
print()

# change tsp2 to tsp if traveller returns
planned_route = tsp2(graph, s, country)
route = planned_route.get_route()
print(route)


# # Map Output - Marker Placement and Plotlines
# Place map
gmap = gmplot.GoogleMapPlotter(18.496610, 115.147213, 4, "AIzaSyADPWVyNFbG-E0rpvNF6qnL6XBdIy48L94")

# Marker

for i in range(countries):
    gmap.marker(cd[country[i]][0], cd[country[i]][1], "crimson")

# Draw
gmap.draw("mapMarker.html")

# open in a new tab, if possible
newtab = 2

# open the HTML file in a web browser
url = os.getcwd()+"\mapMarker.html"
webbrowser.open(url, new=newtab)


# Polyline
gmap1 = gmplot.GoogleMapPlotter(18.496610, 115.147213, 4, "AIzaSyD803CsvDwLLM-f2exIrQdC1e_M1d7nnYg")

route_lats, route_lons = [], []
for i in range(countries):
    route_lats.append(cd[route[i]][0])
    route_lons.append(cd[route[i]][1])

gmap1.plot(route_lats, route_lons,'darkorchid', edge_width = 4.5)

gmap1.draw("mapPolyline.html")

# open the HTML file in a web browser
url1 = os.getcwd()+"\mapPolyline.html"
webbrowser.open(url1, new=newtab)