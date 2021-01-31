
#!/usr/bin/enc python

import serial, time, re

# Device name on OSX
#device_name = '/dev/cu.usbserial-AK068DL0'
device_name = '/dev/ttyUSB0'
power_off_command = 'PWR OFF\r'.encode()
power_off_code = '00'
power_check_command = 'PWR?\r'.encode()

ser = serial.Serial(device_name, timeout=5)
if ser.isOpen():
    ser.close()
ser.open()
ser.isOpen()

print('Turning off projector')
for i in range(10):
    ser.write(power_check_command)
    time.sleep(5)
    msg = ''
    msg = ser.read(20).decode('utf-8')
    powered_off = re.findall(power_off_code,msg)
    if not powered_off:
        print('Checking if projector is off')
        print('Response from Projector = ' + msg)
        ser.write(power_off_command)
    else:
        break

print('Power is off')
ser.close()