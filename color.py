#
#  color.py
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
bright=125 # user set
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
sum=0,0,0
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
mean=sum[0]/(x+1)*(y+1), sum[1]/(x+1)*(y+1), sum[2]/(x+1)*(y+1)# Calculate mean
print "Average intensity calculated"
print mean
overall=0,0,0	
while (i<x):
	i=i+1
	while (n<y):
		pixel=im.getpixel((i,n))
		intensity=pixel
		difference=intensity[0]-mean[0],intensity[1]-mean[1],intensity[2]-mean[2]
		overall=(difference[0]*difference[0])+overall[0], (difference[1]*difference[1])+overall[1], (difference[2]*difference[2])+overall[2]
		n=n+1
	n=0
deviation=math.sqrt(overall[0]/((x+1)*(y+1))), math.sqrt(overall[1]/((x+1)*(y+1))), math.sqrt(overall[2]/((x+1)*(y+1)))# Standard Deviation for intensity
print "standard deviation:"
print deviation
stat=ImageStat.Stat(im)
median=stat.median
print "median"
print median#intensity median
med=median
i=0
n=0
im2=Image.new("RGB",(x+1,y+1))
# now find out which pixels are bad and enhance the image
while (i<x):
	i=i+1
	while (n<y):
		pixel=im.getpixel((i,n))
		intensity=pixel
		v=med[0]-intensity[0], med[1]-intensity[1], med[2]-intensity[2]
		error=math.fabs(v[0]/deviation[0]),math.fabs(v[1]/deviation[1]),math.fabs(v[2]/deviation[2])
		color=error[0]*bright, error[1]*bright, error[2]*bright
		im2.putpixel(((i-1),n),color)
		
		n=n+1
	n=0
im2.save(sys.argv[2])


	