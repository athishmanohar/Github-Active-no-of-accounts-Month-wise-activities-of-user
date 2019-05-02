from collections import deque
import matplotlib.pyplot as plt
from pylab import *
import numpy as np
import random

#a=[40, 1, 18, 22, 20, 8, 5, 0, 0, 0, 0, 4]
def arr(a):
	d=[]
	maxi=max(a)
	for i in a:
		x=[i]
		b=[0]*(12-len(x))
		x.extend(b)
		d.extend(x)
	return d

def user_activity(a):
	new_a=a[2:]
	data = arr(new_a)
	data=array(data)
	print(len(data))
	data=data.reshape(12,12)
	i=0
	temp=[]
	for item in data:
		ch=np.roll(item,i)
		i=i+1
		temp.append(ch)

	data=array(temp)
	data = np.abs(data)
	#colors = [(0,0,0)] + [(cm.Greens(i)) for i in xrange(1,256)]
	#new_map = matplotlib.colors.LinearSegmentedColormap.from_list('new_map', colors, N=256)
	index=['nov','dec','jan','feb','mar','apr','may','jun','jul','aug','sep','oct']
	cols=['nov','dec','jan','feb','mar','apr','may','jun','jul','aug','sep','oct']
	#fig,ax=plt.subplots()
	plt.pcolor(data, cmap=cm.Greens)
	pos=np.arange(len(index))+0.5
	plt.yticks(pos,index)
	#plt.ylabel()

	plt.xticks(pos,cols)
	#plt.xlabel(cols)
	plt.title(str(a[1]))
	plt.colorbar()
	savefig('map.png')
	show()
#if __name__ == '__main__':
#	user_activity(a)	