def main():
    intro()
    task = ask_task()
    task()

def intro():
    print('Welcome to the CSC110 Book Recommender. Type the word in the')
    print('left column to do the action on the right.')
    
def ask_task():
    task = input("next task? ")

    return task

def recommend():
    print("This is the function for recommending books")
    
main()
