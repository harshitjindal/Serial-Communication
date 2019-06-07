myData   = 'Øâþ   ÿþ  !Zk2ìm "Ï"À>q  úÞ'
yourData = 'Øâþ   ÿþ  !Zk2ìm "Ï"À>q  úÞ'

print(*[hex(ord(letter))[2:] for letter in myData])
print(*[hex(ord(letter))[2:] for letter in yourData])

string = 'Øâþ   ÿþ  !Zk2ìm "Ï"À>q  úÞ'
hexa = ['{:02x}'.format(ord(letter)) for letter in string]
print(type(hexa))

hexstr = ''
for i in range(len(hexa)):
	hexstr += hexa[i]
	
print(hexstr)
