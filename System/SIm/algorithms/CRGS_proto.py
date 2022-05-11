#import numpy as np
import pygame
pygame.init()
import math
import time

white = (255, 255, 255) #RGB
black = (0, 0, 0)
red = (255, 0, 0)
clock = pygame.time.Clock()

l=int(input('Enter the length of room'))
b=int(input('Enter the breadth fo room'))
x1=int(input('Enter the intial x position number'))
y1=int(input('Enter the intial y position number'))
x2=int(input('Enter the final x position number'))
y2=int(input('Enter the final y position number'))
rblb=int(input('Enter l&b of robot'))
# finding the distance of x & y position
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


print(xdisp,ydisp,xstep,ystep)

if(x1<l and x2<l and y1<b and y2<b):
   '''
   shortd=(((x1-x2)**2+(y1-y2)**2)**.5)
   print('Shortest Path between two points is', shortd)
   print('Speed of Robot should be',shortd/rbtl, 'm/s')
  
   theta=math.acos((x2-x1)/shortd)
   print ('angle of turning is',theta)
   '''
   #displaying intial position of ROBO
   dis = pygame.display.set_mode((l,b))#size
   pygame.display.set_caption('Cordinate Geometry Robot Guidance System')
   dis.fill(black)
   pygame.draw.rect(dis, red, [x1, y1, 10, 10])
   pygame.display.update()
   clock.tick(30)
   
   robo=False
   while not robo:
      for event in pygame.event.get():
         if(event.type ==pygame.QUIT):
            robo =True
         else:
            while xstep!=-1:
               print('x position',x1)
               if(xdir=='right'):
                  x1 += rblb
               else:
                  x1 -= rblb   
               xstep -= 1
               dis.fill(black)
               pygame.draw.rect(dis, red, [x1, y1, 10, 10])
               pygame.display.update()
               clock.tick(30)
               
            while ystep!=-1:
               print('y Position',y1)
               if(ydir=='up'):
                  y1 += rblb
               else:
                  y1 -= rblb   
               ystep -= 1
               dis.fill(black)
               pygame.draw.rect(dis, red, [x1, y1, 10, 10])
               pygame.display.update()
               clock.tick(30)
                  
            print('Reached the desired position',x2,y2)
            quit()
      time.sleep(30)

else:
   print('Outside the permissible area')