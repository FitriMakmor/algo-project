from gmplot import gmplot

# Place map
gmap = gmplot.GoogleMapPlotter(37.766956, -122.438481, 13, "AIzaSyADPWVyNFbG-E0rpvNF6qnL6XBdIy48L94")

# Polygon
ben_travel, ben_sampai = zip(*[
    (2.745564,101.707021),
    (-6.126928,106.653502),
    (13.697766,100.751978),
    (13.697766,100.751978),
    (25.081791,121.237306),
    (22.308000,113.918500),
    (35.549400,139.779800),
    (40.079900,116.603100),
    (37.460200,126.440700),
    ])
gmap.plot(ben_travel, ben_sampai, 'cornflowerblue', edge_width=10)

# Scatter points
top_attraction_lats, top_attraction_lons = zip(*[
    (37.769901, -122.498331),
    (37.768645, -122.475328),
    (37.771478, -122.468677),
    (37.769867, -122.466102),
    (37.767187, -122.467496),
    (37.770104, -122.470436)
    ])
gmap.scatter(top_attraction_lats, top_attraction_lons, '#3B0B39', size=40, marker=False)

# Marker
hidden_gem_lat, hidden_gem_lon = 37.770776, -122.461689
gmap.marker(hidden_gem_lat, hidden_gem_lon, 'cornflowerblue')

# Draw
gmap.draw("my_map.html")