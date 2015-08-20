#!/usr/local/bin/python3
#
# surlybot.py
#
# This is a simple script that will sing the famount "99 bottles of beer" song
#
# 08/14/2015 - Dan West - Initial Version
#
# Notes
# I just needed something to test Github
#
# Variables
# - variablename - Description
#
# Known Issues/ToDo
# - Finish Writing the Script
# - Get drunker

# Import some modules
import sys, time

# Check for arguments
def arg_check():
    if len(sys.argv) == 2:
        argument = sys.argv[1]
        return argument
    else:
        print("Usage: ./surlybot.py <argument>")
        print("Example: ./surlybot.py 99")
        sys.exit()
        
# Sing the song
def singing(bottle_num):
	bottle_num = bottle_num
	while bottle_num > 0:
		# This is the song
		line1 = str(bottle_num) + " bottles of beer on the wall\n"
		line2 = str(bottle_num) + " bottles of beer\n"
		line3 = "Take one down\n"
		line4 = "Pass it around\n"
		
		# Take a bottle off the wall
		bottle_num -= 1

		# Now there is one less bottle on the wall
		line5 = str(bottle_num) + " bottles of beer on the wall\n\n"

		# This is where the song comes together
		sing_it = line1 + line2 + line3 + line4 + line5

		# Actually sing now
		#print(sing_it)
		print(line1)
		time.sleep(2)
		print(line2)
		time.sleep(2)
		print(line3)
		time.sleep(2)
		print(line4)
		time.sleep(2)
		print(line5)
		time.sleep(3)

# Code goes below here
def main():
	bottle_num = int(arg_check())
	print(bottle_num)
	singing(bottle_num)

# Run the main script
main()
