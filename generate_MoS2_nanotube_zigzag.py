#!/usr/bin/env python
from ase import Atoms, Atom, io
import numpy as np

n = 20       # number of atoms per ring
c = 5.526       # cell length along c direction
vacuum = 13.0    # Vacuum thickness
len = 3.190     #   Mo-Mo distance
layer_gap = 1.565

angle = 2*np.pi/n
r_Mo = len/2/np.sin(angle/2)    # radius of the Mo layer
r_S_in = r_Mo - layer_gap	# radius of the inner S layer
r_S_out = r_Mo + layer_gap	# radius of the outer S layer

print 'Tube inner-radius is ', r_S_in

a = b = vacuum + 2 * r_S_out    # cell length along a and b directions

atoms = Atoms(cell=[a,b,c])

for i in range(n):
	dx = r_Mo * np.sin(angle*i)
	dy = r_Mo * np.cos(angle*i)
	Mo_pos = [a/2+dx, b/2+dy, 0]
	atoms.append(Atom('Mo',Mo_pos))
		
	dx = r_Mo * np.sin(angle*i+angle/2)
        dy = r_Mo * np.cos(angle*i+angle/2)
        Mo_pos = [a/2+dx, b/2+dy, c/2]
        atoms.append(Atom('Mo',Mo_pos))

        dx = r_S_in * np.sin(angle*i)
        dy = r_S_in * np.cos(angle*i)
        S_pos = [a/2+dx, b/2+dy, c/3]
        atoms.append(Atom('S',S_pos))

        dx = r_S_out * np.sin(angle*i)
        dy = r_S_out * np.cos(angle*i)
        S_pos = [a/2+dx, b/2+dy, c/3]
        atoms.append(Atom('S',S_pos))

        dx = r_S_in * np.sin(angle*(i+0.5))
        dy = r_S_in * np.cos(angle*(i+0.5))
        S_pos = [a/2+dx, b/2+dy, 5*c/6]
        atoms.append(Atom('S',S_pos))

        dx = r_S_out * np.sin(angle*(i+0.5))
        dy = r_S_out * np.cos(angle*(i+0.5))
        S_pos = [a/2+dx, b/2+dy, 5*c/6]
        atoms.append(Atom('S',S_pos))

io.write('MoS2_tube_zigzag_%i_0.cif'%n,atoms)
