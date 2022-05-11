from Swarm_Intelligence import Fear_Of_Boundary
import numpy as np
import random
import time
import matplotlib.pyplot as plt
j=0
SwarmList=[]
plotter_x=[]
plotter_y=[]
for i in range(0,10):
    x=(random.randint(100, 500))
    y=(random.randint(100, 500))
    SwarmList.append([x,y])
Swarm = np.array(SwarmList)

#print(Swarm.shape)
#print(Swarm)

for i in range(0,10):
    x0=Swarm[i,0]
    y0=Swarm[i,1]
    plotter_x.append(x0)
    plotter_y.append(y0)

    #print(x0,y0)

    for i in range(0,10):
        x1=Swarm[i,0]
        y1=Swarm[i,1]
        Status=Fear_Of_Boundary.boundary_check(x0,y0,50,x1,y1)
        print(x1,y1)
        if(Status==True):
            print(x1,y1,"---> Path change")
        
        #time.sleep(1)
plt.scatter(plotter_x,plotter_y)
plt.show()