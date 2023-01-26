def same_dashes(str1, str2):

    if len(str1) != len(str2):

        return False

    for index in range(len(str1)):

        if str1[index] == "-":

            if not str1[index] == str2[index]:

                return False
    
    return True

print(same_dashes("eep-","oop-ers"))
