
from Swarm_Intelligence import Fear_Of_Boundary
import pygame
pygame.init()
import math
import time
import csv



def GuidanceMapper(Status,xdir,xstep,ydir,ystep,l,b,x1,y1,x2,y2,rblb,swarm_flock_distance,xdir1,xstep1,ydir1,ystep1,Bot1x,Bot1y,xdir2,xstep2,ydir2,ystep2,Bot2x,Bot2y,xdir3,xstep3,ydir3,ystep3,Bot3x,Bot3y):

    
    
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
    #pygame.draw.rect(dis,white,[x1,y1,10,10])
    #pygame.draw.rect(dis,green,[x1+swarm_flock_distance,y1+swarm_flock_distance,10,10])
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
                    pygame.draw.rect(dis, white, [x1, y1, 10, 10])
                    pygame.draw.rect(dis, red, [Bot1x, Bot1y, 10, 10])
                    pygame.draw.rect(dis,green,[Bot2x,Bot2y,10,10])
                    pygame.draw.rect(dis,blue,[Bot3x,Bot3y,10,10])                    
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
                    pygame.draw.rect(dis, white, [x1, y1, 10, 10])
                    pygame.draw.rect(dis, red, [Bot1x, Bot1y, 10, 10])
                    pygame.draw.rect(dis,green,[Bot2x,Bot2y,10,10])
                    pygame.draw.rect(dis,blue,[Bot3x,Bot3y,10,10])
                    pygame.display.update()
                    clock.tick(30)

            ############################################

                 
                pygame.draw.rect(dis, white, [x1, y1, 10, 10])
                pygame.draw.rect(dis,red,[Bot1x,Bot1y,10,10])
                pygame.draw.rect(dis,green,[Bot2x,Bot2y,10,10])
                pygame.draw.rect(dis,blue,[Bot3x,Bot3y,10,10])
                pygame.display.update()
                        


                while xstep1!=-1:
                    
                    print('bot1x position',Bot1x)
                    if(xdir1=='right'):
                        Bot1x += rblb
                    else:
                        Bot1x -= rblb   
                    xstep1 -= 1
                    dis.fill(black)
                    pygame.draw.rect(dis, white, [x1, y1, 10, 10])
                    pygame.draw.rect(dis, red, [Bot1x, Bot1y, 10, 10])
                    pygame.draw.rect(dis,green,[Bot2x,Bot2y,10,10])
                    pygame.draw.rect(dis,blue,[Bot3x,Bot3y,10,10])                  
                    pygame.display.update()
                    clock.tick(30)
                   
                    Collision_Status=Fear_Of_Boundary.boundary_check(Bot1x,Bot1y,15,Bot2x,Bot2y)
                    if(Collision_Status==True):
                        print('[collision Bot 1,Bot 2]')
                        break
                    Collision_Status=Fear_Of_Boundary.boundary_check(Bot2x,Bot2y,15,Bot3x,Bot3y)
                    if(Collision_Status==True):
                        print('[collision Bot 2,Bot 3]')
                        break
                
                while ystep1!=-1:
                    
                    print('bot1y Position',Bot1y)
                    if(ydir1=='up'):
                        Bot1y += rblb
                    else:
                        Bot1y -= rblb   
                    ystep1 -= 1
                    dis.fill(black)
                    pygame.draw.rect(dis, white, [x1, y1, 10, 10])
                    pygame.draw.rect(dis, red, [Bot1x, Bot1y, 10, 10])
                    pygame.draw.rect(dis,green,[Bot2x,Bot2y,10,10])
                    pygame.draw.rect(dis,blue,[Bot3x,Bot3y,10,10])
                    pygame.display.update()
                    clock.tick(30)
                   
                    Collision_Status=Fear_Of_Boundary.boundary_check(Bot1x,Bot1y,15,Bot2x,Bot2y)
                    if(Collision_Status==True):
                        print('[collision Bot 1,Bot 2]')
                        break
                    Collision_Status=Fear_Of_Boundary.boundary_check(Bot2x,Bot2y,15,Bot3x,Bot3y)
                    if(Collision_Status==True):
                        print('[collision Bot 2,Bot 3]')
                        break
                    

    
                while xstep2!=-1:
                    
                    print('bot2x position',Bot2x)
                    if(xdir2=='right'):
                        Bot2x += rblb
                    else:
                        Bot2x -= rblb   
                    xstep2 -= 1
                    dis.fill(black)
                    pygame.draw.rect(dis, white, [x1, y1, 10, 10])
                    pygame.draw.rect(dis, red, [Bot1x, Bot1y, 10, 10])
                    pygame.draw.rect(dis,green,[Bot2x,Bot2y,10,10])
                    pygame.draw.rect(dis,blue,[Bot3x,Bot3y,10,10])                 
                    pygame.display.update()
                    clock.tick(30)
                   
                    Collision_Status=Fear_Of_Boundary.boundary_check(Bot1x,Bot1y,15,Bot2x,Bot2y)
                    if(Collision_Status==True):
                        print('[collision Bot 1,Bot 2]')
                        break
                    Collision_Status=Fear_Of_Boundary.boundary_check(Bot2x,Bot2y,15,Bot3x,Bot3y)
                    if(Collision_Status==True):
                        print('[collision Bot 2,Bot 3]')
                        break
                    
                while ystep2!=-1:
                    
                    print('bot2y Position',Bot2y)
                    if(ydir2=='up'):
                        Bot2y += rblb
                    else:
                        Bot2y -= rblb   
                    ystep2 -= 1
                    dis.fill(black)
                    pygame.draw.rect(dis, white, [x1, y1, 10, 10])
                    pygame.draw.rect(dis, red, [Bot1x, Bot1y, 10, 10])
                    pygame.draw.rect(dis,green,[Bot2x,Bot2y,10,10])
                    pygame.draw.rect(dis,blue,[Bot3x,Bot3y,10,10])
                    pygame.display.update()
                    clock.tick(30)
                   
                    Collision_Status=Fear_Of_Boundary.boundary_check(Bot1x,Bot1y,15,Bot2x,Bot2y)
                    if(Collision_Status==True):
                        print('[collision Bot 1,Bot 2]')
                        break
                    Collision_Status=Fear_Of_Boundary.boundary_check(Bot2x,Bot2y,15,Bot3x,Bot3y)
                    if(Collision_Status==True):
                        print('[collision Bot 2,Bot 3]')
                        break


                while xstep3!=-1:
                    
                    print('bot3x position',Bot3x)
                    if(xdir3=='right'):
                        Bot3x += rblb
                    else:
                        Bot3x -= rblb   
                    xstep3 -= 1
                    dis.fill(black)
                    pygame.draw.rect(dis, white, [x1, y1, 10, 10])
                    pygame.draw.rect(dis, red, [Bot1x, Bot1y, 10, 10])
                    pygame.draw.rect(dis,green,[Bot2x,Bot2y,10,10])
                    pygame.draw.rect(dis,blue,[Bot3x,Bot3y,10,10])                 
                    pygame.display.update()
                    clock.tick(30)
                  
                    Collision_Status=Fear_Of_Boundary.boundary_check(Bot1x,Bot1y,15,Bot2x,Bot2y)
                    if(Collision_Status==True):
                        print('[collision Bot 1,Bot 2]')
                        break
                    Collision_Status=Fear_Of_Boundary.boundary_check(Bot2x,Bot2y,15,Bot3x,Bot3y)
                    if(Collision_Status==True):
                        print('[collision Bot 2,Bot 3]')
                        break
                   
                
                while ystep3!=-1:
                    print('bot2y Position',Bot3y)
                    if(ydir3=='up'):
                        Bot3y += rblb
                    else:
                        Bot3y -= rblb   
                    ystep3 -= 1
                    dis.fill(black)
                    pygame.draw.rect(dis, white, [x1, y1, 10, 10])
                    pygame.draw.rect(dis, red, [Bot1x, Bot1y, 10, 10])
                    pygame.draw.rect(dis,green,[Bot2x,Bot2y,10,10])
                    pygame.draw.rect(dis,blue,[Bot3x,Bot3y,10,10])
                    pygame.display.update()
                    clock.tick(30)
                    
                    Collision_Status=Fear_Of_Boundary.boundary_check(Bot1x,Bot1y,15,Bot2x,Bot2y)
                    if(Collision_Status==True):
                        print('[collision Bot 1,Bot 2]')
                        break
                    Collision_Status=Fear_Of_Boundary.boundary_check(Bot2x,Bot2y,15,Bot3x,Bot3y)
                    if(Collision_Status==True):
                        print('[collision Bot 2,Bot 3]')
                        break
                   



                #############################################

         
            Bot_state=str(Bot1x)+str(Bot1y)+str(Bot2x)+str(Bot2y)+str(Bot3x)+str(Bot3y)
            with open('AI_bots_setting.csv', 'w', newline='') as file:
                print("recorded Message")
                writer = csv.writer(file)
                writer.writerow(Bot_state)
            return('[Reached the desired position]',x2,y2)
            
            #quit()
        time.sleep(30)

