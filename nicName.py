import subprocess

# static= ('netsh interface ipv4 show interface')
static= (f'netsh interface ipv4 set address name= "Ethernet" source=static address=172.16.20.10 mask=255.255.254.0')
s= subprocess.run(static,shell=True)




