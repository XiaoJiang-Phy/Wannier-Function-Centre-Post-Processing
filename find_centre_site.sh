#!/bin/sh
# Extract the Cartesian coordinates and spread of the Wannier function center in the output file prefix.wout of wannier90
#Set the context keyword
keyword_before='Final State'
keyword_after='Spreads (Ang^2)'
#
#
input_file='WO3.wout'
#
rm centre.dat
awk "/$keyword_before/,/$keyword_after/" "$input_file" >> centre.dat
rm centre_site.dat
echo "# Cartesian Coordinate (Ang)" >> centre_site.dat
echo "# atoms projections NO. x y z spread" >> centre_site.dat
atoms='1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17'
proj='pz px py'
j=0
for i in ${atoms}
 do
   for p in ${proj}
    do
       ((j++))
       grep "$j  (" "centre.dat" | awk -v c1=$i -v c2=$p '{print c1, c2, $5, $7, $8, $9, $11}' >> centre_site.dat
    done
 done
grep "Sum of centres and spreads" "centre.dat"| awk '{print "#", $0}' >> centre_site.dat

