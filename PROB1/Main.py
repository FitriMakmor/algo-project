from gmplot import gmplot
import webbrowser
import os

# Place map
gmap = gmplot.GoogleMapPlotter(18.496610, 115.147213, 4, "AIzaSyADPWVyNFbG-E0rpvNF6qnL6XBdIy48L94")

# Marker

# Malaysia Negara Tercinta uhuk
mas_lan, mas_lon = 2.745564, 101.707021
gmap.marker(mas_lan, mas_lon, "cornflowerblue")

# Indonesia
indo_lan, indo_lon = -6.126928,106.653502
gmap.marker(indo_lan, indo_lon, "cornflowerblue")

# Thailand
thai_lan, thai_lon = 13.697766,100.751978
gmap.marker(thai_lan, thai_lon, "cornflowerblue")

# Taipei
tpei_lan, tpei_lon = 25.081791,121.237306
gmap.marker(tpei_lan, tpei_lon, "cornflowerblue")

# Hong Kong
hk_lan, hk_lon = 22.308000,113.918500
gmap.marker(hk_lan, hk_lon, "cornflowerblue")

# Japan
jap_lan, jap_lon = 35.549400,139.779800
gmap.marker(jap_lan, jap_lon, "cornflowerblue")

# Beijing
bei_lan, bei_lon = 40.079900,116.603100
gmap.marker(bei_lan, bei_lon, "cornflowerblue")

# Korea
kor_lan, kor_lon = 37.460200,126.440700
gmap.marker(kor_lan, kor_lon, "cornflowerblue")

# Draw
gmap.draw("my_map.html")

print(os.getcwd())

# open in a new tab, if possible
new = 2

# open an HTML file on my own (Windows) computer
url = os.getcwd()+"\my_map.html"
webbrowser.open(url,new=new)


# Polyline
gmap1 = gmplot.GoogleMapPlotter(18.496610, 115.147213, 4, "AIzaSyD803CsvDwLLM-f2exIrQdC1e_M1d7nnYg")

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
gmap1.scatter(top_attraction_lats, top_attraction_lons,'# FF0000', size = 40, marker = False )
gmap1.plot(top_attraction_lats, top_attraction_lons,'cornflowerblue', edge_width = 2.5)


gmap1.draw("my_mapPolyline.html")

print(os.getcwd())

# open in a new tab, if possible
new1 = 2

# open an HTML file on my own (Windows) computer
url1 = os.getcwd()+"\my_mapPolyline.html"
webbrowser.open(url1,new=new1)