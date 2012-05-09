#!/bin/bash

# create databases

rrdtool create temperature.rrd --step 30 \
  DS:temp:GAUGE:600:-273:5000 \
  RRA:AVERAGE:0.5:1:1200 \
  RRA:MIN:0.5:12:2400 \
  RRA:MAX:0.5:12:2400 \
  RRA:AVERAGE:0.5:12:2400  

# initialise sensors dir and json files  
mkdir sensors
touch sensors/temperature.json

