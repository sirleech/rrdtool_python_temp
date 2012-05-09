#!/usr/bin/env python


##################################################
#
# printTime()
#
# Print the Date/Time in a human readable form
##################################################

def printTime():
	import datetime
	now = datetime.datetime.now()
	print now.strftime("%Y-%m-%d %H:%M")
