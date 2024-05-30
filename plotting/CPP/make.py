import subprocess

program = ['one', 'logn', 'n', 'nlogn', 'nsquare']

for i in range(len(program)):
    subprocess.Popen([f'g++ {program[i]}.cpp -o {program[i]}'], shell=True)