morse_dict = {
"A" : ".-",
"B" : "-...",
"C" : "-.-.",
"D" : "-..",
"E" : ".",
"F" : "..-.",
"G" : "--.",
"H" : "....",
"I" : "..",
"J" : ".---",
"K" : "-.-",
"L" : ".-..",
"M" : "--",
"N" : "-.",
"O" : "-= 1-",
"P" : ".--.",
"Q" : "--.-",
"R" : ".-.",
"S" : "...",
"T" : "-",
"U" : "..-",
"V" : "...-",
"W" : ".--",
"X" : "-..-",
"Y" : "-.--",
"Z": "--..",
" " : ""}

def to_morse_code(mapping,string):
    #string is "SOS TITANIC"
    list1=[]
    string = [x.upper() for x in string]
    #mapping is our dictionary
    list1[:0] = string
    #print(list(list1))
    for value in range(len(list1)):
        key = string[value]
        if key not in morse_dict:
            print("", end = "")
        else:
            print(morse_dict[key], end = " ")




to_morse_code(0,"WE are sinking Fast")
