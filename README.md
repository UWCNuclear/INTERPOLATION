# Interpolation
Cebo's interpolation code

# Description
This code calculates the total and second moment of nuclear photo-absorption cross sections.
Photo-absorption cross sections are composed of neutron, proton, two-neutron etc. channels, these must be input independently if not summed prior.

# Requirements
The interpolation code is written in Python language, python version 3 is required together with pandas, scipy and matplotlib libraries.
The input file called in the code is required to have three columns of data-that is, gamma energies, cross section and cross section uncertainty.

# Execution
in terminal: 
/bin/python3 Interpolation_Code_Aug2021.py
 
or simply:
python3 Interpolation_Code_Aug2021.py

# File Format
The code requires input from an ASCII file with extension .dat, .txt or .csv
 
# Output
The program outputs a figure of the interpolant and experimental data, total cross section and the second moment of nuclear photo-absorption cross section and uncetainty.
