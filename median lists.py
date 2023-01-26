def median(a_list):
    mylist = a_list
    mylist.sort(reverse = False)
    middle = ((len(mylist) - 1)//2)
    print(mylist[middle])

median([5, 2, 4, 17, 55, 4, 3, 26, 18, 2, 17])




