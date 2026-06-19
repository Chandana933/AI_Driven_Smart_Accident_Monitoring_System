import serial

ser = serial.Serial('COM3',9600)

def read_sensor():

    line = ser.readline().decode().strip()

    try:
        gas,x,y = line.split(',')

        return float(gas),float(x),float(y)

    except:
        return None