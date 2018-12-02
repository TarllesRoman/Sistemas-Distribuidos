import bluetooth, time, json

bluez = ('20:16:10:25:34:22', 'HC-06')

sock = None
char_end = "!"

def connect():
    global sock
    if(sock != None): return True
    try:
        nearby_devices = bluetooth.discover_devices(lookup_names=True)
        tentativas = 2
        while (bluez not in nearby_devices) and tentativas:
            print("\nbluetooth nao encontrado, tentativas restantes: "+str(tentativas))
            nearby_devices = bluetooth.discover_devices(lookup_names=True)
            tentativas -= 1
        if(bluez in nearby_devices):
            print('Founded HC-06')
        else:
            raise Exception

        addr = bluez[0]
        port = 1
        sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
        sock.connect((addr, port))
        time.sleep(1)
        print("Connected HC-06")
        return True
    except:
        sock = None
        return False

def send_json(str_js):
    global sock
    try:
        sock.send(json.dumps(str_js))
        return True
    except:
        sock = None
        return False

def receive(end_c):
    global sock
    try:
        data = sock.recv(1024).decode('utf-8')
        while(end_c not in data):
            data = data+sock.recv(1024).decode('utf-8')
        return data
    except:
        sock = None
        return ""


"""
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
        tempo = int(input("Informe o tempo de alimentação: "))
        tanque = int(input("Informe o tanque a alimentar: "))
        dados = {
            "tanque":tanque,
            "tempo":tempo
        }
        sock.send(json.dumps(dados))
        data = sock.recv(1024).decode('utf-8')
        while("!" not in data):
            data = data+sock.recv(1024).decode('utf-8')
        print(data)
except Exception as e:
    print("Comando nao reconhecido... Finalizando conexao...")
    sock.close()
    print("ALL DONE!!!", e)
"""