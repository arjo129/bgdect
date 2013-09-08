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
print ""
print "Image statistics applet"
print "<c> Arjo Chakravarty- GNU GPL"
print "THIS IS DISTRIBUTED WITHOUT ANY WARRANTY"
print "Getting information (this will take time)..."
(x,y)=im.size
print "height:"
print x
print "width:"
print y
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
print "Average intensity calculated"
print mean
overall=0	
while (i<x):
	i=i+1
	while (n<y):
		pixel=im.getpixel((i,n))
		intensity=(pixel[0]+pixel[1]+pixel[2])/3
		difference=intensity-mean
		overall=(difference*difference)+overall
		n=n+1
	n=0
deviation=math.sqrt(overall/((x+1)*(y+1)))# Standard Deviation for intensity
print "standard deviation:"
print deviation
stat=ImageStat.Stat(im)
median=stat.median
print "median"
print (median[0]+median[1]+median[2])/3#intensity median
med=(median[0]+median[1]+median[2])/3
i=0
n=0
im2=Image.new("RGB",(x+1,y+1))
# now find out which pixels are bad and enhance the image
while (i<x):
	i=i+1
	while (n<y):
		pixel=im.getpixel((i,n))
		intensity=(pixel[0]+pixel[1]+pixel[2])/3
		v=med-intensity
		error=math.fabs(v/deviation)
		color=error*75
		im2.putpixel(((i-1),n),(color,color,color))
		
		n=n+1
	n=0
im2.save(sys.argv[2])


	