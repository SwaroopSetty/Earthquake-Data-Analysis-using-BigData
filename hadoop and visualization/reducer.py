#!/usr/bin/python

import sys

janTotal = 0
febTotal = 0
marTotal = 0
aprTotal = 0
mayTotal = 0
junTotal = 0
julTotal = 0
augTotal = 0
sepTotal = 0
octTotal = 0
novTotal = 0
decTotal = 0
oldKey = None
place = None
count = 0
low = 30.0
high = 60.0
# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

print "place,jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec"
infile = sys.stdin
next(infile) 
for line in infile:

    data = line.strip().split("\t")
    if len(data) != 13:
        # Something has gone wrong. Skip this line.
        continue

    place,jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec = data

    # Initially there is nothing in oldkey and it fails. Hence this condition is skipped for first time.
    # Condition changes only when new store is read.

    if oldKey == place:
        try:
        	if (jan == '-9999.9' or feb == '-9999.9' or mar == '-9999.9' or apr == '-9999.9' or may == '-9999.9' or jun == '-9999.9' or jul == '-9999.9' or aug == '-9999.9' or sep == '-9999.9' or oct == '-9999.9' or nov == '-9999.9' or dec == '-9999.9'):
		        continue
		    else:
		        janTotal += float(jan)
		        febTotal += float(feb)
		        marTotal += float(mar)
		        aprTotal += float(apr)
		        mayTotal += float(may)
		        junTotal += float(jun)
		        julTotal += float(jul)
		        augTotal += float(aug)
		        sepTotal += float(sep)
		        octTotal += float(oct)
		        novTotal += float(nov)
		        decTotal += float(dec)
		        count = count +1
        except ValueError,e:
        	print "error",e,"on line",line
    else:
    	if oldKey:
    		print '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s'%(oldKey,janTotal/count,febTotal/count,marTotal/count,aprTotal/count,mayTotal/count,junTotal/count,julTotal/count,augTotal/count,sepTotal/count,octTotal/count,novTotal/count,decTotal/count )
    	oldKey = place
    	try:
    		if (jan == '-9999.9' or feb == '-9999.9' or mar == '-9999.9' or apr == '-9999.9' or may == '-9999.9' or jun == '-9999.9' or jul == '-9999.9' or aug == '-9999.9' or sep == '-9999.9' or oct == '-9999.9' or nov == '-9999.9' or dec == '-9999.9'):
		    	continue
		    else:
		    	janTotal = 0+float(jan)
		        febTotal = 0+float(feb)
		        marTotal = 0+float(mar)
		        aprTotal = 0+float(apr)
		        mayTotal = 0+float(may)
		        junTotal = 0+float(jun)
		        julTotal = 0+float(jul)
		        augTotal = 0+float(aug)
		        sepTotal = 0+float(sep)
		        octTotal = 0+float(oct)
		        novTotal = 0+float(nov)
		        decTotal = 0+float(dec)
		        count  = 1
        except ValueError,e:
        	print "error",e,"on line",line
#For Last line of record
if place == oldKey:
	print '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s'%(oldKey,janTotal/count,febTotal/count,marTotal/count,aprTotal/count,mayTotal/count,junTotal/count,julTotal/count,augTotal/count,sepTotal/count,octTotal/count,novTotal/count,decTotal/count )