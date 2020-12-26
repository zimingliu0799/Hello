#!/usr/bin/env python2

from ase import Atom, io
from sys import argv

"""To use it: python add_O.py B/N/P"""

file_name = argv[1]
atoms = io.read('../../base/%s/CONTCAR' % file_name)

position = atoms[48].position + [0, 0, 1.75]
atoms.append(Atom('O', position))

io.write('POSCAR', atoms)
