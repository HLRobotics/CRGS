from Robot_Guidance_System import PhysicalParamTester
from Robot_Guidance_System import Guidance
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
    else:
        x1=x2
        y1=y2
        x2=int(input('Enter the final x position number'))
        y2=int(input('Enter the final y position number'))

    data=PhysicalParamTester.Physics(x1,x2,y1,y2,rblb,l,b)
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
    guidance=Guidance.GuidanceMapper(status,xdir,xstep,ydir,ystep,l,b,x1,y1,x2,y2,rblb)
    logic=True
    print(guidance)