import csv
#from Swarm_Intelligence import Fear_Of_Boundary
def Physics(x1,x2,y1,y2,rblb,l,b,swarm_flock_distance,formation):
    
    xdisp=x2-x1
    ydisp=y2-y1

    #########################################
    swarm_flock_distance=swarm_flock_distance
    
    locations="AI_bots_setting.csv"
    with open(locations) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            print("[Reading previous location data]")
            for row in readCSV: 
                print(row)
                Bot1x=int(str(row[0])+str(row[1])+str(row[2]))
                Bot1y=int(str(row[3])+str(row[4])+str(row[5]))

                Bot2x=int(str(row[6])+str(row[7])+str(row[8]))
                Bot2y=int(str(row[9])+str(row[10])+str(row[11]))

                Bot3x=int(str(row[12])+str(row[13])+str(row[14]))
                Bot3y=int(str(row[15])+str(row[16])+str(row[17]))


    

    #Triangular formation
    if(formation==1):
        Bot1Xdisp=x2-Bot1x-swarm_flock_distance
        Bot1Ydisp=y2-Bot1y-swarm_flock_distance

        Bot2Xdisp=x2-Bot2x+swarm_flock_distance
        Bot2Ydisp=y2-Bot2y+swarm_flock_distance

        Bot3Xdisp=x2-Bot3x+swarm_flock_distance
        Bot3Ydisp=y2-Bot3y-swarm_flock_distance
    #Triangular formation

    #Parallel formation
    if(formation==2):
        Bot1Xdisp=x2-Bot1x
        Bot1Ydisp=y2-Bot1y-swarm_flock_distance

        Bot2Xdisp=x2-Bot2x
        Bot2Ydisp=y2-Bot2y-swarm_flock_distance-swarm_flock_distance

        Bot3Xdisp=x2-Bot3x
        Bot3Ydisp=y2-Bot3y-swarm_flock_distance-swarm_flock_distance-swarm_flock_distance
    #Parallel formation


    if(Bot1Xdisp<0):
        xdir1='left'
        xstep1=int(Bot1Xdisp/rblb)*-1   # to make it positive
    else:
        xdir1='right'
        xstep1=int(Bot1Xdisp/rblb) 

    if(Bot1Ydisp<0):
        ydir1='down'
        ystep1=int(Bot1Ydisp/rblb)*-1   # to make it positive
    else:
        ydir1='up'
        ystep1=int(Bot1Ydisp/rblb)


    if(Bot2Xdisp<0):
        xdir2='left'
        xstep2=int(Bot2Xdisp/rblb)*-1   # to make it positive
    else:
        xdir2='right'
        xstep2=int(Bot2Xdisp/rblb) 

    if(Bot2Ydisp<0):
        ydir2='down'
        ystep2=int(Bot2Ydisp/rblb)*-1   # to make it positive
    else:
        ydir2='up'
        ystep2=int(Bot2Ydisp/rblb)

    

    if(Bot3Xdisp<0):
        xdir3='left'
        xstep3=int(Bot3Xdisp/rblb)*-1   # to make it positive
    else:
        xdir3='right'
        xstep3=int(Bot3Xdisp/rblb) 

    if(Bot3Ydisp<0):
        ydir3='down'
        ystep3=int(Bot3Ydisp/rblb)*-1   # to make it positive
    else:
        ydir3='up'
        ystep3=int(Bot3Ydisp/rblb)

    #########################################    

    #finding the direction & steps of x & y movement 
    if(xdisp<0):
        xdir='left'
        xstep=int(xdisp/rblb)*-1   # to make it positive
    else:
        xdir='right'
        xstep=int(xdisp/rblb) 

    if(ydisp<0):
        ydir='down'
        ystep=int(ydisp/rblb)*-1   # to make it positive
    else:
        ydir='up'
        ystep=int(ydisp/rblb)

    if(x1<l and x2<l and y1<b and y2<b and Bot1x<l and Bot1y<b and Bot2x<l and Bot2y<b and Bot3x<l and Bot3y<b):
        return(True,xdir,xstep,ydir,ystep,l,b,x1,y1,x2,y2,rblb,swarm_flock_distance,xdir1,xstep1,ydir1,ystep1,Bot1x,Bot1y,xdir2,xstep2,ydir2,ystep2,Bot2x,Bot2y,xdir3,xstep3,ydir3,ystep3,Bot3x,Bot3y)
    else:
        print("[WARNING:System parameter outbounted]")


