import numpy as np
import argparse

parser = argparse.ArgumentParser()
#Cheat sheet of arguments to be used with the script
parser.add_argument("-inp1", "--input1", dest = "input1", default = "VECTORS", help="Name of input file that contains only the scaling factor and the cell vectors")
parser.add_argument("-inp2", "--input2", dest = "input2", default = "0.xyz", help="Name of .xyz file that contains the cartesian coordinates")
parser.add_argument("-out", "--output", dest = "output", default = "POSCAR", help="Name of your output file")
args = parser.parse_args()

f = open(args.input1,"r")
content = f.readlines()
ScaleFactor = float(content[0])
Vectors = []
for i in range(1,4):
    Vectors.append(content[i].split())
VectorsAdj = []
for i in Vectors:
    VectorsAdj.append([float(i[0])*ScaleFactor,float(i[1])*ScaleFactor,float(i[2])*ScaleFactor])
FixedVals = content[4]
commapos = []
for i in range(len(FixedVals)):
    if FixedVals[i]==',':
        commapos.append(i)

FRange = []

for i in range(len(commapos)):
    if i==0:
        x = FixedVals[:commapos[i]]
        if '-' in x:
            xindex = x.index('-')
            firstval = int(x[:xindex])
            secondval = int(x[xindex+1:])
            for i in range(firstval-1,secondval):
                FRange.append(i)
        else:
            FRange.append(int(x)-1)
    else:
        x = FixedVals[commapos[i-1]+1:commapos[i]]
        if '-' in x:
            xindex = x.index('-')
            firstval = int(x[:xindex])
            secondval = int(x[xindex+1:])
            for i in range(firstval-1,secondval):
                FRange.append(i)
        else:
            FRange.append(int(x)-1)
x = FixedVals[commapos[len(commapos)-1]+1:]
if '-' in x:
    xindex = x.index('-')
    firstval = int(x[:xindex])
    secondval = int(x[xindex+1:])
    for i in range(firstval-1,secondval):
        FRange.append(i)
else:
    FRange.append(int(x)-1)
if len(commapos) == 0:
    if '-' in FixedVals:
        xindex = FixedVals.index('-')
        firstval = int(FixedVals[:xindex])
        secondval = int(FixedVals[xindex+1:])
        for i in range(firstval-1,secondval):
            FRange.append(i)
    else:
        FRange.append(int(FixedVals)-1)


g = open(args.input2,"r")
content = g.readlines()
AtomCoords = []
Atoms = []
for i in range(2,len(content)):
    Atoms.append(content[i].split()[0])
    AtomCoords.append([float(content[i].split()[1]),float(content[i].split()[2]),float(content[i].split()[3])])

h = open(args.output,"w")
print("XYZ to POSCAR",file=h)
print("%0.16f" % ScaleFactor,file=h)
for i in Vectors:
    print("%0.16f" % float(i[0]),"%0.16f" % float(i[1]),"%0.16f" % float(i[2]),file=h)
AtomList = []
AtomNum = []
for i in range(len(Atoms)):
    if i==0:
        AtomList.append(Atoms[i])
        AtomNum.append(1)
    else:
        if Atoms[i] != AtomList[len(AtomList)-1]:
            AtomList.append(Atoms[i])
            AtomNum.append(1)
        else:
            AtomNum[len(AtomNum)-1] += 1
for i in AtomList:
    print(i, end=" ",file=h)
print("",file=h)
for i in AtomNum:
    print(i, end=" ",file=h)
print("",file=h)
print("Selective dynamics",file=h)
print("Direct",file=h)

AtomTot = 0
for i in AtomNum:
    AtomTot+=i

for i in range(AtomTot):
    MatrixMult = np.matmul(AtomCoords[i],np.linalg.inv(VectorsAdj))
    if i in FRange:
        print('%0.16f' % MatrixMult[0], '%0.16f' % MatrixMult[1],'%0.16f' % MatrixMult[2],'F','F','F',file=h)  
    else:
        print('%0.16f' % MatrixMult[0], '%0.16f' % MatrixMult[1],'%0.16f' % MatrixMult[2],'T','T','T',file=h)  
h.close()
