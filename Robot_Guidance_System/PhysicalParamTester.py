xdisp=0
ydisp=0
robo="N"

def Physics(x1,x2,y1,y2,rblb,l,b):
    
    xdisp=x2-x1
    ydisp=y2-y1

    #finding the direction & steps of x & y movement 
    if(xdisp<1):
        xdir='L'
        xstep=int(xdisp/rblb)*-1   # to make it positive
        if(xstep<100):
            xstep="0"+str(xstep)
        elif(xstep<10):
            xstep="0"+"0"+str(xstep)
    else:
        xdir='R'
        xstep=int(xdisp/rblb) 
        if(xstep<100):
            xstep="0"+str(xstep)
        elif(xstep<10):
            xstep="0"+"0"+str(xstep)

    if(ydisp<1):
        ydir='F'
        ystep=int(ydisp/rblb)*-1   # to make it positive
        if(ystep<100):
            ystep="0"+str(ystep)
        elif(ystep<10):
            ystep="0"+"0"+str(ystep)
    else:
        ydir='R'
        ystep=int(ydisp/rblb)
        if(ystep<100):
            ystep="0"+str(ystep)
        elif(ystep<10):
            ystep="0"+"0"+str(ystep)

    if(x1<l and x2<l and y1<b and y2<b):
        return(xdir,xstep,ydir,ystep)
    else:
        print("[WARNING:System parameter outbounted]")


def Physics2(XF,YF,x1,x2,x3,y1,y2,y3,l,b):
    global xdisp,ydisp,robo
    
    xcost1=XF-x1
    xcost2=XF-x2
    xcost3=XF-x3
  

    if(xcost1<xcost2 and xcost1<xcost3):
        xdisp=xcost1
        ydisp=YF-y1
        print(x1,y1)
        robo="T"
    if(xcost2<xcost1 and xcost2<xcost3):
        xdisp=xcost2
        ydisp=YF-y2
        print(x2,y2)
        robo="P"
    if(xcost3<xcost1 and xcost3<xcost2):
        xdisp=xcost3
        ydisp=YF-y3
        print(x3,y3)
        robo="D"

    rblb=1
    if(xdisp<1):
        xdir='L'
        xstep=int(xdisp/rblb)*-1   # to make it positive
        if(xstep<100):
            xstep="0"+str(xstep)
        elif(xstep<10):
            xstep="0"+"0"+str(xstep)
    else:
        xdir='R'
        xstep=int(xdisp/rblb) 
        if(xstep<100):
            xstep="0"+str(xstep)
        elif(xstep<10):
            xstep="0"+"0"+str(xstep)

    if(ydisp<1):
        ydir='F'
        ystep=int(ydisp/rblb)*-1   # to make it positive
        if(ystep<100):
            ystep="0"+str(ystep)
        elif(ystep<10):
            ystep="0"+"0"+str(ystep)
    else:
        ydir='R'
        ystep=int(ydisp/rblb)
        if(ystep<100):
            ystep="0"+str(ystep)
        elif(ystep<10):
            ystep="0"+"0"+str(ystep)

    #if(x1<l and x2<l and y1<b and y2<b):
    return(robo,xdir,xstep,ydir,ystep)
    #else:
    #    print("[WARNING:System parameter outbounted]")

   


    
   