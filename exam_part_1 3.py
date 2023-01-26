# Show a number square from min to max.
def number_square(min, max):

    # Figure out how many numbers wide/rows long the square will be
    sqr_size = max - min + 1

    # For each row in the square
    for row in range(sqr_size):

        # Show the numbers in that particular row
        show_line(row, min, sqr_size)

# Show all of the values for a particular row in a number square
def show_line(row_number, min, sqr_size):

    # For each location in the row
    for location in range(sqr_size):

        # Calculate the number that is displayed given the location,
        # line number, min, and size of number square
        display_number = (location + row_number) % sqr_size + min

        # Show the number without going to the next line
        print(display_number, end="")

    # Line complete. Print a blank line to go to next line.
    print()
