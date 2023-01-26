def number_square(min,max):
    for current_row in range(min,max+1):
        for front in range(current_row,max+1):
            print(front, end='')
        for back in range(min,current_row):
            print(back, end='')
        print()
        
number_square(1,5)
