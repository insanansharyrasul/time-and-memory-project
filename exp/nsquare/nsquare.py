import random
import time


def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if swapped == False:
            break

with open("/home/teaguy21/Documents/exp/constant.txt", "r") as file:
  first_line = file.readline()
  number_string = first_line.rstrip("\n")
  number = int(number_string)

input_array = []
amount = number
for i in range(amount):
    input_array.append(random.randint(1, amount))

start = time.time_ns()
bubbleSort(input_array)
end = time.time_ns()

print(format((end - start) / 10 ** 9, ".6f"))
