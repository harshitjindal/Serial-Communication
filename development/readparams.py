port=COM1
baudrate = 9600
bytesize = 8
parity = 'N'
stopbits = 1
f = open("params.txt", "r")
port = str(f.readline())
baudrate = int(f.readline())
bytesize = int(f.readline())
parity = str(f.readline())
stopbits = int(f.readline())
segments = [int(segment) for segment in f.readline().split(" ")]
print(baudrate, bytesize, parity, stopbits, sep="\n")
print("Segments are: ", segments)
f.close()


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

def partition(alist, indices):
	return [alist[i:j] for i, j in zip([0]+indices, indices+[None])]
	
segmentedList = partition(list, segments)
print(segmentedList)