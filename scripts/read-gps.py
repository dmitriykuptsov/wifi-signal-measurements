import serial
import time

from datetime import datetime

def send_command(command):
    ser.write((command + '\r\n').encode())
    time.sleep(2)
    response = ser.read(ser.inWaiting())
    return response

port = "/dev/tty.usbserial-10"
ser = serial.Serial(port, 9600, timeout=1)
time.sleep(2)
send_command("AT")
print(send_command("AT+GPS=1"))
print(send_command("AT+GPSRD=1"))
time.sleep(10)
import re
coordinates = re.compile(".*(GPSRD.*GNGG.*,[0-9A-Z]{2}.*\*).*", re.MULTILINE)
fd = open("coordinates.txt", "w+")
while True:
	try:
		response = send_command("AT").decode("ASCII")
	except:
		time.sleep(0.5)
		continue
	g = coordinates.findall(response)
	if g:
		fd.write(str(datetime.utcnow()) + " " + g[0] + "\n")
		fd.flush()
	else:
		fd.write(str(datetime.utcnow()) + " No coordinates\n")
		fd.flush()
		
	time.sleep(0.5)
#response = ser.read(ser.inWaiting()).decode()
ser.close()

