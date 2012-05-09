#!/usr/bin/env python
import time
import utils
import temperature
import serial


# constants
graphTimeRange = 43200
loggingInterval = 15

#infinite loop
while (1):	
	try:
		value = 'N:'
		temp = temperature.getValue()
		utils.logDataPoint("temperature.rrd",temp)
		temperature.makePngGraph(graphTimeRange)
		
		# terminal output
		print utils.getTimeString(),'| tempC:',temp
		
		
	except serial.SerialException as e:
		# terminal output
		print utils.getTimeString(),'| tempC: SERIAL PORT NOT AVAILABLE', e
		
	           
	time.sleep(loggingInterval)



