#!/usr/bin/env python

# Switch to False when a real Arduino is connected
mock = True

def getValue():
	
	if (mock == False):
		import serial

		ser = serial.Serial('/dev/ttyUSB0', 38400)
		tempstring = ser.readline()
		temp = float(tempstring)
		ser.close()			
	else:
		import random
		temp = random.uniform(20, 27)	
	
	return temp
	
def makePngGraph(graphTimeRange):
	import rrdtool
	import time
	
	# graph temp
	nowUnixTime = int(time.time())
	
	rrdtool.graph('temperature.png',
		            '--start', str(nowUnixTime-graphTimeRange), 
		            '--end', str(nowUnixTime),
		            '--title','Temperature (degrees c)',
		            '--width','800',
          		    'DEF:myspeed=temperature.rrd:temp:AVERAGE',
		            'LINE2:myspeed#FF0000')   
