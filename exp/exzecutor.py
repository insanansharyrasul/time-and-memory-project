import os


program = ["one", "logn", "n", "nlogn", "nsquare"]
file_location = "/home/teaguy21/Documents/exp"

def start():
    for i in range(len(program)):
        os.system(f"cd {file_location}/{program[i]} && javac {program[i]}.java")
        os.system(f"cd {file_location}/{program[i]} && g++ -O2 {program[i]}.cpp -o {program[i]}")

start()