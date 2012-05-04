#!/usr/bin/env python
#rrdtool update temperature.rrd  N:26

import rrdtool
rrdtool.update('temperature.rrd','N:22')
