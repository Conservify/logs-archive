set datafile separator ","
set terminal png size 900,400
set title "Battery"
set ylabel "Level"
set xlabel "Date"
set xdata time
set timefmt "%s"
set format x "%m/%d"
set key left top
set grid

plot "battery.csv" using 1:2 with lines lw 2 lt 3 title 'battery'
