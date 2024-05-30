import random
import time
import csv


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

def binarySearch(arr, low, high, x):

    while low <= high:

        mid = low + (high - low) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1

# with open("/home/teaguy21/Documents/plotting/constant.txt", "r") as file:
#   first_line = file.readline()
#   number_string = first_line.rstrip("\n")
#   number = int(number_string)

n = 0
times = 0

labels = ["n", "times"]
with open('nsquare.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, labels)
    csv_writer.writeheader()

for i in range (10000):
    with open("nsquare.csv", "a") as csv_file:
        csv_writer = csv.DictWriter(csv_file, labels)
        info = {
            "n" : n,
            "times" : times
        }
        n += 1
        csv_writer.writerow(info)
        print(n, times)
        input_array = []
        amount = i
        for i in range(amount):
            input_array.append(random.randint(1, amount))

        start = time.time_ns()
        bubbleSort(input_array)
        end = time.time_ns()
        times = "{:.8f}".format(float((end - start) / 10 ** 9))
        # print(format((end - start) / 10 ** 9, ".6f"))


        
