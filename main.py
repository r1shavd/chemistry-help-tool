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

periodicTable = [{"atomic_number" : 1, "element_name" : "Hydrogen"}, {"atomic_number" : 2, "element_name" : "Helium"}, {"atomic_number" : 3, "element_name" : "Lithium"}, {"atomic_number" : 4, "element_name" : "Berylium"}, {"atomic_number" : 5, "element_name" : "Boron"}, {"atomic_number" : 6, "element_name" : "Carbon"}, {"atomic_number" : 7, "element_name" : "Nitrogen"}, {"atomic_number" : 8, "element_name" : "Oxygen"}, {"atomic_number" : 9, "element_name" : "Fluorine"}, {"atomic_number" : 10, "element_name" : "Neon"}, {"atomic_number" : 11, "element_name" : "Sodium"}, {"atomic_number" : 12, "element_name" : "Magnesium"}, {"atomic_number" : 13, "element_name" : "Aluminium"}, {"atomic_number" : 14, "element_name" : "Sillon"}, {"atomic_number" : 15, "element_name" : "Phosphorus"}, {"atomic_number" : 16, "element_name" : "Sulphur"}, {"atomic_number" : 17, "element_name" : "Chlorine"},{"atomic_number" : 18, "element_name" : "Argon"}, {"atomic_number" : 19, "element_name" : "Potassium"}, {"atomic_number" : 20, "element_name" : "Calcium"}, {"atomic_number" : 21, "element_name" : "Scandium"}, {"atomic_number" : 22, "element_name" : "Titanium"}, {"atomic_number" : 23, "element_name" : "Vanadium"}, {"atomic_number" : 24, "element_name" : "Chromium"}, {"atomic_number" : 25, "element_name" : "Maganese"}, {"atomic_number" : 26, "element_name" : "Iron"}, {"atomic_number" : 27, "element_name" : "Cobalt"}, {"atomic_number" : 28, "element_name" : "Nickel"}, {"atomic_number" : 29, "element_name" : "Copper"}, {"atomic_number" : 30, "element_name" : "Zinc"}, {"atomic_number" : 31, "element_name" : "Gallium"}, {"atomic_number" : 32, "element_name" : "Germanium"}, {"atomic_number" : 33, "element_name" : "Arsenic"}, {"atomic_number" : 34, "element_name" : "Selenium"}, {"atomic_number" : 35, "element_name" : "Bromine"}, {"atomic_number" : 36, "element_name" : "Krypton"}, {"atomic_number" : 37, "element_name" : "Rubidium"}, {"atomic_number" : 38, "element_name" : "Strontium"}, {"atomic_number" : 39, "element_name" : "Yttrium"}, {"atomic_number" : 40, "element_name" : "Zirconium"}, {"atomic_number" : 41, "element_name" : "Niobium"}, {"atomic_number" : 42, "element_name" : "Molybdenum"},{"atomic_number" : 43, "element_name" : "Technetium"}, {"atomic_number" : 44, "element_name" : "Ruthenium"}, {"atomic_number" : 45, "element_name" : "Rhodium"}, {"atomic_number" : 46, "element_name" : "Palladium"}, {"atomic_number" : 47, "element_name" : "Silver"}, {"atomic_number" : 48, "element_name" : "Cadmium"}, {"atomic_number" : 49, "element_name" : "Indium"}, {"atomic_number" : 50, "element_name" : "Tin"}, {'atomic_number': 51, 'element_name': 'Antimony'}, {'atomic_number': 52, 'element_name': 'Tellurium'}, {'atomic_number': 53, 'element_name': 'Iodine'}, {'atomic_number': 54, 'element_name': 'Xenon'}, {'atomic_number': 55, 'element_name': 'Cesium'}, {'atomic_number': 56, 'element_name': 'Barium'}, {'atomic_number': 57, 'element_name': 'Lanthanum'}, {'atomic_number': 58, 'element_name': 'Cerium'}, {'atomic_number': 59, 'element_name': 'Praseodymium'}, {'atomic_number': 60, 'element_name': 'Neodymium'}, {'atomic_number': 61, 'element_name': 'Promethium'}, {'atomic_number': 62, 'element_name': 'Samarium'}, {'atomic_number': 63, 'element_name': 'Europium'}, {'atomic_number': 64, 'element_name': 'Gadolinium'}, {'atomic_number': 65, 'element_name': 'Terbium'}, {'atomic_number': 66, 'element_name': 'Dysprosium'}, {'atomic_number': 67, 'element_name': 'Holmium'}, {'atomic_number': 68, 'element_name': 'Erbium'}, {'atomic_number': 69, 'element_name': 'Thulium'}, {'atomic_number': 70, 'element_name': 'Ytterbium'}, {'atomic_number': 71, 'element_name': 'Lutetium'}, {'atomic_number': 72, 'element_name': 'Hafnium'}, {'atomic_number': 73, 'element_name': 'Tantalum'}, {'atomic_number': 74, 'element_name': 'Tungsten'}, {'atomic_number': 75, 'element_name': 'Rhenium'}, {'atomic_number': 76, 'element_name': 'Osmium'}, {'atomic_number': 77, 'element_name': 'Iridium'}, {'atomic_number': 78, 'element_name': 'Platinum'}, {'atomic_number': 79, 'element_name': 'Gold'}, {'atomic_number': 80, 'element_name': 'Mercury'}, {'atomic_number': 81, 'element_name': 'Thallium'}, {'atomic_number': 82, 'element_name': 'Lead'}, {'atomic_number': 83, 'element_name': 'Bismuth'}, {'atomic_number': 84, 'element_name': 'Polonium'}, {'atomic_number': 85, 'element_name': 'Astatine'}, {'atomic_number': 86, 'element_name': 'Radon'}, {'atomic_number': 87, 'element_name': 'Francium'}, {'atomic_number': 88, 'element_name': 'Radium'}, {'atomic_number': 89, 'element_name': 'Actinium'}, {'atomic_number': 90, 'element_name': 'Thorium'}, {'atomic_number': 91, 'element_name': 'Protactinium'}, {'atomic_number': 92, 'element_name': 'Uranium'}, {'atomic_number': 93, 'element_name': 'Neptunium'}, {'atomic_number': 94, 'element_name': 'Plutonium'}, {'atomic_number': 95, 'element_name': 'Americium'}, {'atomic_number': 96, 'element_name': 'Curium'}, {'atomic_number': 97, 'element_name': 'Berkelium'}, {'atomic_number': 98, 'element_name': 'Californium'}, {'atomic_number': 99, 'element_name': 'Einsteinium'}, {'atomic_number': 100, 'element_name': 'Fermium'}, {'atomic_number': 101, 'element_name': 'Mendelevium'}, {'atomic_number': 102, 'element_name': 'Nobelium'}, {'atomic_number': 103, 'element_name': 'Lawrencium'}, {'atomic_number': 104, 'element_name': 'Rutherfordium'}, {'atomic_number': 105, 'element_name': 'Dubnium'}, {'atomic_number': 106, 'element_name': 'Seaborgium'}, {'atomic_number': 107, 'element_name': 'Bohrium'}, {'atomic_number': 108, 'element_name': 'Hassium'}, {'atomic_number': 109, 'element_name': 'Meitnerium'}, {'atomic_number': 110, 'element_name': 'Darmstadtium'}, {'atomic_number': 111, 'element_name': 'Roentgenium'}, {'atomic_number': 112, 'element_name': 'Copernicium'}, {'atomic_number': 113, 'element_name': 'Ununtrium'}, {'atomic_number': 114, 'element_name': 'Flerovium'}, {'atomic_number': 115, 'element_name': 'Ununpentium'}, {'atomic_number': 116, 'element_name': 'Livermorium'}, {'atomic_number': 117, 'element_name': 'Ununseptium'}, {'atomic_number': 118, 'element_name': 'Ununoctium'},]

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
