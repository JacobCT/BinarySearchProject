#!/bin/bash
#make a list of everything in ao327
rm directorylist.txt
rm for_database.txt
touch for_database.txt
touch directorylist.txt
cd /hyrule/results/ao327/.
ls -1 > /home/jdc0059/BinarySearch/directorylist.txt
sed -ni '/^[5].*/p' /home/jdc0059/BinarySearch/directorylist.txt
sed -i '/.tar.gz/d' /home/jdc0059/BinarySearch/directorylist.txt
sed -i '/singlepulse/d' /home/jdc0059/BinarySearch/directorylist.txt
sed -i '/.tar.gz/d' /home/jdc0059/BinarySearch/subdirlist.txt
sed -i '/candidates/d' /home/jdc0059/BinarySearch/subdirlist.txt                                                                                                        sed -i '/SPfiles/d' /home/jdc0059/BinarySearch/subdirlist.txt                                                                                                           sed -i '/duplicates/d' /home/jdc0059/BinarySearch/subdirlist.txt                                                                                                        sed -i '/for_database/d' /home/jdc0059/BinarySearch/subdirlist.txt
one=1
#Now go through that list and in order to make the pointing list
while IFS='' read -r LINE || [ -n "${LINE}" ]; do
	cd $LINE
	subdircount=$(ls -lR | grep ^d | wc -l)
	echo "subdircount is $subdircount"
	#subdircount=$(find /hyrule/results/ao327/${LINE}/. -maxdepth 1 -type d | wc -l)
	echo "At start:"
	pwd
	if [ "$subdircount" -lt "$one" ]
	then #If no sub directories are found:
		echo "No sub-directories are found"
		pwd
		ls -1  >> /home/jdc0059/BinarySearch/for_database.txt
	else #If more sub directories are found:
		touch /home/jdc0059/BinarySearch/subdirlist.txt
		#cd $LINE
		echo "More sub directories are found Location:"
		pwd
		ls -1 > /home/jdc0059/BinarySearch/subdirlist.txt
		sed -i '/.out/d' /home/jdc0059/BinarySearch/subdirlist.txt
		sed -i '/.tar.gz/d' /home/jdc0059/BinarySearch/subdirlist.txt
		sed -i '/candidates/d' /home/jdc0059/BinarySearch/subdirlist.txt
		sed -i '/SPfiles/d' /home/jdc0059/BinarySearch/subdirlist.txt
		sed -i '/duplicates/d' /home/jdc0059/BinarySearch/subdirlist.txt
		sed -i '/for_database/d' /home/jdc0059/BinarySearch/subdirlist.txt
		sed -i '/singlepulse/d' /home/jdc0059/BinarySearch/subdirlist.txt
		while IFS='' read -r line || [ -n "${line}" ]; do
			cd $line
			echo "Trying to go into those more directories:"
			pwd
			ls -1  >> /home/jdc0059/BinarySearch/for_database.txt
			cd ..
		done < /home/jdc0059/BinarySearch/subdirlist.txt
		rm /home/jdc0059/BinarySearch/subdirlist.txt
	fi
	cd ..
done < /home/jdc0059/BinarySearch/directorylist.txt
#Go back into your directory
cd /home/jdc0059/BinarySearch/
#Format the files so that they are sortable and readable by BinarySearch.py
sed -i 's/[^0-9]//g' for_database.txt
#cut -c8- for_database.txt | sed -e 's/^.\{2\}/&h/' | sed -e 's/^.\{5\}/&m/' | sed -e 's/^.\{8\}/&s/' | sed -e 's/^.\{12\}/&d/' | sed -e 's/^.\{15\}/&m/' | sed "s/+/ /g" > pointings.txt
#sed -e 's/^.\{2\}/&h/' | sed -e 's/^.\{5\}/&m/' | sed -e 's/^.\{8\}/&s/' | sed -e 's/^.\{12\}/&d/' | sed -e 's/^.\{15\}/&m/' | sed "s/+/ /g" for_database.txt
#sed -i 's/^.*D/D/' pointings.txt

#paste pointings.txt for_database.txt > pointingsfolders.txt
#sort -nk1 pointingsfolders.txt > pointingsfolderssortra.txt
#awk '{print $3}' pointingsfolderssortra.txt  > fordatabasesort.txt
#awk '{print $1, $2}' pointingsfolderssortra.txt  > pointingssorted.txt
