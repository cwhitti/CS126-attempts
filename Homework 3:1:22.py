def odds():
    #make list
    mylist = []
    #put items in a list
    for i in range(-6,38,2):
        mylist.append(i)
    #shift the items +1
    newlist = [x+1 for x in mylist]
    print(f"odds = {newlist}")

odds()





