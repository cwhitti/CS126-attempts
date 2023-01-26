def is_sorted(a_list):
    if len(a_list) == 1:
        return True
    value = 0
    tally = 0
    while a_list[value] <= a_list[value+1]:
        value += 1   
        tally += 1
        if tally == len(a_list)-1:
            break
    if tally == len(a_list)-1:
        return True
    else:
        return False
