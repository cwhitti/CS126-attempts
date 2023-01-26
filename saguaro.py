# Header : A program that programatically prints a cactus based off of a
#          constant

CACTUS_ARM_WIDTH = 2

def main():
    draw_upper_cactus()
    draw_middle_cactus()
    draw_lower_cactus()

# draw_upper_cactus() : prints the upper portion of the catus
def draw_upper_cactus():
    num_spaces = (CACTUS_ARM_WIDTH * 2 + 1) - (CACTUS_ARM_WIDTH + 2)
    num_top_row_spaces = num_spaces + 2
    num_top_row_x = CACTUS_ARM_WIDTH * 2
    num_rows = 2 * CACTUS_ARM_WIDTH - 1

    print(" " + "x" * CACTUS_ARM_WIDTH + " " * num_top_row_spaces + "x" *
            num_top_row_x)

    for row in range(num_rows):
        num_backslash = row + 1
        num_hyphen = 2 * CACTUS_ARM_WIDTH - row - 1
        print("X" + "-" * CACTUS_ARM_WIDTH + "X" + " " * num_spaces + "X" + "/"
                * num_backslash + "-" * num_hyphen + "X")

# draw_middle_cactus() : prints the middle portion of the cactus
def draw_middle_cactus():
    num_spaces_leading = 2 * CACTUS_ARM_WIDTH + 1
    num_center_width = 2 * CACTUS_ARM_WIDTH
    num_x_bottom_arm = 2 * CACTUS_ARM_WIDTH
    num_spaces_between_arm = (CACTUS_ARM_WIDTH * 2 + 1) - (CACTUS_ARM_WIDTH + 2)
    num_spaces_between_top_row = num_spaces_between_arm + 1
    num_rows = 2 * CACTUS_ARM_WIDTH - 1

    print(" " + "x" * num_x_bottom_arm + "X" + "~" * num_center_width + "X" +
            " " * num_spaces_between_top_row + "x" * CACTUS_ARM_WIDTH)

    for row in range(num_rows):
        num_forward_slash = row + 1
        num_hyphen = 2 * CACTUS_ARM_WIDTH - row - 1
        print(" " * num_spaces_leading + "X" + "-" * num_hyphen + "\\" *
                num_forward_slash + "X" + " " * num_spaces_between_arm + "X" + 
                "-" * CACTUS_ARM_WIDTH + "X")

# draw_lower_cactus() : prints the lower portion of the cactus
def draw_lower_cactus():
    num_spaces = 2 * CACTUS_ARM_WIDTH + 1
    num_center_width = 2 * CACTUS_ARM_WIDTH
    num_x_bottom_arm = 2 * CACTUS_ARM_WIDTH
    num_rows = 2 * CACTUS_ARM_WIDTH

    print(" " * num_spaces + "X" + "~" * num_center_width + "X" + "x" *
            num_x_bottom_arm)

    for row in range(num_rows):
        print(" " * num_spaces + "X" + "~" * num_center_width + "X")

main()