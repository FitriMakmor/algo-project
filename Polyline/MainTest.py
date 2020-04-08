from gmplot import gmplot
import webbrowser
import os

# Place map
gmap = gmplot.GoogleMapPlotter(18.496610, 115.147213, 4, "AIzaSyD803CsvDwLLM-f2exIrQdC1e_M1d7nnYg")

latitude, longtitude = zip(*[
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
gmap.scatter(latitude, longtitude,'# FF0000', size = 50, marker = False )
gmap.plot(latitude, longtitude,'darkorchid', edge_width = 4.5)


gmap.draw("Polyline.html")

print(os.getcwd())

# open in a new tab, if possible
new = 2

# open an HTML file on my own (Windows) computer
url = os.getcwd()+"\Polyline.html"
webbrowser.open(url,new=new)
