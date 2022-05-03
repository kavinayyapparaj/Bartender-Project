def glassposition(self):
    import serial
    import time
    if __name__ == '__main__':
        ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        ser.reset_input_buffer()
        a = []
        for i in range(2):
            ser.write(b"1")
            line = str(ser.readline().decode('utf-8').rstrip())
            a.append(line)
        print(a[1])
        return a[1]
