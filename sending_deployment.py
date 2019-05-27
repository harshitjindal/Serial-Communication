import serial                    # import pySerial module
import binascii
from itertools import accumulate

print("Reading Parameters")
params = open("params.txt", "r")
port = str(params.readline().split("=")[1].replace("\n", ""))
baudrate = int(params.readline().split("=")[1])
bytesize=int(params.readline().split("=")[1])
stopbits=int(params.readline().split("=")[1])
parity=str(params.readline().split("=")[1].replace("\n", ""))
segment_indices = [(int(segment_index)*8) for segment_index in params.readline().split(" ")]
segment_indices = list(accumulate(segment_indices))

subsegment_indices = list()
for i in range(len(segment_indices)):
    subsegment = [(int(segment_index)) for segment_index in params.readline().split(" ")]
    subsegment = list(accumulate(subsegment)) #take cumulative sum of list items
    subsegment_indices.append(subsegment)

print(subsegment_indices)

params.close()

ser = serial.Serial(port)
ser.baudrate = baudrate
ser.bytesize = bytesize
ser.stopbits = 1
ser.parity = parity
print(ser)

print("Received Heartbeat from Basestation")
print("Attempting to Establish Connection")
input = input("")
print("Connection Successfully Established")
print("Listening...")

def partition(data, segment_indices):
    return [data[i:j] for i, j in zip([0]+segment_indices, segment_indices+[None])]

def readLoop():
    delimiterDetected = False
    receivedCharData = str()
    char = ""

    data = str(ser.read(4), "utf-8")
    while (delimiterDetected != True):
        
        while data[-4:] != 'FADE':
            char = str(ser.read(1), "utf-8")
            data += char
        data = data[-852:]
            
        bin_data = bin(int(data, 16))
        print(len(bin_data) - 2)
            
        datafile.write("FADE: Sequence Detected \n")
        delimiterDetected = True

    segmented_data = partition(bin_data[2:], segment_indices)
    subsegmented_data = list()

    for i in range(len(segment_indices)):
        print("Segment", i+1, ": ", segmented_data[i])
        datafile.write("Segment %d : %s \n" %(i+1, segmented_data[i]))
    
        subsegment = partition(segmented_data[i], subsegment_indices[i])
        subsegmented_data.append(subsegment)
        datafile_subsegments.write("Subsegment %d : %s \n" %(i+1, subsegmented_data[i]))
        
        binaryval = subsegmented_data[i]
        for j in range(len(binaryval)):
            if str(binaryval[j]) != '':
                datafile_decimal.write("Subsegment %d : %s \n" %(i+1, int(str(binaryval[j]), 2)))
        datafile_decimal.write("\n")
        print("\n\n")

readSequence = 5

datafile = open("received_data.txt", "w")
datafile_subsegments = open("subsegment_data.txt", "w")
datafile_decimal = open("decimal_data.txt", "w")

for i in range(readSequence):
    readLoop()
    datafile.write("\n")
    datafile_subsegments.write("\n")
datafile.close()
datafile_subsegments.close()
datafile_decimal.close()

ser.close()                  # Close the COM Port
print("Port Closed")
