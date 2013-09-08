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
print "Image Manipulation Applet- Chakravarty Transform"
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
		intensity=pixel
		sum=intensity+sum
		n=n+1
	n=0
	
i=0
n=0
mean=sum/((x+1)*(y+1))# Calculate mean

stat=ImageStat.Stat(im)
deviation=stat.stddev[0]# Standard Deviation for intensity


median=stat.median[0]
med=median
i=0
n=0
print "\r"+Green+"						[Done]"
print ""
print System+"Writing to file..."
im2=Image.new("RGB",(x+1,y+1))
# now find out which pixels are bad and enhance the image
while (i<x):
	i=i+1
	while (n<y):
		pixel=im.getpixel((i,n))
		intensity=pixel
		v=med-intensity
		error=math.fabs(v/deviation)
		color=error*25
		im2.putpixel(((i-1),n),(color,color,color))
		n=n+1
	n=0
im2.save(sys.argv[2])
print "\r"+Green+"						[Done]"
print System


	