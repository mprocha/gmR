#!/bin/bash

file=grid-mR-st3
region=-75/-30/-35/10
scale=1.00/4.6/0.05  # min: 1.07 ; max: 4.54

file=grid-mR-st4
region=-75/-30/-35/10
scale=1.00/4.6/0.05  # min: 1.63 ; max: 4.57

file=grid-mR-st6
region=-75/-30/-35/10
scale=1.00/4.6/0.05 # min: 1.99 ; max: 4.67

xyz2grd /home/marcelo/gmR/$file.txt -G./$file.grd -R$region -I1 -V


makecpt -I -T$scale > /home/marcelo/gmR/$file.cpt
#grd2cpt /home/marcelo/maps/a-grids/$file.grd > ~/maps/a-grids/$file.cpt
 
grdimage /home/marcelo/gmR/$file.grd -JM19 -E300 -C/home/marcelo/gmR/$file.cpt > $file-quick.ps
psscale -C/home/marcelo/gmR/$file.cpt -D5.5i/2.00i/2.00i/0.3i -Ba0.2f0.1:"Magnitudes Values":  -O -E -K >> $file-quick.ps
#grdcontour /home/marcelo/gmR/$file.grd -JM19 -C/home/marcelo/gmR/$file.cpt > $file-quick.ps
gv $file-quick.ps&
