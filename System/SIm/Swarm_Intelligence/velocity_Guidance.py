import pygame
import numpy as np




def Guidance():
    x1=100
    y1=100
    x2=100
    y2=150
    x3=100
    y3=250
    x4=100
    y4=500

    l=600
    b=600
    x0=int(input("x0--->"))
    y0=int(input("y0--->"))

    

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
                    pygame.draw.rect(dis,blue,[x4,y4,10,10])  
                    pygame.display.update()      
                    clock.tick(30)
                else:
                    break



Guidance()