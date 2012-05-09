#!/usr/bin/env python
import rrdtool
import time
import utils
import temperature


#infinite loop
while (1):
	# 12 hours
	#range = 43200
	range = 1600

	value = 'N:'
	temp = temperature.getValue()
	value += str(temp)
	rrdtool.update('temperature.rrd',value)
	temperature.makePngGraph(range)
	
	# terminal output
	print ('tempC:'),	
	print (temp),
	utils.printTime()	
	
	           
	time.sleep(15)



