#!/usr/bin/gnuplot

set term postscript eps enhanced color 24

set output 'hop-plot.eps'

set xlabel "distance/50"
set ylabel "Number of Pairs"
set title "Hop-plot"

plot 'data' u 1:2 title "fre" w linespoints
