def friend_list(myfile):
    friends = {}
    with open(myfile,"r") as filelines:
        #Put everyone in a dictionary
        for line in filelines:   
            (key, value) = line.split()
            if not key in friends:
                friends[key] = set()
            if not value in friends:
                friends[value] = set()
            friends[key].add(value)
            friends[value].add(key)
        for key in friends:
            friends[key] = list(friends[key])
            friends[key].sort()
            
        #now we have the names in a dictionary
        return friends

friend_list("buddies.txt")





