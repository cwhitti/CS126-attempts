#temp getter and stat maker

def main():
    #get an input from user for the number of days
    day_count = int(input("How many day's temps? "))
    #initialize temp_total
    temp_total = 0
    #for each day
    for day in range(day_count):
        temp = int(input(f"Day {day + 1}'s high temp: "))
        temp_total += temp
        
    avg_temp = temp_total / day_count
    print(f"Average temp = {avg_temp}")
        
main()
