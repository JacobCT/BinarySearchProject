#!/bin/bash
#Before running this script, make sure the pulsars are all formatted correctly. (Ra: 00h00m00s, Dec: 00d00m00s)

while read p; do
	sed 's/\(.*\).../\1/' >> fromcatclean.txt
done <fromcat.txt
	
	
