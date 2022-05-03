def gantryright(self):
    import serial
    import time
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    for i in range(2):
        ser.write(b"2")
        line = str(ser.readline().decode('utf-8').rstrip())
