import subprocess
import os
# import signal

try:
    subprocess.Popen(["python3 nlogn.py"], shell=True)
    subprocess.Popen(["python3 plotting.py"], shell=True)
except KeyboardInterrupt:
    os.system("killall python3")