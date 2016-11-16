from Pascal_triangle import *


def print_pascal(lines_number, file_name):
    create_triangle(file_name, pascal(lines_number))

if __name__ == "__main__":
    print(print_pascal(9, "test.txt"))