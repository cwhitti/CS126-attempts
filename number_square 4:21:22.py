
#12345
#23451
#34512
#45123
#51234

def number_square(smallest, largest):

    for current_row in range(smallest, largest + 1):

        for front in range(current_row, largest + 1):

            print(front, end = '')
    
        for back in range(smallest, current_row):

            print(back, end ='')             

        print()
        
number_square(1,5)
