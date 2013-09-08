#
#  main.py
#  
#
#  Created by arjo chakravarty on 6/16/11.
#  Copyright (c) 2011 __MyCompanyName__. All rights reserved.
#
import os, sys
import Image
import ImageStat
import math
infile=sys.argv[1]
im = Image.open(infile)
Orange = '\033[93m'
Green = '\033[92m'
Red = '\033[91m'
Blue='\033[94m'
Magenta='\033[95m'
System='\033[0m'
print ""
print "Image Manipulation Applet- Background seperation"
print "<c> Arjo Chakravarty- GNU GPL"
print ""
print "THIS IS DISTRIBUTED WITHOUT ANY WARRANTY"

print "Getting information (this will take time)..."

(x,y)=im.size

x=x-1 #fix x and y for co-ordinate systems
y=y-1

i=0
n=0
sum=0
while (i<x):
	i=i+1
	while (n<y):
		pixel=im.getpixel((i,n))
		intensity=(pixel[0]+pixel[1]+pixel[2])/3
		sum=intensity+sum
		n=n+1
	n=0
	
i=0
n=0
mean=sum/((x+1)*(y+1))# Calculate mean
stat=ImageStat.Stat(im)
deviation=(stat.stddev[0]+stat.stddev[1]+stat.stddev[2])# Standard Deviation for intensity
median=stat.median
med=(median[0]+median[1]+median[2])/3
i=0
n=0
print "\r"+Green+"						[Done]"
print ""
print System+"Writing to file..."
im2=Image.new("RGB",(x+1,y+1))
im3=Image.new("RGB",(x+1,y+1))
# now find out which pixels are bad and enhance the image
while (i<x):
	i=i+1
	while (n<y):
		pixel=im.getpixel((i,n))
		intensity=(pixel[0]+pixel[1]+pixel[2])/3
		v=med-intensity
		if deviation>0:
			error=math.fabs(v/deviation)
			if error>0.1:
				im2.putpixel((i,n),pixel)
			else:
				im3.putpixel((i,n),pixel)
		else:
			print ""+red+"Error: All one colour?"
		n=n+1
	n=0
im2.save(sys.argv[2])
im3.save(sys.argv[3])
print "\r"+Green+"						[Done]"
print System


	