#!/usr/bin/env python
import rrdtool
import random
import time
import serial
import utils


while (1):
	# 12 hours
	range = 43200

	now = int(time.time())
	# temperature
	#ser = serial.Serial('/dev/ttyUSB0', 38400)
	#tempstring = ser.readline()
	value = 'N:'
	#temp = float(tempstring)
	#ser.close()	
	
	temp = 26
	value += str(temp)
	rrdtool.update('temperature.rrd',value)
	
	# graph temp
	rrdtool.graph('temperature.png',
		            '--start', str(now-range), 
		            '--end', str(now),
		            '--title','Temperature (degrees c)',
		            '--width','800',
          		    'DEF:myspeed=temperature.rrd:temp:AVERAGE',
		            'LINE2:myspeed#FF0000')   
	
	# pH
	value = 'N:'
	pH = random.uniform(7,8)	
	value += str(pH)
	rrdtool.update('ph.rrd',value)
	
	# graph pH
	rrdtool.graph('pH.png',
		            '--start', str(now-range), 
		            '--end', str(now),
		            '--title','pH',
		            '--width','800',
          		    'DEF:myspeed=ph.rrd:temp:AVERAGE',
		            'LINE2:myspeed#FF0000')  
	
	# terminal output
	print ('tempC:'),	
	print (temp),
	print ('pH:'),	
	print (pH),
	utils.printTime()	
	
	           
	time.sleep(15)



