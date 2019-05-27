import serial               # import the module
import binascii

ser = serial.Serial('COM1') # open COM1

print("Attempting to Establish Connection")
print("Connection successfully Established!")



encodedData1 = bytes("fa114d92c39c5b8bee3ee3bfc16c3028391dfcbace6a65cc1b5c2c031ed880539eed19cedf7197ee5ab8eadefb8962028832598218781009eb0cbf15a511c0d0068d28458552bdab4f637d258d55565a2cad47423d6a3d6e5793bd07b381ff76327c48cdd9987f2379aaf88b97c8ae33318a6223062c603d3064190185748b194b8e1ac361c435fe81524d94f3f5f2faf5bef26b9140d08818f742db1562b3a7b71e3f0b0bd6156bd4fcd46e62e44a0c72b71e63e8d6a8142bb3b90a2d1fdc480128216f6ca0eab4cdca9cd4a1179e660fc3bac39e", "utf-8")
encodedData2 = bytes("7b2dc6484b7c3593cf95fce226463878c28b97e9f76b31b691ed0f8f9babf09430bce6e2f4294aa5abb54444f51df2029766d7926bf36d0f4c9dadd5c29c5320aa03d418cf1bb43fefbcc0ed07d7cedff8b029cf78eac5875f04e6e4ec806a5c8aaa6b8ff1562d12fe8ea3453720d16c7ae580c0c30f005efb761f3c4ab6ed19136d475c182a21f4738415c6b2bc1d4a4bc87af8f3588c19bc52ed333857e8ec0d9d0d2f5fe0575f38269ff7fa799638b8436c28b2fdf09c48dfa679f9778f527afacbba06d8cdf170b63e334afb658959c3bacd9e", "utf-8")
encodedData3 = bytes("f8609068f12bb5819d2952039d5abb64d8aaf9d1fb7d75927b2008141ded85e150f93f311ab93a45233e090999ee9fb5855494842c0473f0362fbe826ee3494c26aac6e535cf3f11181bbbb2c5268aa8e2de894636fe50c007bc9d0c3aacf639cdd25598a8a6a71d5cc8f30f019f58267098a149425eb323acb9e0b3d1fcf45196b74bdf86cdde6d1ea88d7c958f87e7b31bba716fb5bae892d6aa24a7bebef1e0e8739d5e87b2fd615d508f52efc16f1aecabb90124d0e48686591ae71616d76915e6a22a577093046001cec401b44c3bc3bac39e", "utf-8")

print("Sending")

import time
import sys
from tqdm import tqdm
for i in tqdm(range(10)):
    time.sleep(0.1)

sys.stdout.write("\n")
ser.write(bytes(encodedData1))
ser.write(bytes(encodedData2))
ser.write(bytes(encodedData3))
ser.write(b'\n')

ser.close()                 # Close the Com port
print("Connection Closed")


##   c3bac39e
