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

##################################################
#
# logDataPoint(databaseName,value)
#
# Log one data point with a time of "now"
# into a specified round-robin database
##################################################
	
def logDataPoint(databaseName,value):
		import rrdtool
		logValue = 'N:'
		logValue += str(value)
		rrdtool.update(databaseName,logValue)
