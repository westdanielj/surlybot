#!/usr/local/bin/python3
#
# surlybot.py
#
# This is a simple script that will sing the famous "99 bottles of beer" song.  It will default to starting with
# 99 bottles of beer, but you can add optional arguments for changing the beverage type and starting number.
#
# 08/14/2015 - Dan West - Initial Version
# 08/21/2015 - Dan West - Added optional arguments for specifying the beverage type and number to start with
# 09/02/2015 - Dan West - Added a list and loop for the lyrics
#
# Notes
# I just needed something to test Github
#
# Known Issues/ToDo
# - Finish Writing the Script
# - Get drunker

# Import some modules
import sys, time, argparse

# Check for arguments
def arg_check():
    parser = argparse.ArgumentParser(prog='surlybot.py')
    parser.add_argument('-b', '--beverage', default='beer', required=False, action='store', dest='bev_type', help='Requires a valid beverage')
    parser.add_argument('-n', '--number', default='5', required=False, action='store', dest='bottle_num', help='Requires a number greater than 0')
    args = vars(parser.parse_args())
    bev_type = str(args['bev_type'])
    bottle_num = int(args['bottle_num'])
    return bev_type, bottle_num

# Beer printer
def beer_printer(bottle_num):
	mug_icon = u"\U0001F37A".encode('utf-8')
	mugs = ""
	for count in range(bottle_num):
		mugs += str(mug_icon) + " "
	print(mugs)

# Sing the song
def singing(bev_type, bottle_num):
	bev_type = bev_type
	bottle_num = bottle_num
	while bottle_num > 0:
		
		# Print bottles remaining
		beer_printer(bottle_num)

		# Add lyrics to each verse
		verse = []
		verse.append(str(bottle_num) + " bottles of " + str(bev_type) + " on the wall\n")
		verse.append(str(bottle_num) + " bottles of " + str(bev_type) + "\n")
		verse.append("Take one down\n")
		verse.append("Pass it around\n")
		
		# Take a bottle off the wall
		bottle_num -= 1
		
		# Now there is one less bottle on the wall
		verse.append(str(bottle_num) + " bottles of " + str(bev_type) + " on the wall\n")
		
		# Actually sing now
		for line in verse:
			print(line)
			time.sleep(2)	
		time.sleep(1)

# Main Function
def main():
	# Check optional arguments
	bev_type, bottle_num = arg_check()

	# Start singing the song
	singing(bev_type, bottle_num)
	
	# Congrats message
	print("Congratulations, you are now drunk.")
# Run the main script
main()
