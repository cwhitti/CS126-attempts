#import our geolocation class
from geolocation import *

#our main function
def main():

    #name the item information
    stash = GeoLocation(34.988889,-106.614444)
    ABQ = GeoLocation(34.989978,-106.614357)
    FBI = GeoLocation(35.131281,-106.61263)
    
    #print all the location info using the __str__ function
    print("the stash is at " + stash.__str__())
    print("ABQ studio is at " + ABQ.__str__())
    print("FBI building is at " + FBI.__str__())

    #print all the distance computations using the distance_from function
    print("distance in miles between:")
    print("    stash/studio = " + str(stash.distance_from(ABQ)))
    print("    stash/fbi    = " + str(stash.distance_from(FBI)))

main()
