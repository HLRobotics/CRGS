
from FireBase import firefetch
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

time.sleep(5)
ack=firefetch.fireFetch()
print(ack)

try:
    ser.write(str.encode(ack))
    print("[DATA SEND TO HARDWARE]")

except:
    print("[ERROR]")
