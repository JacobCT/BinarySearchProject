#!/bin/bash
rm for_database_clean.txt
touch for_database_clean.txt
while IFS='' read -r LINE || [ -n "${LINE}" ]; do
	echo $LINE | sed -e 's/^.\{2\}/&h/' | sed -e 's/^.\{5\}/&m/' | sed -e 's/^.\{8\}/&s/' | sed -e 's/^.\{11\}/&d/' | sed -e 's/^.\{14\}/&m/' | sed -e 's/^.\{9\}/&+/' >> for_database_clean.txt
done < /home/jdc0059/BinarySearch/for_database.txt

