#!/usr/bin/python

import sys
import numpy as np
from astropy import units as u
from astropy.coordinates import SkyCoord

fromcat = []
pntsrt = []


file = open('fromcat.txt', 'r+')
for line in file:
	fromcat.append(line)
	
fromcat = [s.replace('h', '') for s in fromcat]
fromcat = [s.replace('m', '') for s in fromcat]
fromcat = [s.replace('s', '') for s in fromcat]
fromcat = [s.replace('+', '') for s in fromcat]
fromcat = [s.replace('d', '') for s in fromcat]
fromcat = [s.replace('\t', '') for s in fromcat]
fromcat = [s.replace('\n', '') for s in fromcat]


file2 = open('pointingssorted.txt', 'r+')
for line in file2:
        pntsrt.append(line)
        

pntsrt  = [s.replace('h', '') for s in pntsrt]
pntsrt = [s.replace('m', '') for s in pntsrt]
pntsrt = [s.replace('s', '') for s in pntsrt]
pntsrt = [s.replace('+', '') for s in pntsrt]
pntsrt  = [s.replace('d', '') for s in pntsrt]
pntsrt = [s.replace('\t', '') for s in pntsrt]
pntsrt = [s.replace('\n', '') for s in pntsrt]
pntsrt = [s.replace(' ', '') for s in pntsrt]   


#print(fromcat)
#print(pntsrt)

#Pulsar that you are searching for with RA and DEC only in numbers:
x = '0435002749'   #'0436032745'

l =  0
r =  len(pntsrt)-1  #is this ok?
tempx = int(x) - 100
tempx2 = int(x) + 101
xarr =  [tempx]
for i in range(0,10010000, 10000):
	for j in range(0,11,1):
		xarr.append(tempx+(i+j))
		xarr.append(tempx-(i+j))
#print(xarr)
 #Iterative Binary Search Function 
# It returns location of x in given array arr if present, 
# else returns -1 
def binarySearch(arr, l, r, x, xarr): 
  
    while l <= r: 
  
        mid = l + (r-l)/2;

        # Check if x is present at mid 
        if int(arr[mid]) in xarr: 
            print(arr[mid]) 
  	    arr.remove(arr[mid])
	    binarySearch(pntsrt, l, r, x, xarr)

        # If x is greater, ignore left half 
        elif int(arr[mid]) < int(x): 
            l = mid + 1
  
        # If x is smaller ignore right half 
        else: 
            r = mid - 1
      
    # If we reach here, then the element was not present 
    return -1

#print(len(pntsrt))

print(binarySearch(pntsrt, l, r, x, xarr))

file.close()
file2.close()
