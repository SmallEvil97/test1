from SandBox.analysis_text import *
import pylab
import time
dat = []
ylis = [25,12.5,8.75,7.5,5,5,3.75,3.75,2.6,2.6,2.6,2.6,2,2,2,2,2,2,2,2]
dat.extend(b)
e = 2
pylab.ion()
for n in range(10):
    q = [(e + n / 2)]
    ylis.extend(q)
    dat.extend(q)
    pylab.subplot (2, 1, 1)
    pylab.plot (dat,'go-')
    pylab.title ("Chart Analysis_Text")
    pylab.subplot (2, 1, 2)
    pylab.plot (ylis,'ro-')
    pylab.title ("Chart")        
    pylab.draw()
    if e == 2:
        e += 6
    else:
        e -= 2       
    time.sleep(1)
