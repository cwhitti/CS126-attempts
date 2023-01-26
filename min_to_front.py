def min_to_front(my_list):
    new_list = []
    count = 0
    ori_length = len(my_list)

    while count != ori_length:
        min = my_list[0]
        for num in range(len(my_list)):
            if my_list[num] < min:
                min = my_list[num]
        new_list.append(min)
        x = my_list.index(min)
        count += 1
        
    my_list.insert(0, x)

    #my_list
    print(my_list)

min_to_front([3, 8, 92, 4, 2, 17, 9])
