# This class stores information about a location on Earth.
# Locations are stored by their name, address, tag, latitude, and longitude.
# This class includes another class that compues the distance
# Between two locations

#import our stuff
from geolocation import *

class PlaceInformation:

    # constructs a geo location object with given latitude and longitude
    def __init__(self, name, address, tag, latitude, longitude):

        self.__name = str(name)
        self.__address = str(address)
        self.__tag = str(tag)
        self.__latitude = float(latitude)
        self.__longitude = float(longitude)

    # returns the name of this geo location
    def get_name(self):
        return self.__name

    # returns the address of this geo location
    def get_address(self):
        return self.__address

    # returns the tag of this geo location
    def get_tag(self):
        return self.__tag

    # returns the name and location of this geo location
    def __str__(self):

        locations = GeoLocation(self.__longitude, self.__latitude)

        location_string = locations.__str__()
        
        return "name: " + self.__name + ", " + str(self.location)
    
    # returns the location (longitude + latitude) of this geo location
    def get_location(self):

        location = GeoLocation(self.__longitude, self.__latitude)
        
        return str(location)

    # returns the distance in miles between this geo location and the given
    # other geo location using the geolocation file
    def distance_from(self, other):

        first_location = GeoLocation(self.__longitude, self.__latitude)

        distance = first_location.distance_from(other)
        
        return distance
