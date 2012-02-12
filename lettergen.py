#!/usr/bin/ env python
from sys import argv as arg
import string

#generate aphanumerical sequence
def lettergen():
	for char in range(1,27):
			yield chr(char+96)

#generate sum of alphanumeric input
def numgen(words):
	wordsum=0
	for w in str(words):
		wordsum+=ord(w)-96
	return "%s\t %s" % (words,wordsum)

if len(arg)!=1:
	print "%s requires alphanumeric input at runtime\n\t eg: %s hello"

for word in arg[1:]:
	print numgen(word)
			

