#!/usr/bin/env python

import rrdtool
import time


now = int(time.time())
range = 240

rrdtool.graph('output.png',
              '--start', str(now-range), 
              '--end', str(now),
		          'DEF:myspeed=temperature.rrd:temp:AVERAGE',
              'LINE2:myspeed#FF0000')

