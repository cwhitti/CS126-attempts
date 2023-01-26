print("This program reads exam/homework scores")
print("and reports your overall course grade.")
print()

#globals
global WeightedMidterm1Score
global WeightedMidterm2Score
global WeightedFinalScore
global WeightedHomeworkScore
global WeightedQuizScore
global WeightedDHomeworkScore

WeightedMidterm1Score = float(0)
WeightedMidterm2Score = float(0)
WeightedFinalScore = float(0)
WeightedHomeworkScore = float(0)
WeightedQuizScore = float(0)
WeightedDHomeworkScore = float(0)

#Main function
def main():
    
    midterm1()
    midterm2()
    final()
    homework()
    quizzes()
    dailyHomework()
    overall()
    
def midterm1():
    global WeightedMidterm1Score
    print("Midterm 1:")
    #Weight (0-100)?
    weight = int(input("Weight (0-100)? "))
    #Score earned
    score = int(input("Score earned? "))
    #Were scores shifted?
    shift = int(input("Were scores shifted (1=yes, 2=no)? "))
    if shift == 1:
        shiftamount = int(input("Shift amount? "))
        score += shiftamount
        if score >= 100:
            score = 100
        else:
            score = score
    elif shift == 2:
        score = score
    #Total points?
    print("Total points = " + str(score) + " / " + "100")
    score /= 100
    score *= weight
    # Round score
    score = round(score,1)
    # Results
    print("Weighted score = " + str(float(score)) + " / " + str(weight))
    WeightedMidterm1Score = float(score)
    print()
    return WeightedMidterm1Score
    
def midterm2():
    global WeightedMidterm2Score
    print("Midterm 2:")
    #Weight (0-100)?
    weight = int(input("Weight (0-100)? "))
    #Score earned
    score = int(input("Score earned? "))
    #Were scores shifted?
    shift = int(input("Were scores shifted (1=yes, 2=no)? "))
    if shift == 1:
        shiftamount = int(input("Shift amount? "))
        score += shiftamount
        if score >= 100:
            score = 100
        else:
            score = score
    elif shift == 2:
        if score >= 100:
            score = 100
        else:
            score = score
        
    #Total points? 
    print("Total points = " + str(score) + " / " + "100")
    score /= 100
    score *= weight
    #Round score
    score = round(score,1)
    print("Weighted score = " + str(float(score)) + " / " + str(weight))
    WeightedMidterm2Score = float(score)
    print()
    return WeightedMidterm2Score

def final():
    global WeightedFinalScore
    print("Final:")
    #Weight (0-100)?
    weight = int(input("Weight (0-100)? "))
    #Score earned
    score = int(input("Score earned? "))
    #Were scores shifted?
    shift = int(input("Were scores shifted (1=yes, 2=no)? "))
    if shift == 1:
        shiftamount = int(input("Shift amount? "))
        score += shiftamount
        if score >= 100:
            score = 100
        else:
            score = score
    elif shift == 2:
        if score >= 100:
            score = 100
        else:
            score = score
    #Total points?
    print("Total points = " + str(score) + " / " + "100")
    score /= 100
    score *= weight
    #round score
    score = round(score,1)
    # Results
    print("Weighted score = " + str(float(score)) + " / " + str(weight))
    WeightedFinalScore = float(score)
    print()
    return WeightedFinalScore
def homework():
    global WeightedHomeworkScore
    print("Homework:")
    #Weight (0-100)?
    weight = int(input("Weight (0-100)? "))
    # Number of assignments
    assignments = int(input("Number of assignments? "))
    #initialize variables
    score = 0
    maximum = 0
    for assignment in range(assignments):
        score += int(input(f"Assignment {assignment + 1}'s score? "))
        maximum += int(input(f"Assignment {assignment + 1}'s max? "))
    if score > maximum:
        score = maximum
    else:
        score = score
    #How many sections did you attend?
    attendedpoints = int(input("How many sections did you attend? ")) * 3
    if attendedpoints >= 34:
        attendedpoints = 34
    else:
        attendedpoints = attendedpoints
    #section points    
    print(f"Section points = {str(attendedpoints)} / 34")
    #total points
    my_points = score + attendedpoints
    total_points = maximum + 34
    print(f"Total points = {str(my_points)} / {str(total_points)}")   
    #weighted score
    #my_points /= maximum
    WeightedHomeworkScore = (my_points / total_points) * weight
    # Round score
    WeightedHomeworkScore = round(WeightedHomeworkScore, 1)
    # Results
    print(f"Weighted score = {str(float(WeightedHomeworkScore))} / {str(weight)}")
    print()
    return WeightedHomeworkScore

#Quizzes
def quizzes():
    global WeightedQuizScore
    print("Quizzes:")
    #Weight (0-100)?
    weight = int(input("Weight (0-100)? "))
    #total points earned
    score = int(input("Total points earned? "))
    #total points possible
    maximum = int(input("Total points possible? "))
    #total points
    print(f"Total points = {str(score)} / {str(maximum)}")
    WeightedQuizScore = score / maximum
    WeightedQuizScore *= weight
    # Round score
    WeightedQuizScore = round(WeightedQuizScore,1)
    # Results
    print(f"Weighted score = {str(WeightedQuizScore)} / {str(weight)}")
    print()
    #return WeightedQuizScore
    
# Daily Homework
def dailyHomework():
    global WeightedDHomeworkScore
    print("Daily Homework:")
    #Weight (0-100)?
    weight = int(input("Weight (0-100)? "))
    #total points earned
    score = int(input("Total points earned? "))
    #total points possible
    maximum = int(input("Total points possible? "))
    #total points
    # Results
    print(f"Total points = {str(score)} / {str(maximum)}")
    WeightedDHomeworkScore = score / maximum
    WeightedDHomeworkScore *= weight
    # round
    WeightedDHomeworkScore = round(WeightedDHomeworkScore,1)
    print(f"Weighted score = {str(WeightedDHomeworkScore)} / {str(weight)}")
    print()
    return WeightedDHomeworkScore

def overall():
    print()
    #overall percentage
    overall = WeightedMidterm1Score + WeightedMidterm2Score + WeightedFinalScore + WeightedHomeworkScore + WeightedQuizScore + WeightedDHomeworkScore
    if overall >= 90:
        grade = "A"
    elif overall >= 80: 
        grade = "B"
    elif overall >= 70: 
        grade = "C"
    elif overall >= 60: 
        grade = "D"
    else:
        grade = "F"
        
    # Results
    print(f"Overall percentage = {str(overall)}")
    print(f"Your grade will be at least: {grade}")
    # Comments
    if grade == "A":
        print("Nice job, Einstein!")
    elif grade == "B":
        print("Not too shabby!")
    elif grade == "C":
        print("C's get degrees!")
    elif grade == "D":
        print("Well, you tried.")
    elif grade == "F":
        print("The army is always an option.")
    
main()
