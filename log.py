#!/usr/bin/env python
import rrdtool
import random
import time
import datetime

def printTime():
	now = datetime.datetime.now()
	print now.strftime("%Y-%m-%d %H:%M")

while (1):
	#this is a special letter for "now" in UNIX time
	value = 'N:'
	
	# insert your temp reading here
	temp = random.randrange(17,29)	
	value += str(temp)
	rrdtool.update('temperature.rrd',value)
	print ('tempC:'),	
	print (temp),
	printTime()	
	now = int(time.time())
	
	# show 15 minutes
	range = 9000
	rrdtool.graph('output.png',
		            '--start', str(now-range), 
		            '--end', str(now),
          		    'DEF:myspeed=temperature.rrd:temp:AVERAGE',
		            'LINE2:myspeed#FF0000')              
	time.sleep(15)



