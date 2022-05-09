import subprocess

ip= ('netsh interface ipv4 show address Ethernet')
subprocess.run(ip,shell=True)