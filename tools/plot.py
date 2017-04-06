#!/usr/bin/python

import re
import fileinput
import datetime
from dateutil import tz

station = False
battery = None
from_zone = tz.gettz('UTC')
to_zone = tz.gettz('America/New_York')
was_transmitting = transmitting = False

for line in fileinput.input():
	if re.match(r'WS: off', line):
		station = False
	if re.match(r'WS: hup', line):
		station = True
	if re.match(r'^##', line):
		fields = line.strip().split(' ')
		time_utc = datetime.datetime.fromtimestamp(int(fields[1])).replace(tzinfo=from_zone)
		time_local = time_utc.astimezone(to_zone)
		transmitting = re.match(r'.+TX.*', line.strip())
		print ','.join([ time_local.strftime('%s'), fields[5], "1" if station else "0", "1" if transmitting or was_transmitting else "0" ])
		was_transmitting = transmitting
