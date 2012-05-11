#!/usr/bin/env python
import time
import utils
import temperature
import serial


# constants
oneWeek =  604800
twelveHours = 43200
twoHours = 7200

# settings
loggingInterval = 30 #aka 'step'
filterBracket = 5	

# vars
lastTemp = 0


#infinite loop
while (1):	
	try:
		temp = temperature.getValue()
		
		# filter the readings with a specified degrees c bracket
		if (temp > lastTemp + filterBracket or temp < lastTemp - filterBracket):
			print 'EXTRANEOUS READING! Reading is greater or less than',filterBracket,'degrees of the previous reading.'
		else:	
			utils.logDataPoint("temperature.rrd",temp)
			
		# export the graphs, json
		temperature.makePngGraph('Temp C 12 Hours',twelveHours,'web/temperature-12hrs.png')
		temperature.makePngGraph('Temp C 2 Hours',twoHours,'web/temperature-2hrs.png')
		temperature.makePngGraph('Temp C 1 Week',oneWeek,'web/temperature-1wk.png')
		temperature.exportToJson(temp)
		
		# terminal output
		print utils.getTimeString(),'| tempC:',temp
		
		# store the last temperature reading
		lastTemp = temp
		
	except Exception as e:
		# terminal output
		print utils.getTimeString(), e
	
	# sleep
	time.sleep(loggingInterval)

		
	           
	



