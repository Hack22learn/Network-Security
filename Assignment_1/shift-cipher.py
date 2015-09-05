str='abcdefghijklmnopqrstuvwxyz'

shift=int(raw_input('Input the shift : '))
inp=raw_input('Input text to be encrypted : ')
data=[]
for i in inp:
	if i.strip() and i in str:
		data.append(str[(str.index(i) + shift) % 26])
	else:
		data.append(i)

output = ''.join(data)
print output
