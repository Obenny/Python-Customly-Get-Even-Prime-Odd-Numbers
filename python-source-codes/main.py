#!/usr/bin/python

# Copyright (c) Isaac Obenson "(eT. A. M)".
# See LICENSE for details.

import os #for operating system dependent functionality
import playsound #to play notification .mp3 sounds
import time #for delays

#ALL MY FUNCTIONS

#slogo
def logo():
	print "===================================="
	print "===================================="
	print "===================================="
	print "=====                       ========"
	print "===== 3 - S C E N E R I O   ========"
	print "=====                       ========"
	print "===================================="
	print "===================================="
	print "===================================="

#shutdown notification warning
def success_sound():
	playsound.playsound('graceful.mp3', True)

#error notification warning
def error_sound():
	playsound.playsound('system-fault.mp3', True)

#clean function
def clean_screen():
	time.sleep(0.5)  # Delays for 1 second. Can also use float value
	os.system('clear') # clears screen	

#waiting for another client to connect message function
def waiting_message():
	clean_screen()

def box_one(end1):
	print ("\n\nAll the odd numbers\n\n")
	print("1st Box = "), #print on same line
	
	start1=1 #starting interval
	endstart1=end1 #ending interval
  
	# iterating each number in list 
	for num in range(start1, endstart1 + 1): 
      
    		# checking condition 
    		if num % 2 != 0: 
        		print(num), #print on same line

    	print ("\n\n")

def box_two(end2):
	print ("\n\nAll the even numbers.\n\n")
	print("2nd Box = "),
	
	start2=1 #starting interval
	endstart2=end2 #ending interval

	# iterating each number in list 
	for num in range(start2, endstart2 + 1): 
      
    		# checking condition 
    		if num % 2 == 0: 
        		print(num), #print on same line

    	print ("\n\n")

def box_three(end3):
	print ("\n\nAll prime numbers.\n\n")
	print("3rd Box = "),

	start3=1 #starting interval
	endstart3=end3 #ending interval

	for val in range(start3, endstart3 + 1): 
      
   	# If num is divisible by any number   
   	# between 2 and val, it is not prime  
   		if val > 1: 
       			for n in range(2, val): 
           			if (val % n) == 0: 
               				break
       			else:  
           			print(val), #print on same line

    	print ("\n\n")

#checks if is positive number
def check_input():
	while True:
			#call logo fxn
			logo()

			#get input and check if positive
			user_number  = raw_input("\n\nEnter Total Number of Socks\n\n\n==>")

			#checks if value is digit
			if(user_number.isdigit()):
				convert=int(user_number) #convert to integer
				if(convert == 0 or convert == 1):
						print("\n\nUser input MUST be greater than 1\n\n")
							#call error sound function
    						error_sound()

				elif(convert > 1):
    					print("\n\nValid Positive Number")

    					#call success sound function
    					success_sound()

    					#call functions for boxes
    					box_one(convert)
    					time.sleep(2)  # Delays for 2 second.

    					box_two(convert)
    					time.sleep(2)  # Delays for 2 second. 

    					box_three(convert)
    					time.sleep(2)  # Delays for 2 second. 

    					#clear sreen
    					clean_screen()
			else:
    				print("\n\nUser input is NOT a Positive Number")

    				#call error sound function
    				error_sound()

    				#clear sreen
    				clean_screen()

#start main
check_input()