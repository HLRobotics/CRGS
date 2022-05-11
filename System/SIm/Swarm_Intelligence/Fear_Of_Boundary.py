import numpy as np 
def boundary_coordinates(x0,y0,r):
    for i in range(0,180):
        x_Pos=x0+r*np.cos(2*np.pi*i/360)
        y_Pos=y0-r*np.sin(2*np.pi*i/360)
        print(x_Pos,y_Pos)

def boundary_check(x0,y0,r,x1,y1):
    data=((x0-x1)**2)+((y0-y1)**2)-(2*r)**2
    if(data<=0):
        return(True)
    else:
        return(False)



