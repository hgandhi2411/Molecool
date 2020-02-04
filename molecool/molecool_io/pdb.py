"""
input and output for pdb files
"""

import os

def open_pdb(file_location):
    # This function reads in a pdb file and returns the atom names and coordinates.
    with open(file_location) as f:
        data = f.readlines()
    
    coords = []
    symbols = []
    for line in data:
        if 'ATOM' in line[0:6] or 'HETATM' in line[0:6]:
            symbols.append(line[76:79].strip())
            atoms_coords = [float(x) for x in line[30:55].split()]
            coords.append(atom_coords)
    
    coords = np.array(coords)
    
    return symbols, coords
