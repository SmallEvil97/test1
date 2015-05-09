from SandBox.analysis_text1 import *
import pylab
import time
dat = []
ylis = [25,12.5,8.75,7.5,5,5,3.75,3.75,2.6,2.6,2.6,2.6,2,2,2,2,2,2,2,2]
pylab.ion()
for n in range(30):
    ylist = [(y + n / 2) for y in ylis]
    dat.extend(b)
    pylab.subplot (2, 1, 1)
    pylab.plot (dat,'go-')
    pylab.title ("Chart Analysis_Text")
    pylab.subplot (2, 1, 2)
    pylab.plot (ylist,'go-')
    pylab.title ("Chart")        
    pylab.draw()
    time.sleep(1)
