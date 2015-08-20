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
import sys, time, argparse

# Check for arguments
def arg_check():
    parser = argparse.ArgumentParser(prog='surlybot.py')
    parser.add_argument('-b', '--beverage', required=False, action='store', dest='bev_type', help='Requires a valid beverage')
    parser.add_argument('-n', '--number', required=False, action='store', dest='bottle_num', help='Requires a number greater than 0')
    args = vars(parser.parse_args())
    bev_type = args['bev_type']
    bottle_num = args['bottle_num']
    return bev_type, bottle_num

# Sing the song
def singing(bev_type, bottle_num):
	bev_type = bev_type
	bottle_num = bottle_num
	while bottle_num > 0:
		# This is the song
		line1 = str(bottle_num) + " bottles of " + str(bev_type) + " on the wall\n"
		line2 = str(bottle_num) + " bottles of " + str(bev_type) + "\n"
		line3 = "Take one down\n"
		line4 = "Pass it around\n"
		
		# Take a bottle off the wall
		bottle_num -= 1

		# Now there is one less bottle on the wall
		line5 = str(bottle_num) + " bottles of " + str(bev_type) + " on the wall\n\n"

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
	bev_type, bottle_num = int(arg_check())
	singing(bev_type, bottle_num)

# Run the main script
main()
