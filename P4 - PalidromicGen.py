#!/bin/env python
#999x999=998001 (six digits)
a=0; b=0; n=0; nplace=0
numref={}
numlist=[]
#limit 997
def numgen(value=100):
	for n in range(0,value):
		n+=1; a=n; b=n; p=a*b
		yield p

for n in numgen():
	numlist.append(n)

print(numlist)
# if len(str(p))>=4:
# 			numlist.append(p)
# 		return numlist
		
