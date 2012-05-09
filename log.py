#!/usr/bin/env python
import time
import utils
import temperature
import serial


# constants
oneWeek =  604800
twelveHours = 43200
twoHours = 7200
loggingInterval = 15

#infinite loop
while (1):	
	try:
		value = 'N:'
		temp = temperature.getValue()
		utils.logDataPoint("temperature.rrd",temp)
		temperature.makePngGraph(twelveHours,'web/temperature-12hrs.png')
		temperature.makePngGraph(twoHours,'web/temperature-2hrs.png')
		temperature.makePngGraph(oneWeek,'web/temperature-1wk.png')
		
		# terminal output
		print utils.getTimeString(),'| tempC:',temp
		
	except Exception as e:
		# terminal output
		print utils.getTimeString(), e
	
	# sleep
	time.sleep(loggingInterval)

		
	           
	



