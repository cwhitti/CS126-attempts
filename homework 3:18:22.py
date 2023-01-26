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

num2 = {
'board': 'skate',
'car': 'drive',
'computer': 'play',
}

num3 = {
'begin': 'end',
'boy': 'girl',
'ebert': 'siskel',
'first': 'last',
'H': 'T'
}

num4 = {
'cotton': 'rain',
'light': 'tree',
'seed': 'tree',
'tree': 'violin'
}
