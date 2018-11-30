#Author: Michael Royal
#Function: Access Google Maps for traffic information
#Status: Working/Tested

from geolocation.main import GoogleMaps
from geolocation.distance_matrix.client import DistanceMatrixApiClient

def dist():
    origin = ['Santa Cruz']
    destination = ['Seaside']
    duration = []

    google_maps = GoogleMaps(api_key='AIzaSyBTfMBsYy9fFaJ-XVhoHIz-VnKiN2DZGpg')

    items = google_maps.distance(origin, destination).all()

    for item in items:
        duration.append('Start: ' + origin[0] + '\n' + 'Destination: ' + destination[0] + '\n' + 'Travel time: %s' % item.duration)

    return duration
