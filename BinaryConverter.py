#READ ME
#This is a Python Script that will convert a given  decimal number to Binary and vice versa
#Still currently being worked on
import Tkinter as tk

class BinaryConverter(tk.Frame):
	def convert(value, response):
		count = 0
		total = 0
		if value == "":
			total = "No Entry"
		elif response == 1:
			for digit in str(value):
				if digit == '1':
					total = total + (2**count)
				count += 1	
		else:
			total = ''
			#While loop to get the highest base that the value can go into
			while (value > 2**count):
				count +=1
			#for loop that counts backwards from the count value
			for place in range(count, 0, -1):
				if value >= 2**(place-1):
					total = total + '1'
					#To calculate the newly created value
					value = value - 2**(place-1)
				else:
					total = total + '0'
		print total;

	top = tk.Tk()
	v = tk.IntVar()
	B1 = tk.Radiobutton(top, text = "Decimal to Binary", variable = v, value = 1, indicatoron = 0).grid(row = 0, column = 0)

	B2 = tk.Radiobutton(top, text = "Binary to Decimal", variable = v, value = 2, indicatoron = 0).grid(row = 0, column = 1)

	EntryField = tk.Entry(top)
	EntryField.grid(row = 1, column = 1)


	Convert = tk.Button(top, text = "Convert", command = lambda:convert(EntryField.get(), v.get())).grid(row = 2, columnspan = 2)
	label = tk.Label(top, text = "Decimal/Binary Value").grid(row = 1, column = 0)
	Result = tk.Label(top, text = "Result:").grid(row = 3, column = 0)

top = tk.Tk()
BinaryConverter(top);
top.mainloop()


