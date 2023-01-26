print("This program reads exam/homework scores")
print("and reports your overall course grade.")
print()

#main
def main():
    midterm1()
    midterm2()
    final()
    #homework()
    #quizzes()
    #daily_homework()
    overall_percentage()
    
#midterm1
def midterm1():
    print("Midterm 1:")
    #Weight (0-100)?
    print("Weight (0-100)? ", end ='')
    weight = int(input())
    #Score earned
    print("Score earned? ",end = '')
    score = int(input())
    #Were scores shifted?
    print("Were scores shifted (1=yes, 2=no)? ", end = '')
    shift = int(input())
    if shift == 1:
        print("Shift amount? ", end = '')
        shiftamount = int(input())
        newscore = score + shiftamount
        if newscore >= 100:
            newscore = 100
        else:
            newscore = newscore
    elif shift == 2:
        newscore = score
    #Total points?
    print("Total points = " + str(newscore) + " / " + "100")
    newscore /= 100
    newscore *= weight
    print("Weighted score = " + str(float(newscore)) + " / " + str(weight))
    WeightedMidterm1Score = float(newscore)
    print()
    return WeightedMidterm1Score
    
#midterm 2
def midterm2():
    print("Midterm 2:")
    #Weight (0-100)?
    print("Weight (0-100)? ", end ='')
    weight = int(input())
    #Score earned
    print("Score earned? ",end = '')
    score = int(input())
    #Were scores shifted?
    print("Were scores shifted (1=yes, 2=no)? ", end = '')
    shift = int(input())
    if shift == 1:
        print("Shift amount? ", end = '')
        shiftamount = int(input())
        newscore = score + shiftamount
        if newscore >= 100:
            newscore = 100
        else:
            newscore = newscore
    elif shift == 2:
        if score >= 100:
            newscore = 100
        else:
            newscore = score
    #Total points?
    print("Total points = " + str(newscore) + " / " + "100")
    newscore /= 100
    newscore *= weight
    print("Weighted score = " + str(float(newscore)) + " / " + str(weight))
    WeightedMidterm2Score = float(newscore)
    print()
    return WeightedMidterm2Score

#final
def final():
    print("Final:")
    #Weight (0-100)?
    print("Weight (0-100)? ", end ='')
    weight = int(input())
    #Score earned
    print("Score earned? ",end = '')
    score = int(input())
    #Were scores shifted?
    print("Were scores shifted (1=yes, 2=no)? ", end = '')
    shift = int(input())
    if shift == 1:
        print("Shift amount? ", end = '')
        shiftamount = int(input())
        newscore = score + shiftamount
        if newscore >= 100:
            newscore = 100
        else:
            newscore = newscore
    elif shift == 2:
        if score >= 100:
            newscore = 100
        else:
            newscore = score
    #Total points?
    print("Total points = " + str(newscore) + " / " + "100")
    newscore /= 100
    newscore *= weight
    print("Weighted score = " + str(float(newscore)) + " / " + str(weight))
    WeightedFinalScore = float(newscore)
    print()
    return WeightedFinalScore

#homework
def homework():
    print("Homework:")
    #Weight (0-100)?
    print("Weight (0-100)? ", end ='')
    weight = int(input())
    # Number of assignments
    print("Number of assignments? ", end ='')
    assignments = int(input())
    #Assignment scores
    for loop in range(assignments):
        print("Assignment " + loop + "score? ", end='')
        score = int(input())
        print("Assignment " + loop + "max? ", end='')
        maximum = int(input())
        score += score
        maximum += maximum
    #How many sections did you attend?
    print("How many sections did you attend? ", end = '')
    attendedpoints = int(input()) * 3
    if attendedpoints >= 34:
        attendedpoints = 34
    else:
        attendedpoints = attendedpoints
    print("Section points = " + str(attendedpoints) " / 34")
    
    print("Total points = " + str(score) " / " + str(score)
    
    
    #Assignment scores
    #Assignment max
    #How many sections did you attend?
    #Section points
    #Total points
    #weighted score

#Quizzes
    #weight
    #total points earned
    #total points possible
    #total points
    #weighted score

# Daily homework
    #weight
    #total points earned
    #total points possible
    #total points
    #weighted score

#overall percentage
def overall_percentage():
    midterm1score = midterm1()
    midterm2score = midterm2()
    print(midterm1score)
    #midterm1score(TIMES WEIGHT) + midterm1score(TIMES WEIGHT)+ finalexamscore(TIMES WEIGHT)
    #+ + homework score(TIMES WEIGHT)
    
main()
