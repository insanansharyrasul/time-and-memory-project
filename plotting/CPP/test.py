import subprocess

print((subprocess.check_output('./logn', shell=True)).decode('utf-8'))