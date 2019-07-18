# MolSSI Summer School 2019
# Python Workshop
# Geometry Analysis Project
# Updated: 7/18/19
# A.Zamani


# importing libraries

import numpy as np
import os
import sys

# begin functions definitions

# conditional for bond length thresholds
def bond_check(d_2atm, min_d=0, max_d = 1.5):
    if d_2atm > min_d and d_2atm <= max_d:
        return True
    else:
        return False


# function for calculating bond distance
def calculate_distance(a1, a2):
    x_distance = a1[0] - a2[0]
    y_distance = a1[1] - a2[1]
    z_distance = a1[2] - a2[2]
    distance = np.sqrt(x_distance**2 + y_distance**2 + z_distance**2)
    
    return distance

# end function definitions

#
# start main code
#

if __name__ == "__main__":

# conditional for cmd line argument

    if len(sys.argv) != 2:
        print('Filename not specified. Please try again.')
        exit()

# specify cmd line argument for input file 

    xyzfilename = sys.argv[1]

    water_file = os.path.join('data', xyzfilename) #dont need to type out entire directory
    print(water_file)

    water = np.genfromtxt(fname=water_file,skip_header=2, dtype='unicode') 
    #help(np.genfromtxt)
    atom_labels = water[0:,0]
    print(atom_labels)
    atom_coordinates = water[0:,1:]
    print(water)
    print(atom_coordinates)
    print('\n')

    atom_coordinates = atom_coordinates.astype(np.float)

# write H2O bond distances to file
    
    water_distance_file = open(os.path.join('data', 'water_distance_file.txt'),'w+')

# let the number of atom labels = total number of atoms

    num_atoms = len(atom_labels)
    print(' Number of atoms in molecule:',num_atoms)

# nested for loops used to compute & print all bond distances

    for i in range(num_atoms):
        for j in range(i+1,num_atoms):
            distance_2atoms = calculate_distance(atom_coordinates[i],atom_coordinates[j])
            if bond_check(distance_2atoms):
              
                print(F' {atom_labels[i]} - {atom_labels[j]} | Atom Distance: {distance_2atoms:.5f} Angstroms')
                water_distance_file.write(F'{atom_labels[i]} - {atom_labels[j]} | Atom Distance: {distance_2atoms:.5f} Angstroms \n')

# close the file after writing
            
    water_distance_file.close()

#
# end main code
#
