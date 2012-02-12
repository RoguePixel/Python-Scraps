#!/bin/env python
from sys import argv as arg

def divisor(value):
	for n in range(1,100000):
		if value % n!=1:
			yield n	

def primediv(value):
	for n in range(1,100000):
		if value % n!=1:
				if n % 2 !=0:
					yield n	
	
# for a in divisor(int(arg[1])):
# 	print "\t%s" % a
		
for b in primediv(int(arg[1])):
	print b