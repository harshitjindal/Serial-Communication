import serial                    # import pySerial module
import binascii

ser = serial.Serial('COM1')
print("Listening")


def readLoop():
    delimiterDetected = False
    receivedCharData = str()
    char = ""
    while (delimiterDetected != True):
        
        data = str(ser.read(426), "utf-8")
        if data[-8:] == 'c3bac39e':
            print("FADE: Sequence Detected")
            delimiterDetected = True
        else:
            print("SEQUENCE MISSING!")
    ##    print(data, end="\n\n")
print(data[-426:-418])
print(data[-418:-414])
print(data[-414:-158])
print(data[-158:-30])
print(data[-30:-8])
print(data[-8:])

readSequence = 3
for i in range(readSequence):
    readLoop()

##--------------------------------FUNCTIONAL CODE BELOW-----------

##    incomingData = ser.readline()
##    print(incomingData)
##
##    decodedData = str(incomingData, "utf-8")
##    print(decodedData, end="")
##
##    decodedData = bytes(binascii.unhexlify(incomingData[:-1]))
##    print(decodedData, end="")
##
##    decodedData = str(decodedData, "utf-8")
##    print(decodedData)
##
##    receivedData.append(decodedData)

##-------------------------------------------------------------------

ser.close()                  # Close the COM Port
print("Port Closed")
