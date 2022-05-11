import py_qmc5883l
import math
import numpy as np

sensor=py_qmc5883l.QMC5883L()
while(True):
    m=sensor.get_magnet()
    x=m[0]
    y=m[1]
    #print(x,y)
    tan=y/x
    value=90-(math.atan2(y,x))*180/np.pi
    print(value)
    if(value<40 and value>38):
        print("North")
    elif(value<81 and value>80):
        print("West")
    elif(value<45 and value>43):
        print("East")