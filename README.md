# Wannier-Function-Centre-Post-Processing
The data of Wannier function centre, spread and atomic coordinates are extracted from the output files processed by Wannier90 and analyzed. 



# Processing flow
After reading the coordinates of different atoms and the coordinates of the wannier function centre from the prefix.wout file (bash find_atom_site.sh and bash find_centre_site.sh), the distance between the wannier function centre and the atomic coordinate corresponding to the atom can be calculated through WFC.py, and output to the csv file.
