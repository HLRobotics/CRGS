

import pygame
pygame.init()
import math
import time


def GuidanceMapper(Status,xdir,xstep,ydir,ystep,l,b,x1,y1,x2,y2,rblb):

    try:
        white = (255, 255, 255) #RGB
        black = (0, 0, 0)
        red = (255, 0, 0)
        clock = pygame.time.Clock()
        dis = pygame.display.set_mode((l,b))#size
        pygame.display.set_caption('[Robot Guidance System]')
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
                            
                return('[Reached the desired position]',x2,y2)
                
                #quit()
            time.sleep(30)

    except:
        return('[ERROR in physics]')