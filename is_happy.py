def is_happy_number(integer):
    mysum = 0
    tries = 0
    check_list = []
    integer = [int(value) for value in str(integer)]
    while mysum != 1:
        mysum = 0
        for value in range(len(integer)):
            mysum += integer[value] ** 2
        integer.clear()
        integer.append(mysum)
        integer = [int(value) for value in str(mysum)]
        tries += 1
        if tries > 10:
            Return False
    return True


is_happy(139)


#num = 13579
#x = [int(a) for a in str(num)]
#print(x)
