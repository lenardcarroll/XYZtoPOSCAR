# XYZtoPOSCAR

Before using this script, create a file that contains only the scaling factor (lattice constant) and the cell vectors of your system. It should look like this:

```
 1.00000000000000     
 
 24.6914512445513985  0.0000000000000000  0.0000000000000000
 
  7.4065517955292197 12.8319727856189001  0.0000000000000000
  
  0.0000000001313560  0.0000000000558372 10.0000000000000000
```

Next, to use the script, follow this general command:

```
python -i XYZtoPOSCAR.py -inp1 <CELL_VECTOR_FILE> -inp2 <XYZ_INPUT_FILE> -out <OUTPUT_FILE_NAME>
```

This script should convert some general .xyz files into POSCAR files in fractional coordinates.
