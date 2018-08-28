# gaussianGeometry

## Description

Script to read the optimized geometry of a molecule in an o Gaussian 09 output file.

## Usage:     

```console
e_gaussianGeometry.py gaussian.log 
```

- input:   gaussian output file


## Typical output


For a 2-Me-pyrrole:

```console
e_gaussianGeometry.py 2-Me-p.log
```

<pre>
Opt procedure:
Step   0  (E-E0) =     0.0000000 kJ/mol
Step   1  (E-E0) =   -21.9474157 kJ/mol
Step   2  (E-E0) =   -23.3865100 kJ/mol
Step   3  (E-E0) =   -23.5130906 kJ/mol
Step   4  (E-E0) =   -23.5195099 kJ/mol
Step   5  (E-E0) =   -23.5200114 kJ/mol
Step   6  (E-E0) =   -23.5200508 kJ/mol
Step   7  (E-E0) =   -23.5200534 kJ/mol
Step   8  (E-E0) =   -23.5200534 kJ/mol
Step   9  (E-E0) =   -23.5200534 kJ/mol

Final Energy:
-249.508450456  Hartree,  -655084.4366722  kJ/mol


Probabilities (%):
[  8.93988412e-04   6.25682446e+00   1.11807894e+01   1.17665308e+01
   1.17970401e+01   1.17994268e+01   1.17996143e+01   1.17996268e+01
   1.17996268e+01   1.17996268e+01] sum =  100.0

Output: 2-Me-p_opt.xyz

</pre>
