import googlemaps


def get_distance(origin, dest):
    gmaps = googlemaps.Client(key='AIzaSyADPWVyNFbG-E0rpvNF6qnL6XBdIy48L94')
    distance = gmaps.distance_matrix(origin,dest)['rows'][0]['elements'][0]
    return distance


cd = {
    "Malaysia": "2.745564,101.707021",
    "Jakarta": "-6.126928,106.653502",
    "Bangkok": "13.697766,100.751978",
    "Taipei": "25.081791,121.237306",
    "Hong Kong": "22.308000,113.918500",
    "Tokyo": "35.549400,139.779800",
    "Beijing": "40.079900,116.603100",
    "Seoul": "37.460200,126.440700"
}
result = get_distance(cd["Malaysia"], cd["Jakarta"])
print(result['distance']['value'])
