#This program demonstrates the boxes and pigeons concept
import random
import math

def make_box_dict(boxes):

    box_dictionary = {}

    #Create a list for each box
    for index in range(1, boxes + 1):

        box_dictionary['box_%s' % index] = 0
        
    return box_dictionary


def distribute_pigeons(pigeons, box_dictionary):

    for pigeon in range(pigeons):

        #choose a random box
        random_box = random.choice(list(box_dictionary.keys()))

        #access the random box's dictionary
        random_box_value = box_dictionary.get(random_box)

        #add one pigeon to the random box's number
        random_box_value += 1

        #update the dictionary
        box_dictionary[random_box] = random_box_value

def results(boxes, box_dictionary):    

    for index in range(1,boxes + 1):

        current_box = "box_" + str(index)

        current_box_number = box_dictionary.get(current_box)

        if current_box_number == 1:

            print("Box " + str(index) + " = " + str(current_box_number) + " pigeon")
        
        else:
            print("Box " + str(index) + " = " + str(current_box_number) + " pigeons")
            
def reset_dictionary_content(boxes,box_dictionary):
    
    for index in range(1,boxes+1):

        #get the box numbers (key) for the dictionary
        current_box = "box_" + str(index)

        #reset the dictionary content
        box_dictionary[current_box] = 0
        
def calc_guaranteed_amount(pigeons, boxes):

    guaranteed_amount = (pigeons / boxes)

    guaranteed_amount = math.ceil(guaranteed_amount)
    
    print()
    print("Your pigeons have flown to their boxes!")
    print()
    print(f"You are guaranteed to have at least {guaranteed_amount}")
    print("pigeons in at least one box.")

    print()
    

def main():

    #init variables
    run_program = True

    #explain program
    print("This is a tool that demonstrates the")
    print("Box and Pigeon concept from Discrete Mathematics.\n")
    print("Each box will be populated with a random amount of")
    print("pigeons, all summing to your total amount of pigeons.\n")
    
    #Get input
    boxes = int(input("How many boxes? "))
    pigeons = int(input("How many pigeons? "))
    repeat_times = int(input("How many simulations? "))

    #something went wrong
    if ((boxes <= 0) or (repeat_times <= 0 )):
        
        print("\nERROR: You cannot have non-positive inputs!")
            
        run_program = False

    #process data
    if (run_program == True):

        box_dictionary = make_box_dict(boxes)
        
        calc_guaranteed_amount(pigeons, boxes)

        #Distribute pigeons
        for index in range(1, repeat_times+1):

            print("     Test " + str(index))

            distribute_pigeons(pigeons, box_dictionary)

            results(boxes, box_dictionary)

            reset_dictionary_content(boxes, box_dictionary)

        
    #end program
    print("End Program")
    

    return 0

main()
