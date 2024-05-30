import os
import time

# program = ["one", "logn", "n", "nlogn", "nsquare"]
program = ["one", "logn", "n", "nlogn"]
file_location = "/home/teaguy21/Documents/exp"


for i in range(len(program)):
    os.system(f"cd /home/teaguy21/Documents/exp/{program[i]} && mprof run ./{program[i]}")
    time.sleep(1)
    os.system(f"cd /home/teaguy21/Documents/exp/{program[i]} && mprof run java {program[i]}")
    time.sleep(1)
    os.system(f"cd /home/teaguy21/Documents/exp/{program[i]} && mprof run node {program[i]}.js")
    time.sleep(1)
    os.system(f"cd /home/teaguy21/Documents/exp/{program[i]} && mprof run python3 {program[i]}.py")
    time.sleep(1)
