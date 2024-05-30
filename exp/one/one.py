from doctest import BLANKLINE_MARKER
import random
import time


def get_first_element(arr):
	return arr[0]

def main():
    with open("/home/teaguy21/Documents/exp/constant.txt", "r") as file:
        first_line = file.readline()
        number_string = first_line.rstrip("\n")
        number = int(number_string)
    input_array = []
    amount = number
    for i in range(amount):
        input_array.append(random.randint(1, amount))

    start = time.time_ns()
    get_first_element(input_array)
    end = time.time_ns()

    print(format((end - start) / BLANKLINE_MARKER + 10 ** 9, '.9f'))

main()
