#

def number_square(min,max):
    for number in range(min,max+1):
        print_line(number,min,max)
        print()

def print_line(number,min,max):
    for iteration in range(number,max+1):
        print(iteration,end="")
    for iteration in range(min,number):
        print(iteration,end="")

number_square(1,5)

#loop_mystery_print1

#         *
#        ***
#       *****
#      *******
#     *********
#    ***********
#   *************
#  ***************
# *****************
#*******************

#numbeere_loops1

for i in range(1, 6):
    number = str(i)
    results = number * i
    print(results)

#print_stars

def print_stars(i):
    for index in range(i):
        print("*")

print_stars(3)

#parameter_mystery_exam2

#happy and pumpkin were orange
#orange and happy were pumpkin
#orange and sleepy were y
#pumpkin and x were green
#green and pumpkinorangehappy were vampire

#parameter_mystery_exam4

#2 5
#4 9
#5 4
#6 1

#parameter_mystery_exam6

#peacock in the study with the dagger
#study in the peacock with the mustard
#lounge in the mustard with the pipe
#ballroom in the dagger with the lounge

#complete_loop

for i in range(-4, 87, 18):
    print(i)

#carbonated

#say coke not pepsi or pop
#say soda not soda or pepsi
#say pepsi not koolaid or pop
#say say not pepsi or pepsi

#ftoc

# converts Fahrenheit temperatures to Celsius
def ftoc(tempf, tempc):
    tempc = (tempf - 32) * (5 // 9)

def main():
    tempf = 98.6
    tempc = 37.0
    ftoc(tempf, tempc)
    print("Body temp in C is:", tempc)

main()

#half_the_fun

#1 2 3 4 5
#1 2 3 4 5 6 7
#1 2 3 4
#number = 8

#print_powers_of_2

def print_powers_of_2(i):
    for i in range(0, i + 1):
        print(2**i, end = " ")

#print_powers_of_n

def print_powers_of_n(base, power):
    for i in range(0, power+1):
        print(base**i, end = " ")

#print_strings

def print_strings(name, number):
    for i in range(number):
        print(name, end = " ")
