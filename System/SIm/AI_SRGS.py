from Swarm_Robot_Guidance_SYstem import Physics
from Swarm_Robot_Guidance_SYstem import Guidance_System
logic=False
while(True):
    if(logic==False):
        l=int(input('Enter the length of room'))
        b=int(input('Enter the breadth fo room'))
        x1=int(input('Enter the intial x position number'))
        y1=int(input('Enter the intial y position number'))
        x2=int(input('Enter the final x position number'))
        y2=int(input('Enter the final y position number'))
        rblb=int(input('Enter l&b of robot'))
        formation=int(input("1.Triangular formation  2.Parallel formation"))
        swarm_flock_distance=int(input('Enter the Swarm flock formation distance'))
    else:
        x1=x2
        y1=y2
        x2=int(input('Enter the final x position number'))
        y2=int(input('Enter the final y position number'))

    data=Physics.Physics(x1,x2,y1,y2,rblb,l,b,swarm_flock_distance,formation)
    status=data[0]
    xdir=data[1]
    xstep=data[2]
    ydir=data[3]
    ystep=data[4]
    l=data[5]
    b=data[6]
    x1=data[7]
    y1=data[8]
    x2=data[9]
    y2=data[10]
    rblb=data[11]
    swarm_flock_distance=swarm_flock_distance
    xdir1=data[13]
    xstep1=data[14]
    ydir1=data[15]
    ystep1=data[16]
    Bot1x=data[17]
    Bot1y=data[18]
    xdir2=data[19]
    xstep2=data[20]
    ydir2=data[21]
    ystep2=data[22]
    Bot2x=data[23]
    Bot2y=data[24]
    xdir3=data[25]
    xstep3=data[26]
    ydir3=data[27]
    ystep3=data[28]
    Bot3x=data[29]
    Bot3y=data[30]

    guidance=Guidance_System.GuidanceMapper(True,xdir,xstep,ydir,ystep,l,b,x1,y1,x2,y2,rblb,swarm_flock_distance,xdir1,xstep1,ydir1,ystep1,Bot1x,Bot1y,xdir2,xstep2,ydir2,ystep2,Bot2x,Bot2y,xdir3,xstep3,ydir3,ystep3,Bot3x,Bot3y)
    logic=True
    print(guidance)