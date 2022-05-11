
def Physics(x1,x2,y1,y2,rblb,l,b):
    
    xdisp=x2-x1
    ydisp=y2-y1

    #finding the direction & steps of x & y movement 
    if(xdisp<1):
        xdir='left'
        xstep=int(xdisp/rblb)*-1   # to make it positive
    else:
        xdir='right'
        xstep=int(xdisp/rblb) 

    if(ydisp<1):
        ydir='down'
        ystep=int(ydisp/rblb)*-1   # to make it positive
    else:
        ydir='up'
        ystep=int(ydisp/rblb)

    if(x1<l and x2<l and y1<b and y2<b):
        return(True,xdir,xstep,ydir,ystep,l,b,x1,y1,x2,y2,rblb)
    else:
        print("[WARNING:System parameter outbounted]")
