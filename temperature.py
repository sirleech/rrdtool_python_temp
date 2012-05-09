#!/usr/bin/env python

# Switch to False when a real Arduino is connected
mock = True

def exportToJson(temperature):
	import json
	import utils
	f = open('sensors/temperature.json','r+')
	string = '{"temperature":"' + str(temperature) + '","lastUpdated":' + '"' + utils.getTimeString() + '"}'
	f.write(string)
	f.close()

def getValue():
	
	if (mock == False):
		import serial
		trycount = 0
		read = False
		
		# try to read the serial port 5 times in a row
		tryAttempts = 5
		while (read == False & trycount <= tryAttempts):
				try:
					ser = serial.Serial('/dev/ttyUSB0', 38400)
					tempstring = ser.readline()
					temp = float(tempstring)
					exportToJson(temp)
					ser.close()
					read = True	
				except serial.SerialException as e:
					if (trycount >= tryAttempts):
						raise e
					import time
					time.sleep(1)					
				
				trycount = trycount + 1
				
	else:
		import random
		temp = random.uniform(20, 27)	
		exportToJson(temp)
	
	return temp
	
def makePngGraph(graphTimeRange,outfile):
	import rrdtool
	import time
	
	# graph temp
	nowUnixTime = int(time.time())
	
	rrdtool.graph(outfile,
		            '--start', str(nowUnixTime-graphTimeRange), 
		            '--end', str(nowUnixTime),
		            '--title','Temperature (degrees c)',
		            '--width','800',
          		    'DEF:myspeed=temperature.rrd:temp:AVERAGE',
		            'LINE2:myspeed#FF0000')   
