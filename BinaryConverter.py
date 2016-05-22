#READ ME
#This is a Python Script that will convert a given number to Binary and vice versa
#Still currently being worked on

value = input('Enter the binary value that you would like to convert to a whole number: ')

count = 0
total = 0
for digit in str(value):
	if digit == '1':
		total = total + (2**count)
	count += 1	
	

print length