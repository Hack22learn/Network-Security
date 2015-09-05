import string
str=string.ascii_uppercase
print 'Text to be decrypted is UVACLYFZLJBYL'
inp = 'UVACLYFZLJBYL'

for shift in range(0, 25):
	data=[]
	for i in inp:
		if i.strip() and i in str:
			data.append(str[(str.index(i) - shift) % 26])
		else:
			data.append(i)
	output = ''.join(data)
	print output
	print ' '

