import csv
import time
import random

from attr import fields_dict

def count_sort(input_array):
    M = max(input_array)
 
    count_array = [0] * (M + 1)
 
    for num in input_array:
        count_array[num] += 1
 
    for i in range(1, M + 1):
        count_array[i] += count_array[i - 1]
 
    output_array = [0] * len(input_array)
 
    for i in range(len(input_array) - 1, -1, -1):
        output_array[count_array[input_array[i]] - 1] = input_array[i]
        count_array[input_array[i]] -= 1
 
    return output_array
 
# with open("/home/teaguy21/Documents/plotting/constant.txt", "r") as file:
#   first_line = file.readline()
#   number_string = first_line.rstrip("\n")
#   number = int(number_string)
fields = ["n", "times"]
n = 0
times = 0
with open('n.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fields)
    csv_writer.writeheader()

for j in range(1, 50001):
    with open('n.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fields)
        info = {
            "n" : n,
            "times" : times
        }
        csv_writer.writerow(info)
        print(n, times)
        amount = j
        input_array = []
        for i in range(amount):
            input_array.append(random.randint(1, amount))
        n += 1
        start = time.time_ns()
        count_sort(input_array)
        end = time.time_ns()
        times = "{:.8f}".format(float((end - start) / 10 ** 9))
        # print(format((end - start) / 10 ** 9, ".6f"))

