#!/usr/bin env python
from sys import argv as arg

def fib(value):
	num=0; x=1; y=1; a=0
	while num<=int(value):	
		a=x+y; x=y; y=a	
		num+=1
		if (a % 2)!=1:
			yield a

if len(arg)==1:
	print "please input a numerical value when executing %s" % arg[0]
else:

	for i in fib(arg[1]):
		print i
