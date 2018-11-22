import bluetooth, time

bluez = ('20:16:10:25:34:22', 'HC-06')

nearby_devices = bluetooth.discover_devices(lookup_names=True)
print("found %d devices" % len(nearby_devices))
while bluez not in nearby_devices:
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    print("found %d devices" % len(nearby_devices))

addr = bluez[0]
name = bluez[1]

print ("Conectando em %s - %s" %(name, addr))

port = 1

sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((addr, port))
time.sleep(1)
try:
    while True:
        cmd = input("Digite 1 para apagar led ou 2 para acender led ou 3 para sair!!!")
        if(cmd=='1'):
            sock.send('1')
        if(cmd=='2'):
            sock.send('2')
        if(cmd!='1' and cmd!='2'):
            print("Finalizando conexao...")
            sock.close()
            print("ALL DONE!!!")
            break     
except:
    print("Comando nao reconhecido... Finalizando conexao...")
    sock.close()
    print("ALL DONE!!!")