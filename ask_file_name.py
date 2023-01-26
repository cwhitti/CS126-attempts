# importing os module 
import os
  
  
def demo():
    # Path
    prompt = input("Type a file name: ")
    path = '/home/User/Desktop/good.txt'
    
    #is it a file?
    isFile = os.path.isfile(prompt)

    #if the correct file has not been listed...
    while isFile == False:
        prompt = (input("Type a file name: "))
        
    #if the correct file has been listed
    return prompt     

demo()
