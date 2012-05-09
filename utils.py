#!/usr/bin/env python


##################################################
#
# printTime()
#
# Print the Date/Time in a human readable form
##################################################

def getTimeString():
	import datetime
	now = datetime.datetime.now()
	return now.strftime("%Y-%m-%d %H:%M:%S")

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
