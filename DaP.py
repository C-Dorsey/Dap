"""
Divisors and Primes Code:
This program automates some of the functions of a divisor like showing what 
numbers are divisors of a given number. It also automates some of the functions
relating to primes, like checking if a given number is a prime. 

@Author Cohl Dorsey
"""

import math # Inported math in order to use the square root method; sqrt(n) 

# Checks to see if a given value is prime. Returns False if it isn't, and True if it is
def chkPrime(n):
	i = 2
	while(i < (n-1)):
		if(n%i == 0):
			return False
		i = i+1
	return True

# Method takes in an integer and shows its divisors
def onlyDivisors(n):
	i = 1
	while(i <= n):
		if(n%i == 0):
			print "\t", i, "divides", n
		i = i+1

# Method takes in a number, then takes the square root of it. Then
# it checks the given number against all numbers starting from 1 up
# to the value of its square root using the modulus operator to check
# if the input value is prime.
def divides(n):
	sqroot = int(math.sqrt(n))
	print "Square root:", sqroot
	i = 1
	while(i <= sqroot):
		if(n%i == 0):
			print "\t", i, "divides", n
		i = i+1

# This method calculates twin primes
def tp(n):
	print "\nThe twin primes up to", n, "are:"
	i = 1
	while(i <= n):
		p = chkPrime(i)
		p2 = chkPrime((i+2))
		if(p and p2):
			print "\t", i, "and", i+2
		i = i+1
	raw_input("HIT ENTER TO CONTINUE...")
	inputs()
	
# Method takes in an integer and uses the formula f(n)= n^2 + n + 41 and checks if the result is prime
def function(n):
	result = (n ** 2) + n + 41
	print "\nThe result of n=", n, "of f(n)= n^2 + n + 41 =", result, "being prime is: ", chkPrime(result)
	onlyDivisors(result)
	raw_input("\nHIT ENTER TO CONTINUE...")
	inputs()	

# Special version of the function method for the automate method 
def functiona(n):
	result = (n ** 2) + n + 41
	print "\nThe result of n=", n, "of f(n)= n^2 + n + 41 =", result, "being prime is: ", chkPrime(result)
	onlyDivisors(result)
	raw_input("\nHIT ENTER TO CONTINUE...")	
	
# Method automates passing incrementing integers from 1 up to a given value into the function method 
def automate(n):
	i = 1
	while(i <= n):
		print "Passing in n =", i 
		functiona(i)
		i = i+1
	inputs()
	
# Method that takes in input from the user, then passes it to the method for calculation
def method2():
	n = raw_input("\nEnter an integer that's larger than 0 :  ")
	divides(int(n))
	raw_input("\nHIT ENTER TO CONTINUE...")
	inputs()

# Method that takes in input from the user, then passes it to the method for calculation	
def method1():
	n = raw_input("\nEnter an integer that's larger than 0 :  ")
	onlyDivisors(int(n))
	raw_input("\nHIT ENTER TO CONTINUE...")
	inputs()

# Takes in an integer and checks to see if it's a prime number 
def check(n):
	result = chkPrime(n)
	print "\nThe number", n, "is", result
	if(result == True):
		print n, "is prime! :)"
		onlyDivisors(n)
	if(result == False):
		print n, "is not prime... :("
		onlyDivisors(n)
	raw_input("\nHIT ENTER TO CONTINUE...")
	inputs()
	
# Method takes in an integer and displays all Mersenne Primes up to that number 
def mp(n):
	i = 1
	print "\nAll numbers of 2^p - 1 up to", n, "that are primes:"
	while(i <= n):
		result = (2 ** i) - 1
		prm = chkPrime(result)
		if(prm == True):
			print "\t(2^",i,") - 1 =", result
		i = i+1
	
	j = 1
	print "\nAll numbers of 2^p - 1 up to", n, "that are not primes:"
	while(j <= n):
		result = (2 ** j) - 1
		prm = chkPrime(result)
		if(prm == False):
			print "\t(2^",j,") - 1 =", result
		j = j+1
	raw_input("\nHIT ENTER TO CONTINUE...")
	inputs() 
	
# Method that takes in input from the user, and keeps the program going until given the input to quit 
def inputs():
	print "--Check to see if a given number is a prime.\n\tFor this option enter 'check'"
	print "--Show all divisors up to a given value.\n\tFor this option enter 'method1'."
	print "--Show all the divisors up to the square root of the given value.\n\tFor this option enter 'method2'"
	print "--Use the formula f(n) = n^2 + n + 41 on a given value and shows if the \n\tresult is a prime or not. For this option enter 'function'"
	print "--Pass incrementing values of 1 to a given value into the function method.\n\tFor this option enter 'auto'"
	print "--Checks twin primes (p and p+2) up to a certain number.\n\tFor this option enter 'tp'"
	print "--Display all Mersenne Primes up to a given integer.\n\tFor this option enter 'mp'"
	print "--Enter 'q' to quit"
	
	option = raw_input("\nEnter option: ")
	
	if(option == 'check'):
		n = raw_input("Enter an integer that's larger than 0:	")
		check(int(n))
	if(option == 'method1'):
		method1()
	if(option == 'method2'):
		method2()
	if(option == 'function'):
		n = raw_input("Enter an integer that's larger than 0:	")
		function(int(n))
	if(option == 'tp'): # To look into later. After this is used, when brought back the 'else' operator is run
		n = raw_input("Enter an integer that's larger than 0:	")
		tp(int(n))
	if(option == 'mp'):
		n = raw_input("Enter an integer that's larger than 0:	")
		mp(int(n))
	if(option == 'auto'):
		n = raw_input("Enter an integer that's larger than 0:	")
		automate(int(n))
	if(option == 'q'):
		exit()
	else:
		print "[!] Not a valid option. Here are the options again"
		inputs()
	

# The main method for the program 
def main():
	inputs()
	
main() # The call to main in order to launch the program 
