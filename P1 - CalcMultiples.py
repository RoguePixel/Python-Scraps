#!/bin/env python
#Project Euler - Problem 1

#Create by Rafael L.
#Saturday, Februery 11, 2012

#script to calculate the sum of multiple of 3 and 5 within a range of numerical input
from sys import argv as arg

def numstep(limit=10,a=3,b=5):
	n=0; limit+1
	for i in range(0,limit,a):
		n+=1; num=0; num=i+i; i+=num; i+=5 
		yield "%sth increment is = %s (%s)" % (n,i,num)	

if len(arg)==1:
	print """\n%s Please supply a numerical integer \n\t eg:\n\t %s 100 """ % (arg[0],arg[0])	
else:

	for n in numstep(int(arg[1])):
		print n
	
			
		
	 
