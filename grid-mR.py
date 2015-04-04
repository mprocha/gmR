#!/usr/bin/python

from optparse import OptionParser
import math

# Usage string:
use = "Usage: grid-mR.py --minlat --minlat --minlat --minlat --inc --vel --stanum"
desc = """Program to generate a grid of mR magnitudes from a station array                                        
V1.0 04/04/2015 - M. Rocha                                                          

Script generate a file (grid-mR.txt) with the follow rows:                                            
                                                                                          
latitude longitude magnitude_mR
                                                                                                  
 
ex:                                                                                

grid-mR.py --minlat -25 --maxlat -2.0 --minlon -54 --maxlon -34 --inc 0.5 --vel 0.1182 --stanum 3

                                                                
"""

# Calling Parser:
parser = OptionParser(usage = use, description = desc)

# Prog options:

parser.add_option("--minlat", dest="minlat", type = float, help="Minimum Latitude (deg)")
parser.add_option("--maxlat", dest="maxlat", type = float, help="Maximum Latitude (deg)")
parser.add_option("--minlon", dest="minlon", type = float, help="Minimum Longitude (deg)")
parser.add_option("--maxlon", dest="maxlon", type = float, help="Maximum Longitude (deg)")
parser.add_option("--inc",    dest="inc",    type = float, help="Increment (deg) - grid spacing")
parser.add_option("--vel",    dest="vel",    type = float, help="Ground Velocity in nm/s")
parser.add_option("--stanum", dest="stanum", type = int,   help="Number of stations used in calculation", default=3)

# The final step is to parse the options and arguments into variables we can use later:
opts, args = parser.parse_args()

# Making sure all mandatory options appeared:
mandatories = ["minlat", "maxlat", "minlon", "maxlon", "inc", "vel", "stanum"]
for m in mandatories:
    if not opts.__dict__[m]:
        print "\n\n\nMANDATORY OPTION IS MISSING\n\n\n"
        parser.print_help()
        exit(-1)

# Setting up Vars...
minlat = opts.minlat
maxlat = opts.maxlat
minlon = opts.minlon
maxlon = opts.maxlon
inc = opts.inc
vel = opts.vel
stanum = opts.stanum

#print "MINLAT= "+minlat+"  MAXLAT= "+maxlat+"  MINLON= "+minlon+"  MAXLON= "+maxlon

def my_range(start, end, step):
    while start <= end:
        yield start
        start += step
fileout="grid-mR-st"+str(stanum)+".txt"
out=open(fileout, 'w')

for elat in my_range(minlat, maxlat, inc):
    elatr=math.radians(elat)
    ecolat=90-elat
    ecolatr=math.radians(ecolat)
    for elon in my_range(minlon, maxlon, inc):
        elonr=math.radians(elon)
        ldist=[]
        lmr=[]
        for file in open('sta.txt','r').readlines():
            slat=float(file[0:10])
            slatr=math.radians(slat)
            scolat=90-slat
            scolatr=math.radians(scolat)
            slon=float(file[11:21])
            slonr=math.radians(slon)
            selev=float(file[22:28])
            scode=file[29:33]
        
            dist=6371*math.acos((math.cos(ecolatr)*math.cos(scolatr))+(math.sin(ecolatr)*math.sin(scolatr)*math.cos(elonr-slonr)))
            mr=math.log10(vel)+(2.3*math.log10(dist))-2.28

            ldist.append(dist)
            lmr.append(mr)

#            print elat,elon,slat,slon,dist,mr

#        print ldist
        slmr=sorted(lmr)
        mmr=slmr[stanum-1]
#        print elat,elon,mmr
        print("%4.2f %3.2f %3.2f" % (elon,elat,mmr))
        out.write("%4.2f %3.2f %3.2f \n" % (elon,elat,mmr)) 

out.close() 
