import nmap
import subprocess


nm = nmap.PortScanner()
# mapeo= nm.scan('172.16.20.65', '22-443')
diccionario= {}

for num in range(20,22):
    static= (f'netsh interface ipv4 set address name= "Ethernet" source static address=172.16.{num}.10 mask=255.255.254.0')
    for num1 in range(1,254+1):
        ip = f'172.16.{num}.{num1}'
        print(ip)
        mapeo= nm.scan(ip, '22-443')
        try:
            map= mapeo['scan']
            scaneo= map[ip]
            adress= scaneo['addresses']
            mac= adress['mac']
            vendor= scaneo['vendor']
            fabricante= vendor[mac]
            diccionario[ip]=[mac,fabricante]
        except:
            print("no hay nada")

print(diccionario)
# df = pd.DataFrame([[key, diccionario[key]] for key in diccionario.keys()],
#     columns=['IP', 'MAC', 'Fabricante'])
# df.head(5)   
#     diccionario[ip]=[]
#     mapeo= nm.scan(ip, '22-443-80')

#     print(f'172.16.20.{ip}')
# state= nm['172.16.20.65'].state()
# dic= mapeo.__dict__
# print(f'el diccionario es {mapeo}')


