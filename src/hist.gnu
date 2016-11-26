#!/usr/bin/gnuplot

set term postscript eps enhanced color 24

set output 'histogram.eps'

set xtics 20
set ytics 5
set style data histogram
set style histogram rowstacked
set style histogram cluster gap 1
set style fill solid 1.0 
set boxwidth 0.5
set ylabel "Count"
set xrange [0:160]
set size 2,2

mpl_dx     = 0.1
mpl_dy     = 0.1

### Start multiplot (2x2 layout)
set multiplot layout 2,2 rowsfirst 
# --- GRAPH a
set title "Hop-Plot distribution"
set origin 0,1
set size 1,1
set xlabel ""
plot '../out-final/hopDist.plotData' using 2 t "original" , '' using 3 t "random edge"
# --- GRAPH b
set title "Hop-Plot distribution"
set origin 1,1
set size 1,1
set ylabel ""
plot '../out-final/hopDist.plotData' using 2 t "original" , '' using 3 t "random node"
# --- GRAPH c
set title ""
set origin 0,0
set size 1,1
set xlabel "Hop Distance"
set ylabel "Count"
plot '../out-final/hopDist.plotData' using 2 t "original" , '' using 3 t "random node neighbour"
# --- GRAPH d
set origin 1,0
set size 1,1
set ylabel ""
plot '../out-final/hopDist.plotData' using 2 t "original" , '' using 3 t "random walk"


### End multiplot
