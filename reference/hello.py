import sys


def acceptInput():
	msg = ""
	while msg != "quit":
		msg = input("Tell me something, and I will repeat it back to you: ")
		print("Your tax level is: " + findTaxLevel())
		print(msg)
		
def findTaxLevel():
	tax_levels = [0.03, 0.1]
	return str(tax_levels[0])

acceptInput()