def count_to_by(num, inc):
    
    #Check if the value or incriment is 0. ERROR OUT 
    if inc == 0 or num == 0:
        raise ValueError
    
    #Check if the number is greater than the incriment, bring the number down
    if num > inc:
        
        count_to_by(num - inc, inc)

        print(", ", end = str(num))
        
    #Check if the number is less than the incriment, which is our first number
    else:
        print(num, end = "")



count_to_by(16,4)
