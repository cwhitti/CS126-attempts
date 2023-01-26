def loop_mystery_exam1(i, j):
    while i != 0 and j != 0:
        i = i // j
        j = (j - 1) // 2
        print(str(i) + " " + str(j) + " ", end="")
    print(str(i))
    return i + j


loop_mystery_exam1(5, 0) #output	

loop_mystery_exam1(5, 0) #return	

loop_mystery_exam1(3, 2) #output	

loop_mystery_exam1(3, 2) #return

loop_mystery_exam1(16, 5) #output

loop_mystery_exam1(16, 5) #return

loop_mystery_exam1(80, 9) #output

loop_mystery_exam1(80, 9) #return

loop_mystery_exam1(1600, 40) #output

loop_mystery_exam1(1600, 40) #return
