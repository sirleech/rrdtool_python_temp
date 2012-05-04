#!/bin/bash

rrdtool create temperature.rrd --step 1 \
  DS:temp:GAUGE:600:-273:5000 \
  RRA:AVERAGE:0.5:1:1200 \
  RRA:MIN:0.5:12:2400 \
  RRA:MAX:0.5:12:2400 \
  RRA:AVERAGE:0.5:12:2400