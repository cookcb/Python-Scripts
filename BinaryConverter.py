#READ ME
#This is a Python Script that will convert a given  decimal number to Binary and vice versa
#Still currently being worked on

response = raw_input('Type "one" for binary -> whole number and "two" for whole number -> binary: ')

value = input('Enter the value that you would like to convert: ')

def convert(value, response):
	count = 0
	total = 0
	if response == 'one':
		for digit in str(value):
			if digit == '1':
				total = total + (2**count)
			count += 1	
	else:
		total = ''
		#While loop to get the highest base that the value can go into
		while (value > 2**count):
			count +=1
		for place in range(count, 0, -1):

	return total;


print convert(value, response)