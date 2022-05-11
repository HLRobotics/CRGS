import pygame
import numpy as np



def Guidance():
    x1=300
    y1=300
    x2=300
    y2=300
    x3=300
    y3=300
    x4=300
    y4=300

    l=600
    b=600
    Vx=float(input('Vx--->'))
    Vy=float(input('Vy--->'))
    t=float(input("t--->"))

    Vx1=float(input('Vx1--->'))
    Vy1=float(input('Vy1--->'))
    t1=float(input("t1--->"))

    Vx2=float(input('Vx2--->'))
    Vy2=float(input('Vy2--->'))
    t2=float(input("t2--->"))

    Vx3=float(input('Vx2--->'))
    Vy3=float(input('Vy2--->'))
    t3=float(input("t2--->"))

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
        
                if(x1<l and y1<b and x2<l and y2<b and x3<l and x4<l and y3<b and y4<b and x1>0 and x2>0 and x3>0 and x4>0 and y4>0 and y3>0 and y2>0 and y1>0):
                    x1=x1+Vx*t 
                    y1=y1+Vy*t

                    x2=x2+Vx1*t1 
                    y2=y2+Vy1*t1

                    x3=x3+Vx2*t2 
                    y3=y3+Vy2*t2

                    x4=x4+Vx3*t3 
                    y4=y4+Vy3*t3


                    print(x1,y1,x2,y2,x3,y3,x4,y4)

                
                        
                    dis.fill(black)
                    pygame.draw.rect(dis, white, [x1, y1, 10, 10])
                    pygame.draw.rect(dis,red,[x2,y2,10,10])
                    pygame.draw.rect(dis,green,[x3,y3,10,10])  
                    pygame.draw.rect(dis,green,[x4,y4,10,10])  
                    pygame.display.update()      
                    clock.tick(30)
                else:
                    break



Guidance()