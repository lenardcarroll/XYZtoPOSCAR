# XYZtoPOSCAR

Before using this script, create a file that contains only the scaling factor (lattice constant), the cell vectors of your system and where all the frozen atoms are located. It should look like this:

```
 1.00000000000000     
 24.6914512445513985  0.0000000000000000  0.0000000000000000
  7.4065517955292197 12.8319727856189001  0.0000000000000000
  0.0000000001313560  0.0000000000558372 10.0000000000000000
1-20,24,25,29,35-74
```
If no atoms are frozen/fixed, then add 'None' at the bottom, like:

```
 1.00000000000000     
 24.6914512445513985  0.0000000000000000  0.0000000000000000
  7.4065517955292197 12.8319727856189001  0.0000000000000000
  0.0000000001313560  0.0000000000558372 10.0000000000000000
None
```

The last line contains a list of all frozen atoms.

Next, to use the script, follow this general command if you want a POSCAR file with cartesian coordinates.

```
python -i XYZtoPOSCARCartesian.py -inp1 <CELL_VECTOR_FILE> -inp2 <XYZ_INPUT_FILE> -out <OUTPUT_FILE_NAME>
```

If you want fractional coordinates for the POSCAR file, use:
```
python -i XYZtoFractionalPOSCAR.py -inp1 <CELL_VECTOR_FILE> -inp2 <XYZ_INPUT_FILE> -out <OUTPUT_FILE_NAME>
```

This script should convert some general single-frame .xyz file into a POSCAR file in cartesian coordinates or fractional coordinates.
