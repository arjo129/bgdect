#
#  line.py
#  
#
#  Created by arjo chakravarty on 6/17/11.
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
print "Image Statistics Applet"
print "<c> Arjo Chakravarty- GNU GPL"
print ""
print "THIS IS DISTRIBUTED WITHOUT ANY WARRANTY"

print "Getting information (this will take time)..."

(x,y)=im.size

x=x-2 #fix x and y for co-ordinate systems
y=y-2
i=1
n=1
print "\r"+Green+"						[Done]"
print ""
print System+"processing..."
im2=Image.new("RGB",(x+1,y+1))
# now find out which pixels are bad and enhance the image
while (i<x):
	k=0
	while (n<y):
		pixel=im.getpixel((i,n))
		pixel1=im.getpixel((i+1,n))
		pixel2=im.getpixel((i-1,n))
		pixel3=im.getpixel((i,n+1))
		pixel4=im.getpixel((i+1,n+1))
		pixel5=im.getpixel((i-1,n+1))
		pixel6=im.getpixel((i+1,n-1))
		pixel7=im.getpixel((i-1,n-1))
		pixel8=im.getpixel((i,n-1))
		intensity=(pixel[0]+pixel[1]+pixel[2])/3
		intensity1=(pixel1[0]+pixel1[1]+pixel1[2])/3
		intensity2=(pixel2[0]+pixel2[1]+pixel2[2])/3
		intensity3=(pixel3[0]+pixel3[1]+pixel3[2])/3
		intensity4=(pixel4[0]+pixel4[1]+pixel4[2])/3
		intensity5=(pixel5[0]+pixel5[1]+pixel5[2])/3
		intensity6=(pixel6[0]+pixel6[1]+pixel6[2])/3
		intensity7=(pixel7[0]+pixel7[1]+pixel7[2])/3
		intensity8=(pixel8[0]+pixel8[1]+pixel8[2])/3
		sum=intensity+intensity2+intensity3+intensity4+intensity5+intensity6+intensity7+intensity8+intensity1
		mean=sum/9
		l=intensity-mean+intensity2-mean+intensity3-mean+intensity4-mean+intensity5-mean+intensity6-mean+intensity7-mean+intensity8-mean+intensity1-mean
		g=[intensity,intensity1,intensity2,intensity3,intensity4,intensity5,intensity6,intensity7,intensity8]
		g.sort()
		median=g[4]
		deviation=math.sqrt(l/9)
		if deviation==0:
			k=1
		else:
			error=math.fabs((median-intensity)/deviation)
			error1=math.fabs((median-intensity1)/deviation)
			error2=math.fabs((median-intensity2)/deviation)
			error3=math.fabs((median-intensity3)/deviation)
			error4=math.fabs((median-intensity4)/deviation)
			error5=math.fabs((median-intensity5)/deviation)
			error6=math.fabs((median-intensity6)/deviation)
			error7=math.fabs((median-intensity7)/deviation)
			error8=math.fabs((median-intensity8)/deviation)
			color=error*165
			color1=error1*165
			color2=error2*165
			color3=error3*165
			color4=error4*165
			color5=error5*165
			color6=error6*165
			color7=error7*165
			color8=error8*165
			im2.putpixel((i,n),(color,color,color))
			im2.putpixel((i+1,n),(color1,color1,color1))
			im2.putpixel((i-1,n),(color2,color2,color2))
			im2.putpixel((i,n+1),(color3,color3,color3))
			im2.putpixel((i+1,n+1),(color4,color4,color4))
			im2.putpixel((i-1,n+1),(color5,color5,color5))
			im2.putpixel((i+1,n-1),(color6,color6,color6))
			im2.putpixel((i-1,n-1),(color7,color7,color7))
			im2.putpixel((i,n+1),(color8,color8,color8))
		n=n+1
	i=i+1	
	n=1
im2.save(sys.argv[2])
print "\r"+Green+"						[Done]"
print System


