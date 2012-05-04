#!/usr/bin/env python
import rrdtool
import random
import time

while (1):
	value = 'N:'
	temp = random.randrange(17,29)
	value += str(temp)
	rrdtool.update('temperature.rrd',value)
	print temp	
	now = int(time.time())
	range = 240
	rrdtool.graph('output.png',
		            '--start', str(now-range), 
		            '--end', str(now),
				        'DEF:myspeed=temperature.rrd:temp:AVERAGE',
		            'LINE2:myspeed#FF0000')              
	time.sleep(15)
