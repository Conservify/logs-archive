#!/usr/bin/python

import re
import fileinput
import datetime
from dateutil import tz

from_zone = tz.gettz('UTC')
to_zone = tz.gettz('America/New_York')

class TransmissionPhase:
	def __init__(self, time):
		self.time = time

	def transmitted(self, which):
		pass

phase = None
for line in fileinput.input():
	msg = re.match(r'^Message: (\d+),(.+)', line.strip())
	if msg:
		print msg.group(1), msg.group(2)
	tx = re.match(r'^## (\d+).+TX$', line.strip())
	if tx:
		time = datetime.datetime.fromtimestamp(int(tx.group(1))).replace(tzinfo=from_zone)
		phase = TransmissionPhase(time)
	if phase:
		ts = re.match(r'TS: (\d+)', line.strip())
		if ts:
			phase.transmitted(int(ts.group(1)))
