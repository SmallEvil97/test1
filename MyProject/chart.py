import math
import pylab
from matplotlib import mlab
pylab.ion()
xlis = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
ylis = [25,12.5,8.75,7.5,5,5,3.75,3.75,2.6,2.6,2.6,2.6,2,2,2,2,2,2,2,2]
for n in range (200):
    ylist = [(y + n / 50) for y in ylis]
    xlist = [(x + n / 50) for x in xlis]
    pylab.plot(xlist,ylist,'go-')
    pylab.draw()
pylab.close()
