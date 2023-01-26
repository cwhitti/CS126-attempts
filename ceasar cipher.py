def caesar_cipher():

    #get the inputs
    message = input("Your message? ").upper()
    key = int(input("Encoding key? "))
    
    #Set the size of the alphabet
    alphabet_size = 26 

    #loop through each letter in the message
    for letter in message:
        
        #Get the ord of the letter
        letter_ord = ord(letter)

        #check if the letter is not a space
        if letter_ord >= ord("A") and letter_ord <= ord("Z"):
            
            #get the encoded ord value
            shifted_ord = letter_ord + key

            #Make sure the shifted value is a real letter
            while shifted_ord > ord("Z"):

                shifted_ord -= alphabet_size
            
            #Make sure the shifted value is a real letter
            while shifted_ord < ord("A"):

                shifted_ord += alphabet_size
            
            #get the encoded character
            encoded_char = chr(shifted_ord)

            #print the encoded character
            print(encoded_char, end = "")

        #Print the space
        else:
            print(letter, end = "")
            
caesar_cipher()
