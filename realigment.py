#!/usr/bin/env python

from sys import argv
from ase import io,Atom

#base_element = argv[1]
atoms = io.read('POSCAR-FeN4')
for i in atoms.get_chemical_symbols():
    if i is not 'C':
        a = atoms.pop(atoms.get_chemical_symbols().index(i))
        atoms.extend(a)

io.write('POSCAR_re', atoms)
