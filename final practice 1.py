def is_unique(mylist):

    #sort the list in order

    mylist.sort()
          
    for index in range(len(mylist)):

        current_number = mylist[index]

        if index == 0:

            next_number = mylist[-1]

        if index == (len(mylist) -1):

            next_number = mylist[0]
            
        else:
            
            next_number = mylist[index + 1]

        if current_number == next_number:

            return False
        
    return True
        

    
print(is_unique([4]))
