#!/usr/bin/python

import re
import fileinput
import datetime
from dateutil import tz

from_zone = tz.gettz('UTC')
to_zone = tz.gettz('America/New_York')

for line in fileinput.input():
	if re.match(r'^##', line):
		fields = line.strip().split(' ')
		time_utc = datetime.datetime.fromtimestamp(int(fields[1])).replace(tzinfo=from_zone)
		time_local = time_utc.astimezone(to_zone)
		if len(fields) == 8:
			print ','.join([ time_local.strftime('%s'), fields[6] ])
		else:
			print ','.join([ time_local.strftime('%s'), fields[5] ])
