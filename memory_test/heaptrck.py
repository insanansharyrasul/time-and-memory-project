import subprocess
import time

# file_location = "/home/teaguy21/Documents/exp"
# program = ["one", "logn", "n", "nlogn", "nsquare"]
# program = ["one", "logn", "n", "nlogn"]
# program = ["nlogn"]
program = ["nsquare"]
for i in range(len(program)):
    proc1 = subprocess.Popen([f"cd /home/teaguy21/Documents/memory_test/{program[i]} && heaptrack ./{program[i]}"], shell=True).wait()
    proc2 = subprocess.Popen([f"cd /home/teaguy21/Documents/memory_test/{program[i]} && heaptrack java {program[i]}"], shell=True).wait()
    proc3 = subprocess.Popen([f"cd /home/teaguy21/Documents/memory_test/{program[i]} && heaptrack node {program[i]}.js"], shell=True).wait()
    proc4 = subprocess.Popen([f"cd /home/teaguy21/Documents/memory_test/{program[i]} && heaptrack python3 {program[i]}.py"], shell=True).wait()
