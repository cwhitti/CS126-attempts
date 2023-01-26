mylist = [1,2,3,4]

def list_testing():

    mylist.insert(len(mylist),5)

def list_testing2():

    print(mylist)

    list_testing()
            
    print(mylist)

def list_testing3():

    print(mylist)

    mylist.insert(len(mylist),"lol")

    print(mylist)
    
    
list_testing2()

list_testing3()
