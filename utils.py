#!/usr/bin/env python

import datetime

def printTime():
	now = datetime.datetime.now()
	print now.strftime("%Y-%m-%d %H:%M")
