"""
Chemistry Help Tool

The tool provides options to fetch elements in the periodic table

Author : Rishav Das

Created on : March 17, 2021
"""

# Importing the required functions and modules
try:
	from os import system
	from sys import platform
except Exception as e:
	# If there are any errors in importing the functions and modules, then we print the error on the console screen and exit the script

	input('[ Error : {} ]\nPress enter key to continue...'.foramt(e))
	quit()

# Defining the clear screen function
if 'linux' in platform:
	# If the current operating system is a linux based, then we define clear() according to it

	clear = lambda : system('clear')
else:
	# If the current operating system is not linux, then it might be windows, so defining the clear() according to windows

	clear = lambda : system('cls')

# The main script starts here

periodicTable = [{"atomic_number" : 1, "element_name" : "Hydrogen"}, {"atomic_number" : 2, "element_name" : "Helium"}, {"atomic_number" : 3, "element_name" : "Lithium"}, {"atomic_number" : 4, "element_name" : "Berylium"}, {"atomic_number" : 5, "element_name" : "Boron"}, {"atomic_number" : 6, "element_name" : "Carbon"}]

def findElements(by, value):
	""" The function which returns the element after searching it from the periodic table using the user specified details i.e., either atomic number or element name """

	if by.lower() == 'z':
		# If the user specified the element search filter to be the atomic number, then we continue for it

		try:
			atomic_number = int(value)
			results = []
			# Iterating through the periodic table data
			for item in periodicTable:
				if item["atomic_number"] == atomic_number:
					# If the atomic number of the currently iterated item matches, then we append it to the search data

					results.append(item)
			return results
		except Exception as e:
			# If there are any errors in the process, then we print the error on the console screen and quit

			input('[ Error : {} ]\nPress enter key to continue...'.foramt(e))
			quit()
	elif by.lower() == 'name':
		# If the user specified the element search filter to be the element name, then we continue for it

		try:
			element_name = str(value)
			results = []
			# Iterating through the periodic table data
			for item in periodicTable:
				if (item["element_name"].lower() in element_name.lower()) or (element_name.lower() in item["element_name"].lower()):
					# If the search query matches, then we append it to the search result data

					results.append(item)
			return results
		except Exception as e:
                        # If there are any errors in the process, then we print the error on the console screen and quit

                        input('[ Error : {} ]\nPress enter key to continue...'.foramt(e))
                        quit()
	else:
		# If the user does not specified a valid and available element search filter, then we raise an error

		input('[ Error : No element search filter mentioned ]\nPress enter key to continue...')
		quit()

def main():
	""" The main function of the script (DRIVER CODE) """

	# Printing the main menu
	print("""
	CHEMISTRY HELP TOOL
    [ Author : Rishav Das https://github.com/rdofficial ]

[1] Display the entire periodic table
[2] Search for elements
[0] About
[X] Exit
""")

	# Asking the user to enter an option
	choice = input('Enter your choice : ')
	if choice == '1':
		# If the user chooses the option to print the entire list of elements

		# Printing the entire list of periodic table elements
		clear()
		print('The elements in the periodic table are listed below (arranged as per atomic number) : \n')
		for item in periodicTable:
			print('[{}] {}'.format(item["atomic_number"], item["element_name"]))
		input('\nPress enter key to continue...')
	elif choice == '2':
		# If the user chooses the option to search for a specific element and print it

		# Printing the further search menu
		clear()
		choice = input("""
Choose from below option to search :
[1] Search by element name
[2] Search by atomic number

Enter your choice : """)
		if choice == '1':
			# If the user chooses the option to search the element by the element name

			# Asking the user to enter the search element name query
			query = input('\nEnter a name to search for : ')
			results = findElements('name', query)

			# Printing the results on the console screen
			clear()
			print('The search results are : \n')
			for index, item in enumerate(results):
				# Iterating through each elements in the results array

				print('[{}] Atomic number : {} | Element Name : {}'.format(index + 1, item["atomic_number"], item["element_name"]))
			input('Press enter key to continue...')
			return 0
		elif choice == '2':
			# If the user enters the option to search for the element by its atomic number

			# Asking the user to enter the atomic number search query
			query = input('\nEnter the atomic number : ')
			results = findElements('z', query)

			# Printing the results on the console screen
			clear()
			print('The search results are : \n')
			for index, item in enumerate(results):
				# Iterating through each elements in the results array

				print('[{}] Atomic number : {} | Element Name : {}'.format(index + 1, item["atomic_number"], item["element_name"]))
			input('Press enter key to continue...')
			return 0
		else:
			# If the user enteres an unavailable option, then we print the error to the console screen

			input('[ Error : No element search filter mentioned ]\nPress enter key to continue...')
			return 0
	elif choice == '0':
		# If the user chooses the option to print the about information for this tool

		print(__doc__)
		input('Press enter key to continue...')
	elif choice.lower() == 'x' or choice.lower() == 'exit':
		# If the user entered the option to exit the script, then we quit the execution of the script

		quit()
	else:
		# If the user entered an unavailable option, then we print the error to the console screen

		input('[ Error : No element search filter mentioned ]\nPress enter key to continue...')
		return 0

if __name__ == '__main__':
	while True:
		try:
			clear()
			main()
		except KeyboardInterrupt:
			# If the user presses CTRL+C key combo, then we exit the execution of the script

			input('Press enter key to continue...')
			quit()
		except Exception as e:
			# If there are any errors during the execution of the script, then we print that error to the console screen

			input('[ Error : No element search filter mentioned ]\nPress enter key to continue...')
			continue
