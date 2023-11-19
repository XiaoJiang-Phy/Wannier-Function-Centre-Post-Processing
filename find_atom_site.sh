#!/bin/sh
# Extract the Cartesian coordinates of some atoms in the output file prefix.wout of wannier90
key1='O'
file_name='WO3.wout'
atoms='1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16'
rm $key1"_site.dat"
echo "# Cartesian Coordinate (Ang)" >> $key1"_site.dat"
echo "# atoms x y z" >> $key1"_site.dat"
for i in ${atoms}
 do
    grep "$key1    $i" "$file_name" | awk '{print $3, $8, $9, $10}' >> $key1"_site.dat"
    grep "$key1   $i " "$file_name" | awk '{print $3, $8, $9, $10}' >> $key1"_site.dat"
done
