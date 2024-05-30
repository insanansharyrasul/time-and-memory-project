import random
import time
import csv
import os

# O(1)
def get_first_element(arr):
	return arr[0]

# O(n^2)
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

# O(n)
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

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# O(n log n)
def mergeSort(arr, l, r):
    if l < r:

        m = l + (r - l) // 2

        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)

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

with open("/home/teaguy21/Documents/plotting/Python/constant.txt", "r") as file:
  first_line = file.readline()
  number_string = first_line.rstrip("\n")
  number = int(number_string)

arr = []
amount = number
for i in range(amount):
    arr.append(random.randint(1, amount))
n = len(arr)

arrBin = []
for i in range(amount):
    arr.append(i)
    i += 1

x = 1

x_values = 0
times1 = 0
times2 = 0
times3 = 0
times4 = 0
times5 = 0

field_name = ["x_values", "times1", "times2", "times3", "times4", "times5"]

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=field_name)
    csv_writer.writeheader()


while True:
    try:
        with open('data.csv', 'a') as csv_file:
            arr2 = arr[:]
            csv_writer = csv.DictWriter(csv_file, fieldnames=field_name)
            
            info = {
                "x_values" : x_values,
                "times1" : times1,
                "times2" : times2,
                "times3" : times3,
                "times4" : times4,
                "times5" : times5,
            }

            csv_writer.writerow(info)
            print(x_values, times1, times2, times3, times4, times5)

            x_values += 1
            # start1 = time.time_ns()
    
            # get_first_element(arr2)

            # end1 = time.time_ns()
            # start2 = time.time_ns()

            # binarySearch(arrBin, 0, len(arrBin) - 1, x)

            # end2 = time.time_ns()
            arr2 = arr[:]

            # start3 = time.time_ns()

            # count_sort(arr2)

            # end3 = time.time_ns()
            # arr3 = arr[:]
            # start4 = time.time_ns()

            # mergeSort(arr3, 0, n - 1)

            # end4 = time.time_ns()
            start5 = time.time_ns()

            bubbleSort(arr2)

            end5 = time.time_ns()
            # times1 = "{:.9f}".format(float((end1 - start1) / 10 ** 9))
            # times2 = "{:.9f}".format(float((end2 - start2) / 10 ** 9))
            # times3 = "{:.9f}".format(float((end3 - start3) / 10 ** 9))
            # times4 = "{:.9f}".format(float((end4 - start4) / 10 ** 9))
            times5 = "{:.9f}".format(float((end5 - start5) / 10 ** 9))
        time.sleep(0.01)
        
    except KeyboardInterrupt:
        os.remove("data.csv")
        break




# print(format((end - start) / 10 ** 9, ".6f"))
