import serial
ser = serial.Serial('/dev/cu.usbmodem641', 9600)
while 1:
	ser.readline()
	'1 Hello world!\r\n'
	'2 Hello world!\r\n'
	'3 Hello world!\r\n'