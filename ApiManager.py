import googlemaps
import LocalProperties

class ApiManager:

    gmaps = googlemaps.Client(key=LocalProperties.API_KEY)
