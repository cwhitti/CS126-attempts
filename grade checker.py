def main():

    check_grade =  int(input("Enter grade: "))

    if (check_grade > 90):
        
        print("You got an A!")

    elif (check_grade > 80):
        
        print("You got a B!")

    
    elif (check_grade > 70):
        
        print("You got a C!")

    elif (check_grade > 60):

        print("You got a D!")

    elif (check_grade > 50):

        print("You got a F!")

    elif (check_grade < 50):
        print("YOU FAILED LOLLLL")
main()
