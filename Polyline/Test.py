# import codecs
# import googlemaps
# import webbrowser
# import os
#
# #!/usr/bin/python
# print "<!DOCTYPE html>
# <html>
# <head>
#     <meta name=\"viewport\" content=\"initial-scale=1.0, user-scalable=no\">
#     <meta charset=\"utf-8\">
#     <title>Polylines</title>
#     <style>
#          /* Always set the map height explicitly to define the size of the div
#         * element that contains the map. */
#          #map {
#              height: 100%;
#          }
#          /* Optional: Makes the sample page fill the window. */
#          html, body {
#              height: 100%;
#              margin: 0;
#              padding: 0;
#          }
#     </style>
# </head>
# <body>
#     <div id=\"map\"></div>
#     <h1>My Google Map</h1>
#     <script>
#
#         // This example creates a 2-pixel-wide red polyline showing the path of
#         // the first trans-Pacific flight between Oakland, CA, and Brisbane,
#         // Australia which was made by Charles Kingsford Smith.
#
#         function initMap() {
#             var map = new google.maps.Map(document.getElementById('map'), {
#                 zoom: 5,
#                 center: { lat: 2.745564, lng: 101.707021 },
#                 mapTypeId: 'terrain'
#             });
#
#
#             var flightPlan = [
#
#                 { lat: 2.745564, lng: 101.707021 },
#                 { lat: -6.126928, lng: 106.653502 },
#                 { lat: 13.697766, lng: 100.751978 },
#                 { lat: 25.081791, lng: 121.237306 },
#                 { lat: 22.308000, lng: 113.918500 },
#                 { lat: 35.549400, lng: 139.779800 },
#                 { lat: 40.079900, lng: 116.603100 },
#                 { lat: 37.460200, lng: 126.440700 }
#             ];
#
#             var flightPath = new google.maps.Polyline({
#                 path: flightPlan,
#                 geodesic: true,
#                 strokeColor: '#FF0000',
#                 strokeOpacity: 1.0,
#                 strokeWeight: 2
#             });
#
#             flightPath.setMap(map);
#         }
#     </script>
#     <script async defer
#             src=\"https://maps.googleapis.com/maps/api/js?key=AIzaSyD803CsvDwLLM-f2exIrQdC1e_M1d7nnYg&callback=initMap\">
#     </script>
# </body>
# </html>\n";
#
#
#
#
# #new=2
# #url = "D:\KhairilNajimi\Lecture Notes\SEM4\Algo\python\AssignmentAlgo\Maps.html"
# #webbrowser.open(url,new=new)
#
#
#
# #file = codecs.open("Maps.html", "r", "utf-8")
# #print(file.read())
