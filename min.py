#Our main function
def min_of_3(val1,val2,val3):
    
    #Checks if val1 is smaller than val2
    if val1 < val2:
        
        #if val1 is truly the smallest number of the three, print val1
        if val1 < val3:

            #Print val1
            print(val1)
        
        #if val1 is smaller than val2, but bigger than val3, print val3
        else:
            
            #print val3
            print(val3)
        
    #Checks if val2 is smaller than val1
    if val2 < val1:
        
        #if val2 is truly the smallest number of the three, print val2
        if val2 < val3:

            #Print val2
            print(val2)
        
        #if val2 is smaller than val1, but less than val3, print val3
        else:
            
            #Print val3
            print(val3)
            
    #checks if val1 and val2 are the same        
    if val1 == val2:

        #if the repeated number is smaller than val3, print val1
        if val1 < val3:

            #print val1
            print(val1)

        #If the repeated number is larger, print val3
        else:

            #print val3
            print(val3)
            
    
        
#Test the program
min_of_3(0,10,100)
min_of_3(100,10,3)
min_of_3(5,100,100)
