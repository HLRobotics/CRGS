import serial
import time
try:
    ser = serial.Serial("/dev/ttyUSB0", '9600')
    print('[Connected to USB0]')
except:
    print('[CRGS not connected USB0]')

try:
    ser = serial.Serial("/dev/ttyUSB1", '9600')
    print('[Connected to USB1]')
except:
    print('[CRGS not connected USB1]')



import socket
PORT = 65432        # The port used by the server
HOST=input("[Enter IP of CRGS GUIDANCE SYSTEM RONALDO SERVER]")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("[CONNECTED TO RONALDO REMOTE GUIDANCE SYSTEM]")
    while True:
        data = s.recv(1024)
        print(data.decode('utf-8'))
        time.sleep(1)
        try:
            ser.write(str.encode(data.decode('utf-8')))
            print("[SENT]")
        except:
            print("[ERROR]")