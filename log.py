#!/usr/bin/env python
import rrdtool
import time
import utils
import temperature


# constants
graphTimeRange = 43200
loggingInterval = 15

#infinite loop
while (1):	
	try:
		value = 'N:'
		temp = temperature.getValue()
		value += str(temp)
		rrdtool.update('temperature.rrd',value)
		temperature.makePngGraph(graphTimeRange)
		# terminal output
		print ('tempC:'),	
		print (temp),
		utils.printTime()	
	except Exception:
		# terminal output
		print ('tempC: READING FAILED!!'),	
		utils.printTime()		
	           
	time.sleep(loggingInterval)



