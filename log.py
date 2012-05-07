#!/usr/bin/env python
import rrdtool
import random
import time
import datetime

def printTime():
	now = datetime.datetime.now()
	print now.strftime("%Y-%m-%d %H:%M")

while (1):

	now = int(time.time())
	# temperature
	value = 'N:'
	temp = random.uniform(17,29)	
	value += str(temp)
	rrdtool.update('temperature.rrd',value)
	
	# graph temp
	range = 9000
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
	range = 9000
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
	printTime()	
	
	           
	time.sleep(15)



