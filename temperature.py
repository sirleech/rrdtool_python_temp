#!/usr/bin/env python

import serial
import rrdtool
import time

mock = True

def getValue():
	
	if (mock == False):
		ser = serial.Serial('/dev/ttyUSB0', 38400)
		tempstring = ser.readline()
		temp = float(tempstring)
		ser.close()	
	else:
		temp = 26	
	
	return temp
	
def makePngGraph(range):
	# graph temp
	nowUnixTime = int(time.time())
	
	rrdtool.graph('temperature.png',
		            '--start', str(nowUnixTime-range), 
		            '--end', str(nowUnixTime),
		            '--title','Temperature (degrees c)',
		            '--width','800',
          		    'DEF:myspeed=temperature.rrd:temp:AVERAGE',
		            'LINE2:myspeed#FF0000')   
