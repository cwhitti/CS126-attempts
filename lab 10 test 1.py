#import our geolocation class
from geolocation import *

#this is what we want to output
    #the stash is at latitude: 34.988889, longitude: -106.614444
    #ABQ studio is at latitude: 34.989978, longitude: -106.614357
    #FBI building is at latitude: 35.131281, longitude: -106.61263
    #distance in miles between:
        #stash/studio = 0.07548768123801672
        #stash/fbi    = 9.849836190409732

#initialize the items
stash = GeoLocation(34.988889,-106.614444)
ABQ = GeoLocation(34.989978,-106.614357)
FBI = GeoLocation(35.131281,-106.61263)

#our main function
def main():

    #print all the location info using the __str__ function
    print("the stash is at " + stash.__str__())
    print("ABQ studio is at " + ABQ.__str__())
    print("FBI building is at " + FBI.__str__())

    #print all the distance computations using the distance_from function
    print("distance in miles between:")
    print("    stash/studio = " + str(stash.distance_from(ABQ)))
    print("    stash/fbi    = " + str(stash.distance_from(FBI)))

main()
