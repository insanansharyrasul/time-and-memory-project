import time


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

with open("/home/teaguy21/Documents/plotting/constant.txt", "r") as file:
  first_line = file.readline()
  number_string = first_line.rstrip("\n")
  number = int(number_string)

arr = []
for i in range(number):
    arr.append(i)
    i += 1

x = 1

start = time.time_ns()
result = binarySearch(arr, 0, len(arr) - 1, x)
end = time.time_ns()   
print(format((end - start) / 10 ** 9, '.6f'))
# if result != -1:
#     print("Element is present at index", result)
# else:
#     print("Element is not present in array")
