import subprocess
import time

program = ["one", "logn", "n", "nlogn", "nsquare"]
# program = ["nsquare"]
file_location = "/home/teaguy21/Documents/exp"
for i in range(len(program)):
    proc1 = subprocess.Popen([f"cd /home/teaguy21/Documents/exp/{program[i]} && mprof run ./{program[i]}"], shell=True)
    time.sleep(1)
    proc1.kill()
    proc1.wait()
    proc2 = subprocess.Popen([f"cd /home/teaguy21/Documents/exp/{program[i]} && mprof run java {program[i]}"], shell=True)
    time.sleep(1)
    proc2.kill()
    proc2.wait()
    proc3 = subprocess.Popen([f"cd /home/teaguy21/Documents/exp/{program[i]} && mprof run node {program[i]}.js"], shell=True)
    time.sleep(1)
    proc3.kill()
    proc3.wait()
    proc4 = subprocess.Popen([f"cd /home/teaguy21/Documents/exp/{program[i]} && mprof run python3 {program[i]}.py"], shell=True)
    time.sleep(1)
    proc4.kill()
    proc4.wait()

