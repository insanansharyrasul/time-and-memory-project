#!/usr/bin/python3
import os
import subprocess

# program = ["one", "logn", "n", "nlogn"]
# program = ["nsquare"]
# program = ["logn"]
# program = ["nsquare"]
program = ["one", "logn", "n", "nlogn", "nsquare"]
name = ["C++", "Java", "JavaScript", "Python"]
file_location = "/home/teaguy21/Documents/exp"


def write(location, name):
    print(name)
    output = (subprocess.check_output(location, shell=True))
    print(output.decode("utf-8"))
    file.write(name + " " + str(output.decode("utf-8")))
    file.flush()

def start():
    for i in range(len(program)):
        os.system(f"cd {file_location}/{program[i]} && javac {program[i]}.java")
        os.system(f"cd {file_location}/{program[i]} && g++ -O2 {program[i]}.cpp -o {program[i]}")

start()


for i in range(len(program)):
    file = open(f"{program[i]}.txt", "a")
    java = f"java -cp {file_location}/{program[i]}/ {program[i]}"
    cpp = f"{file_location}/{program[i]}/{program[i]}"
    js = f"node {file_location}/{program[i]}/{program[i]}.js"
    py = f"python3 {file_location}/{program[i]}/{program[i]}.py"
    list = [cpp, java, js, py]
    for x in range(100):
        for y in range(len(list)):
            write(list[y], name[y])
    file.close()
    

