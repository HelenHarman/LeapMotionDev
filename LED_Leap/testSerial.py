import serial

ser = serial.Serial('/dev/tty.usbmodem1421', 9600)

ser.flushInput()
ser.write([0, 0, 0, 0, 0, 0])