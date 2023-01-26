def chewie(word):

    chewie_list = []

    #Make everything lowercase
    lower_word = word.lower()

    if len(lower_word) < 2:
        return[]

    for index in range(0,len(lower_word),2):
        chewie_list.append(lower_word[index:index+2])
                           
    print(chewie_list)

    

chewie("HeLLo")
