#!/usr/bin/enc python

import serial, time, re

#Device name on OSX
#device_name = '/dev/cu.usbserial-AK068DL0'
device_name = '/dev/ttyUSB0'
power_on_command = 'PWR ON\r'.encode()
power_on_code = '01'
power_on_ack = ':'
power_check_command = 'PWR?\r'.encode()

ser = serial.Serial(device_name, timeout=5)
if ser.isOpen():
    ser.close()
ser.open()
ser.isOpen()

print('Turning on projector')
for i in range(5):
    ser.write(power_check_command)
    time.sleep(5)
    msg = ''
    msg = ser.read(10).decode('utf-8')
    powered_on = re.findall(power_on_code,msg)
    if not powered_on or not msg == power_on_ack:
        print('Checking if projector is on')
        print('Response from Projector = ' + msg)
        ser.write(power_on_command)
    else:
        break

print('Power is on')
ser.close()