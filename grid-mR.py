#!/usr/bin/python

from optparse import OptionParser

# Usage string:
use = "Usage: grid-mR.py --minlat --minlat --minlat --minlat --inc --vel --stanum"
desc = """Program to generate a grid of mR magnitudes from a station array                                        
V1.0 04/04/2015 - M. Rocha                                                          

Script generate a file (grid-mR.txt) with the follow rows:                                            
                                                                                          
latitude longitude magnitude_mR
                                                                                                  
 
ex:                                                                                

grid-mR.py --minlat --minlat --minlat --minlat --inc --vel --stanum                                                        
                                                                                           

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
parser.add_option("--stanum", dest="stanum", type = float, help="Number of stations used in calculation")

# The final step is to parse the options and arguments into variables we can use later:
opts, args = parser.parse_args()

# Making sure all mandatory options appeared:
mandatories = ["minlat", "maxlat", "minlon", "maxlon"]
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

for lat in my_range(minlat, maxlat, inc):
    for lon in my_range(minlon, maxlon, inc):
        print lat,lon






