#!/mnt/c/Python27/python.exe
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from sys import argv
import os
from scipy.optimize import *

x_CH3OH = [[1,2],[4.5,5.5,6.5,7.5]]      
y_CH3OH = [[0,0],[-1.13,-1.13,-0.83,-0.83]]      
x_CH3OH_ts = [[2,3,4.5]]
y_CH3OH_ts = [[0.00,0.83,-1.13]]

x_HOCH2OH = [[1,2],[4,5,6,7]]           
y_HOCH2OH = [[0,0],[-1.94,-1.94,-1.38,-1.38]]    
x_HOCH2OH_ts = [[2,3,4]]
y_HOCH2OH_ts = [[0,0.15,-1.94]]

x_HCOOH =  [[1,2],[3.8,4.8,5.8,6.8]]          
y_HCOOH = [[0,0],[-1.66,-1.66,-2.32,-2.32]]         
x_HCOOH_ts = [[2,3,3.8]]
y_HCOOH_ts = [[0,0.10,-1.66]]     


def fitting_curve(x,y,X):
    func = lambda tpl,x : tpl[0] + tpl[1]*x + tpl[2]*x**2  
    ErrorFunc = lambda tpl,x,y: (func(tpl,x[0]) - y[0])**2 + (func(tpl,x[1]) - y[1])**2 + (func(tpl,x[2]) - y[2])**2
    tpl_ini = (1.0,1.0,-1.0)
    cons = ({'type':'eq','fun': lambda tpl,y: tpl[0]-tpl[1]**2/(4*tpl[2])-y,'args':[y[1]]},
            {'type':'eq','fun': lambda tpl,x,y: tpl[0] + tpl[1]*x + tpl[2]*x**2 - y,'args':[x[0],y[0]]},
            {'type':'eq','fun': lambda tpl,x,y: tpl[0] + tpl[1]*x + tpl[2]*x**2 - y,'args':[x[-1],y[-1]]},
            {'type':'ineq','fun': lambda tpl,x: -tpl[1]/(2*tpl[2])-x,'args':[x[0]]},
            {'type':'ineq','fun': lambda tpl,x: x+tpl[1]/(2*tpl[2]),'args':[x[-1]]},
            {'type':'ineq','fun': lambda tpl: -tpl[2]})
    opt = {'maxiter':400,'disp':True}
    res = minimize(ErrorFunc,tpl_ini[:],args=(np.array(x),np.array(y)),method='SLSQP',constraints=cons,options=opt)
    Y = func(tuple(res.x),X)
    return Y

def plot_intermediates(x,y,color,linestyle,label=""):
    for i in range(len(x)):
        plt.plot(x[i], y[i], color=color, linestyle=linestyle, label=label)

def plot_TS(x,y,color,linestyle,label=""):
    for i in range(len(x)):
        X = np.linspace(x[i][0],x[i][-1],20)
        if y[i][0] > y[i][-1]:
            tmp= y[i][:]
            tmp.reverse() 
            Y = fitting_curve(x[i],tmp,X)
            X=list(X)
            X.reverse()
            plt.plot(X, Y, color=color, linestyle=linestyle, label=label)
        else:
            Y = fitting_curve(x[i],y[i],X)
            plt.plot(X, Y, color=color, linestyle=linestyle, label=label)

    
figure(figsize=(14,10), dpi=300)   # Size of the figure

# Range of x and y
xmin = 0.5
xmax = 7.5
ymin = -3.05
ymax = 1.27

plt.xlim(xmin,xmax)
plt.ylim(ymin,ymax)

xyfontsize =36    #  font size of the x y lable
legendfontsize =32    #  font size of the legends
tickfontsize =32     # font size of the tick numbers

ax=plt.subplot(1, 1, 1)
subplots_adjust(left=0.18, bottom=0.06, right=0.98, top=0.95, wspace=0.26, hspace=0.24)  #  this settings adjust the border of the frame and should be tested.
rcParams['lines.linewidth'] = 5

frame_linewidth = 5
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(True)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(frame_linewidth)
ax.spines['right'].set_linewidth(frame_linewidth)
ax.spines['top'].set_linewidth(frame_linewidth)
ax.spines['bottom'].set_linewidth(frame_linewidth)

###==============================================================================

plt.plot([0,65],[0,0], color='grey', linestyle='dotted')

#plot_intermediates(x_CH3OH,y_CH3OH,color='black,linestyle='solid',label="")
#plot_TS(x_CH3OH_ts,y_CH3OH_ts,color='black',linestyle='solid',label="")

plot_intermediates(x_CH3OH,y_CH3OH,color='red',linestyle='solid',label="")
plot_TS(x_CH3OH_ts,y_CH3OH_ts,color='red',linestyle='solid',label="")

plot_intermediates(x_HOCH2OH,y_HOCH2OH,color='green',linestyle='solid',label="")
plot_TS(x_HOCH2OH_ts,y_HOCH2OH_ts,color='green',linestyle='solid',label="")

plot_intermediates(x_HCOOH,y_HCOOH,color='blue',linestyle='solid',label="")
plot_TS(x_HCOOH_ts,y_HCOOH_ts,color='blue',linestyle='solid',label="")


#plt.plot(x, y, color='red', linestyle='solid', label="Pt$_3$Ti(111)")

###==============================================================================
 

#plt.xlabel('Reaction Coordinate',fontsize = xyfontsize)
plt.ylabel('Reaction Free Energy (eV)',fontsize= xyfontsize)
plt.xticks(fontsize=tickfontsize)
plt.yticks(fontsize=tickfontsize)
plt.yticks([-3,-2,-1,0,1],fontsize=tickfontsize)
plt.tick_params(
    axis='y',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    left='on',      # ticks along the left edge are on/off
    right='off',         # ticks along the right edge are on/off
    labelleft='on', # labels along the left edge are on/off
    width=3,
    length=6)

plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='off',      # ticks along the bottom edge are off
    top='off',         # ticks along the top edge are off
    labelbottom='off') # labels along the bottom edge are off

plt.legend(loc='upper left',frameon=False,fontsize=legendfontsize)
plt.rc('font',**{'family':'sans-serif','sans-serif':['Arial'], 'stretch': 'expanded', 'weight': 'normal', 'size': 24})

filename = 'Fe1_TS_b14.pdf'
plt.savefig(filename,format='pdf',transparent=True,dpi=600)
plt.show()
