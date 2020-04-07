from gmplot import gmplot
import webbrowser
import os

# Place map
gmap = gmplot.GoogleMapPlotter(18.496610, 115.147213, 4, "AIzaSyADPWVyNFbG-E0rpvNF6qnL6XBdIy48L94")

# Polygon
# ben_travel, ben_sampai = zip(*[
#     (2.745564,101.707021),
#     (-6.126928,106.653502),
#     (13.697766,100.751978),
#     (13.697766,100.751978),
#     (25.081791,121.237306),
#     (22.308000,113.918500),
#     (35.549400,139.779800),
#     (40.079900,116.603100),
#     (37.460200,126.440700),
#     ])
# gmap.plot(ben_travel, ben_sampai, 'cornflowerblue', edge_width=10)

# Scatter points
top_attraction_lats, top_attraction_lons = zip(*[
    (2.745564, 101.707021),
    (-6.126928, 106.653502),
    (13.697766, 100.751978),
    (13.697766, 100.751978),
    (25.081791, 121.237306),
    (22.308000, 113.918500),
    (35.549400, 139.779800),
    (40.079900, 116.603100),
    (37.460200, 126.440700),
    ])
gmap.scatter(top_attraction_lats, top_attraction_lons, '#3B0B39', size=40, marker=False)

# Marker
klia_lan, klia_lon = 2.745564,101.707021
gmap.marker(klia_lan, klia_lon, 'cornflowerblue')

# Testing tengok kalau line ni wujud x selepas pull
# Tambah lagi nak test

# Draw
gmap.draw("my_map.html")

print(os.getcwd())

# open in a new tab, if possible
new = 2

# open an HTML file on my own (Windows) computer
url = os.getcwd()+"\my_map.html"
webbrowser.open(url,new=new)

