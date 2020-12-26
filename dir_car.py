 #!/usr/bin/env python2
# coding: utf-8

# In[2]:

# By Ming
# This script is wrote to turn direct coordination to cartesian coordination
# To use it : python dir_car CONTCAR
# Relaxation layer is fixed to the upper two layers
# The output file will be saved as CONTCAR_C
# Suitable for POSCAR with 'Selective' on the 8th line


# In[2]:


import sys
import os
import numpy as np


# In[3]:

print('Warning!!! Please check the <mode> and <start line> before use this script!\n Defalt: 8 9')

if len(sys.argv) != 2:
    print ('please rewrite your order')
    exit()
else:
    script , file_to_convert = sys.argv[:2]
    print('CONTCAR starting to convert')
    
def get_info():
    f = open(file_to_convert , 'r')
    lines = f.readlines()
    f.close()
    n_atom = sum([int(x) for x in lines[6].split()])

    a = []
    b = []
    c = []
    for i in range(2,5):
        line =[float(n) for n in lines[i].strip().split()]
        a.append(line[0])
        b.append(line[1])
        c.append(line[2])
    vector = np.array([a,b,c])
    return vector,n_atom,lines

def direct():
    mode = lines[8][0]
    if mode == 'D' or mode =='d':
        is_direct = True
    else:
        is_direct = False
    return is_direct

def convert_cart():
    x_cart = []
    y_cart = []
    z_cart = []
    TF = []
    start_line = 9
    for i in range(start_line,start_line+n_atom):
        line_data = [float(m) for m in lines[i].strip().split()[0:3]]
        line_data = np.array([line_data])
        x_c,y_c,z_c =[sum(k) for k in line_data * vector]
        x_cart.append(x_c)
        y_cart.append(y_c)
        z_cart.append(z_c)
        TF.append((lines[i].split()[3:]))

        file_out = open(file_to_convert+'_C','w')
        for i in range(0,7):
            file_out.write(lines[i].rstrip()+'\n')

        file_out.write('Cartesian'+'\n')

        for i in range(0,len(x_cart)):
            file_out.write("\t%15.10f   %15.10f   %15.10f   %s\n"  %(x_cart[i],y_cart[i],z_cart[i],' '.join(TF[i])))
        file_out.close

vector,n_atom,lines = get_info()
is_direct = direct()

if is_direct:
    convert_cart()
else:
    print('%s has Cartesian coordination already'%(file_to_convert))
    exit()


# In[ ]:




