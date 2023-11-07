#!/usr/bin/python

import sys
import numpy as np
from astropy import units as u
from astropy.coordinates import SkyCoord
import gcircBS as gcirc
from psrqpy import QueryATNF

fromcatoriginal = []
pntsrt = []
frdata = []

file = open('fromcatclean.txt', 'r+')
for line in file:
	fromcatoriginal.append(line)

fromcat = [sub[ : -4] for sub in fromcatoriginal]
	
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
        

pntsrt = [s.replace('h', '') for s in pntsrt]
pntsrt = [s.replace('m', '') for s in pntsrt]
pntsrt = [s.replace('s', '') for s in pntsrt]
pntsrt = [s.replace('+', '') for s in pntsrt]
pntsrt = [s.replace('d', '') for s in pntsrt]
pntsrt = [s.replace('\t', '') for s in pntsrt]
pntsrt = [s.replace('\n', '') for s in pntsrt]
pntsrt = [s.replace(' ', '') for s in pntsrt]

file3 = open('fordatabasesort.txt', 'r+')
for line in file3:
	frdata.append(line)

#print(fromcat)
#print(len(pntsrt))

#Pulsar that you are searching for with RA and DEC only in numbers:
plsr = '0435002749'   #'0435002749'
#print("Information of Pulsar Searched for: ")
#xplsr = plsr[:4] + plsr[6:]
#xpsrcat = xplsr[:4] + '+' + xplsr[4:]
#xpsrcat = "J" + xpsrcat
#print("For pulsar: " + xpsrcat)
#query = QueryATNF(params=['JNAME', 'DM', 'P0'], psrs=[xpsrcat], include_errs=False)
#print(query.table)

l =  0
r =  len(pntsrt)-1
tempx = int(plsr)
xarr = [tempx]
for i in range(0,10010000, 10000):
	for j in range(0,11,1):
		xarr.append(tempx+(i+j))
		xarr.append(tempx-(i+j))
#print(xarr)

def binarySearch(arr, l, r, x, p): 
  
   	while l <= r: 
  
        	mid = int(l + (r - l) // 2); 
          
        	# Check if x is present at mid 
        	if int(arr[mid]) == x:
			z = arr[mid]
        		zfull = z[:2] + 'h' + z[2:2] + z[2:4] + 'm' + z[4:4] + z[4:6] + 's+' + z[6:6] + z[6:8] + 'd' + z[8:8] + z[8:10] + 'm' + z[10:10]
            		zsplit=zfull.split('+')
            		rapnt = zsplit[0]
            		decpnt = zsplit[1]
            		decpnt = decpnt[:0] + '+' + decpnt[0:]
			
            		pfull = p[:2] + 'h' + p[2:2] + p[2:4] + 'm' + p[4:4] + p[4:6] + 's+' + p[6:6] + p[6:8] + 'd' + p[8:8] + p[8:10] + 'm' + p[10:10]
            		psplit = pfull.split('+')

 
            		racat = psplit[0]
            		deccat = psplit[1]
            		deccat = deccat[:0] + '+' + deccat[0:]
            		zplus = z[:6] + '+' + z[6:]
            		#print(zplus)
            		#print(zfull)
			#print(zfull2)
			#print("deccat: " + deccat)
			#print("racat: " + racat)
			#print("decpnt: " + decpnt)
			#print("rapnt: " + rapnt)

            		print('\nPointing RA: ' + rapnt + ' DEC: ' + decpnt)
            		gcirc.gcirc(racat, deccat, rapnt, decpnt)
            		#print(sep)
            		for s in frdata:
                		if zplus in s:
                    			print('Corresponding Directory in /for_database: \n' + s + '\n') 
            		return arr[mid] 
  
       		# If x is greater, ignore left half 
        	elif int(arr[mid]) < x: 
            		l = mid + 1
  
        	# If x is smaller, ignore right half 
        	else: 
            		r = mid - 1
      
    	# If we reach here, then the element 
    	# was not present 
    	return -1

for xvar in xarr:
	# Function call 
	result = binarySearch(pntsrt, l, r, xvar, plsr) 
  
	#if result != -1: 
    	#	print ("Pointing Detected: " + str(result))  

  
 #Iterative Binary Search Function 
# It returns location of x in given array arr if present, 
# else returns -1 

#print(binarySearch(pntsrt, l, r, x, xarr))

file.close()
file2.close()
