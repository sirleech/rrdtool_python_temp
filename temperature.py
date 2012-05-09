#!/usr/bin/env python

# Switch to False when a real Arduino is connected
mock = False

def getSerialSensorValue():
		import serial
		ser = serial.Serial('/dev/ttyUSB0', 38400)
		valueString = ser.readline()
		ser.close()		
		return float(valueString)

def getValue():
	
	if (mock == False):
		temp = getSerialSensorValue()				
	else:
		import random
		temp = random.uniform(20, 27)	
	
	return temp
	
def exportToJson(temperature):
	import utils
	import json
	f = open('sensors/temperature.json','w')
	reading = {
							'unit':'degrees celcius',
							'unitPrefix':'&deg;C',
							'value': temperature, 
							'lastUpdated': utils.getTimeString()
						}
	f.write(json.dumps(reading))
	f.close()
	
def makePngGraph(graphTimeRange,outfile):
	import rrdtool
	import time
	
	# graph temp
	nowUnixTime = int(time.time())
	
	rrdtool.graph(outfile,
		            '--start', str(nowUnixTime-graphTimeRange), 
		            '--end', str(nowUnixTime),
		            '--title','Temperature (degrees c)',
		            '--width','700',
          		    'DEF:myspeed=temperature.rrd:temp:AVERAGE',
		            'LINE2:myspeed#FF0000')   
