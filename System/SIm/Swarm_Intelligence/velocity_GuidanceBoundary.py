import pygame
import numpy as np
from Swarm_Intelligence import Fear_Of_Boundary
import csv


def Guidance(x0,y0):



    locations="System/AI_bots_setting.csv"
    with open(locations) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            print("[Reading previous location data]")
            for row in readCSV: 
                print(row)
                x1=int(str(row[0])+str(row[1])+str(row[2]))
                y1=int(str(row[3])+str(row[4])+str(row[5]))

                x2=int(str(row[6])+str(row[7])+str(row[8]))
                y2=int(str(row[9])+str(row[10])+str(row[11]))

                x3=int(str(row[12])+str(row[13])+str(row[14]))
                y3=int(str(row[15])+str(row[16])+str(row[17]))

                x4=int(str(row[18])+str(row[19])+str(row[20]))
                y4=int(str(row[21])+str(row[22])+str(row[23]))
   

    l=600
    b=600
    

    

    white = (255, 255, 255) #RGB
    black = (0, 0, 0)
    red = (255, 0, 0)
    blue=(0,0,255)
    green=(0,255,0)
    clock = pygame.time.Clock()
    dis = pygame.display.set_mode((l,b))#size
    pygame.display.set_caption('[SWARM Robot Guidance System]')
    dis.fill(black)
    pygame.draw.rect(dis, white, [x1, y1, 10, 10])
    pygame.draw.rect(dis,red,[x2,y2,10,10])
    pygame.draw.rect(dis,green,[x3,y3,10,10])
    pygame.draw.rect(dis,blue,[x4,y4,10,10])
    pygame.display.update()
    clock.tick(30)

    while(True):
        for event in pygame.event.get():             
            while(True):
                Vx=(x0-x1)
                t=0.005               
                Vy=(y0-y1)
               
                t1=0.005
                Vx1=(x0-x2)               
                Vy1=(y0-y2)
                
                t2=0.005
                Vx2=(x0-x3)               
                Vy2=(y0-y3)

                
                t3=0.005
                Vx3=(x0-x4)               
                Vy3=(y0-y4)
                
        
                if(x1<l and y1<b and x2<l and y2<b and x3<l and x4<l and y3<b and y4<b and x1>0 and x2>0 and x3>0 and x4>0 and y4>0 and y3>0 and y2>0 and y1>0):
                    x1=x1+Vx*t 
                    y1=y1+Vy*t
                    Status=Fear_Of_Boundary.boundary_check(x0,y0,20,x1,y1)
                    Status1=Fear_Of_Boundary.boundary_check(x1,y1,20,x2,y2)
                    Status2=Fear_Of_Boundary.boundary_check(x2,y2,20,x3,y3)
                    Status3=Fear_Of_Boundary.boundary_check(x3,y3,20,x4,y4)
                    if(Status==True):
                        #break
                        Bot_state=str(int(x1))+str(int(y1))+str(int(x2))+str(int(y2))+str(int(x3))+str(int(y3))+str(int(x4))+str(int(y4))
                        with open('System/AI_bots_setting.csv', 'w', newline='') as file:
                            print("recorded Message")
                            writer = csv.writer(file)
                            writer.writerow(Bot_state)
                        return(True)


                    x2=x2+Vx1*t1 
                    y2=y2+Vy1*t1
                    Status=Fear_Of_Boundary.boundary_check(x0,y0,20,x2,y2)
                    Status1=Fear_Of_Boundary.boundary_check(x1,y1,20,x2,y2)
                    Status2=Fear_Of_Boundary.boundary_check(x2,y2,20,x3,y3)
                    Status3=Fear_Of_Boundary.boundary_check(x3,y3,20,x4,y4)
                    if(Status or Status1 or Status2 or Status3==True):
                        #break
                        Bot_state=str(int(x1))+str(int(y1))+str(int(x2))+str(int(y2))+str(int(x3))+str(int(y3))+str(int(x4))+str(int(y4))
                        with open('System/AI_bots_setting.csv', 'w', newline='') as file:
                            print("recorded Message")
                            writer = csv.writer(file)
                            writer.writerow(Bot_state)
                        return(True)

                    x3=x3+Vx2*t2 
                    y3=y3+Vy2*t2
                    Status=Fear_Of_Boundary.boundary_check(x0,y0,20,x3,y3)
                    Status1=Fear_Of_Boundary.boundary_check(x1,y1,20,x2,y2)
                    Status2=Fear_Of_Boundary.boundary_check(x2,y2,20,x3,y3)
                    Status3=Fear_Of_Boundary.boundary_check(x3,y3,20,x4,y4)
                    if(Status or Status1 or Status2 or Status3==True):

                        #break
                        Bot_state=str(int(x1))+str(int(y1))+str(int(x2))+str(int(y2))+str(int(x3))+str(int(y3))+str(int(x4))+str(int(y4))
                        with open('System/AI_bots_setting.csv', 'w', newline='') as file:
                            print("recorded Message")
                            writer = csv.writer(file)
                            writer.writerow(Bot_state)
                        return(True)

                    x4=x4+Vx3*t3 
                    y4=y4+Vy3*t3
                    Status=Fear_Of_Boundary.boundary_check(x0,y0,20,x4,y4)
                    Status1=Fear_Of_Boundary.boundary_check(x1,y1,20,x2,y2)
                    Status2=Fear_Of_Boundary.boundary_check(x2,y2,20,x3,y3)
                    Status3=Fear_Of_Boundary.boundary_check(x3,y3,20,x4,y4)
                    if(Status or Status1 or Status2 or Status3==True):
                        #break
                        Bot_state=str(int(x1))+str(int(y1))+str(int(x2))+str(int(y2))+str(int(x3))+str(int(y3))+str(int(x4))+str(int(y4))
                        with open('System/AI_bots_setting.csv', 'w', newline='') as file:
                            print("recorded Message")
                            writer = csv.writer(file)
                            writer.writerow(Bot_state)
                        return(True)




                    print(x1,y1,x2,y2,x3,y3,x4,y4)

          

                    dis.fill(black)
                    pygame.draw.rect(dis, white, [x1, y1, 10, 10])
                    pygame.draw.rect(dis,red,[x2,y2,10,10])
                    pygame.draw.rect(dis,green,[x3,y3,10,10])  
                    pygame.draw.rect(dis,blue,[x4,y4,10,10])  
                    pygame.display.update()      
                    clock.tick(30)
                else:
                    break
