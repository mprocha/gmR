#!/bin/bash

gmtset MEASURE_UNIT cm  ; gmtset ANOT_FONT_SIZE 11   ; gmtset LABEL_FONT_SIZE 11   ; gmtset TICK_LENGTH 0.1
gmtset FRAME_PEN  3     ; gmtset BASEMAP_TYPE PLAIN  ; gmtset WANT_EURO_FONT TRUE  ; gmtset PLOT_DEGREE_FORMAT -D
gmtset DOTS_PR_INCH 300 ; gmtset HEADER_FONT_SIZE 30 ; gmtset OBLIQUE_ANNOTATION 0

region=-74/-30/-40/6 

#file=grid-mR-st3
#scale=1.00/4.6/0.05  # min: 1.07 ; max: 4.54

file=grid-mR-st4
scale=1.00/4.6/0.05  # min: 1.63 ; max: 4.57

#file=grid-mR-st6
#scale=1.00/4.6/0.05 # min: 1.99 ; max: 4.67

xyz2grd /home/marcelo/gmR/$file.txt -G./$file.grd -R$region -I0.5 -V

makecpt -I -T1.5/5.0/0.5 > /home/marcelo/gmR/$file.cpt
#makecpt -I -T$scale > /home/marcelo/gmR/$file.cpt
#grd2cpt /home/marcelo/maps/a-grids/$file.grd > ~/maps/a-grids/$file.cpt

psbasemap -R$region -JM17.0 -Ba2WSen -P -K > $file-quick.ps
#pscoast -R$region -W1 -JM17.0 -A1000/1 -Di -G255/255/170 -S116/195/250 -O -K -N1 >> $file-quick.ps



pscoast  -R$region -JM19.0 -Gc -O -K >> $file-quick.ps
grdimage /home/marcelo/gmR/$file.grd -JM17 -E300 -C/home/marcelo/gmR/$file.cpt >> $file-quick.ps
pscoast -Q -O -K >> $file-quick.ps
psscale -C/home/marcelo/gmR/$file.cpt -D5.7i/2.50i/2.00i/0.3i -Ba0.5f0.5:"Magnitudes Values":  -O -E -K >> $file-quick.ps
#grdcontour /home/marcelo/gmR/$file.grd -JM19 -C/home/marcelo/gmR/$file.cpt > $file-quick.ps
gv $file-quick.ps&
