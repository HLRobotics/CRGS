
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
