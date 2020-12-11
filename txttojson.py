filename = 'dict.txt'

# Converting raw data into a dictionary list

dict1 = []

file = open('dict.txt')

for i in range(0,10):
	data = file.readline()
	ptr = file.tell()
	file.seek(ptr)
	dict1.append(data)

print(dict1)





