def mystery(dictionary):
    result = {}
    for key in dictionary:
        if key < dictionary[key]:
            result[key] = dictionary[key]
        else:
            result[dictionary[key]] = key
    print(result)

dictionary = {'skate': 'board', 'drive': 'car', 'program': 'computer', 'play': 'computer'}

mystery(dictionary)
