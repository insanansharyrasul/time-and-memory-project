import subprocess
import csv

x = 0
one = 0
logn = 0
n = 0
nlogn = 0
nsquare = 0

field_names = ['x', 'one', 'logn', 'n', 'nlogn', 'nsquare']
with open('data.csv', 'w') as csv_file:
    csv_reader = csv.DictWriter(csv_file, field_names)
    csv_reader.writeheader()

while True:
    with open('data.csv', 'a') as csv_file:
        csv_reader = csv.DictWriter(csv_file, field_names)
        info = {
            'x' : x,
            'one': one,
            'n': n,
            'logn' : logn,
            'nlogn' : nlogn,
            'nsquare': nsquare
        }
        csv_reader.writerow(info)
        print(x, one, logn, n, nlogn, nsquare)
        x += 1
        one = "{:.9f}".format(float(subprocess.check_output('./one', shell=True).decode('utf-8')))
        logn = "{:.9f}".format(float(subprocess.check_output('./logn', shell=True).decode('utf-8')))
        n = "{:.9f}".format(float(subprocess.check_output('./n', shell=True).decode('utf-8')))
        nlogn = "{:.9f}".format(float(subprocess.check_output('./nlogn', shell=True).decode('utf-8')))
        nsquare = "{:.9f}".format(float(subprocess.check_output('./nsquare', shell=True).decode('utf-8')))
