def mystery(dictionary):
    data = {}
    for (key, value) in dictionary.items():
        if value not in data:
            data[value] = set()
        data[value].add(key)
    print(data)
    return data
    
mystery({'hello': 4, 'world' : 4, 'and': 3})
