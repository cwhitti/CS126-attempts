def fibonacci_square():
    #initialize variables
    
    value = 1
    next_value = 1
    added_together = 2
    
    #my program
    print("This program lists the Fibonacci sequence.")
    maximum = int(input("Max value? "))
    print("0", end='')
    while value <= maximum:
        print(f", {value}", end="")
        added_together = value + next_value
        value = next_value
        next_value = added_together 
        
fibonacci_square()

