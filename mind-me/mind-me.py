#!/usr/bin/env python2

import random
import time

i = 0;

while True:
	
	print "Chalenge :",i
	print "Add"
	print ""

	no1 = int(random.random()*100)
	no2 = int(random.random()*100)

	while(no1 == 0 or no2 == 0 or no1 < 10 or no2 < 10):
		no1 = int(random.random()*100)
		no2 = int(random.random()*100)

	print str(no1)+"+"+str(no2)+"?"

	start = time.time()

	raw_input("Push Me")
	stop = time.time()

	print ""
	print"Answer is "+str(no1+no2)
	print "You finised in "+str(int(stop-start))+" seconds"
	i = i+1