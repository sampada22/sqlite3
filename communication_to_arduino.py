from __future__ import print_function
import glob
import struct
import time
import numpy as numpy

def look_For_Available_Ports():
    """find available serial ports to Arduino"""
    available_ports = glob.glob('/dv/ttyACM*')
    print("Available ports:")
    print(available_ports)

    return available_ports

def get_time_millis():
    return(int(round(time.time() * 1000)))

def get_time_seconds():
    return(int(round(time.time() * 1000000)))

def print_Values(self):
    print("-----ONE MORE MEASUREMENT-----")
    print("Humidity:",self.Data[0])
    print("Temperature in C:",self.Data[1])
    print("Temperature in F:",self.Data[2])
    print("Heat Index in F:",self.Data[3])
    print("Heat Index  in C:",self.Data[4])

class read_From_Arduino(object):
    """A class to read the serial messages from Arduino.(Arduino_Side_LSM9DS0 sketch)"""
    
    def __init__(self,port,SIZE_STRUCT = 8,verbose = 0):
        self.port = port
        self.millis = get_time_millis()
        self.SIZE_STRUCT = SIZE_STRUCT
        self.verbose = verbose
        self.Data = -1
        self.t_init = get_time_millis()
        self.t = 0

        self.port.flushInput()

    def read_one_value(self):
        """Wait for next serial message from Arduino,and read the whole message as a structure"""
        read = False

        while not read:
            myByte = self.port.read(1)
            if myByte.decode() == 'S':
                packed_data = self.port.read(self.SIZE_STRUCT)
                myByte = self.port.read(1)
                if myByte.decode() == 'E':
                    self.t = (get_time_millis() - self.t_init) /1000.0

                    #is a valid message struct
                    unpacked_data = struct.unpack('<hhhh',data)

                    current_time = get_time_millis()
                    time_elapsed = current_time - self.millis
                    self.millis = current_time

                    read = True

                    self.Data = np.array(unpacked_data)

                    return(True)

        return(False)

    def get_Humidity(self):
        self.read_one_value()
        return self.Data[0]

    def get_Temp_in_C(self):
        self.read_one_value()
        return self.Data[1]

    def get_Temp_in_F(self):
        self.read_one_value()
        return self.Data[2]
    
    def get_HeatIndex_in_F(self):
        self.read_one_value()
        return self.Data[3]
    
    def get_HeatIndex_in_C(self):
        self.read_one_value()
        return self.Data[4]

ports = serial_ports()
print(ports)
Arduino = serial.Serial('/dev/ttyACM0',9600)
read_From_Arduino_Instance = read_From_Arduino(Arduino,verbose = 6)

while True:
    print("Humidity:"read_From_Arduino_Instance.get_Humidity)
    print("Temperature in C:"read_From_Arduino_Instance.get_Temp_in_C)
    print("Temperature in F:"read_From_Arduino_Instance.get_Temp_in_F)
    print("Heat Index in F:"read_From_Arduino_Instance.get_HeatIndex_in_F)
    print("Heat Index in C:"read_From_Arduino_Instance.get_HeatIndex_in_C)