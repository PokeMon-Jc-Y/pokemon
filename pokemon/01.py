import pygame
import c.terrain
import c.character
from pygame.locals import *

screen=pygame.display.set_mode([900,600])
Map = []
Dynamicstate_point = 0
press = False

#动态滚动时坐标轴方向偏移量符号
x=0
y=0

Grass_ground = c.terrain.Terrain([pygame.image.load('image/grass.jpg').convert_alpha()],"ground")
Grass_ground1 = c.terrain.Terrain([pygame.image.load('image/grass1.jpg').convert_alpha()],"ground")
flower = c.terrain.Terrain(
    [pygame.image.load('image/flower0.jpg').convert_alpha(),
     pygame.image.load('image/flower1.jpg').convert_alpha(),
     pygame.image.load('image/flower2.jpg').convert_alpha()],"flower")


player = c.character.Character('player',
[
[pygame.image.load('image/player/front0.png').convert_alpha(),
pygame.image.load('image/player/front1.png').convert_alpha(),
pygame.image.load('image/player/front2.png').convert_alpha()],
[pygame.image.load('image/player/back0.png').convert_alpha(),
pygame.image.load('image/player/back1.png').convert_alpha(),
pygame.image.load('image/player/back2.png').convert_alpha()],
[pygame.image.load('image/player/left0.png').convert_alpha(),
pygame.image.load('image/player/left1.png').convert_alpha(),
pygame.image.load('image/player/left2.png').convert_alpha()],
[pygame.image.load('image/player/right0.png').convert_alpha(),
pygame.image.load('image/player/right1.png').convert_alpha(),
pygame.image.load('image/player/right2.png').convert_alpha()]
]
,0,1,0,0)

Tree = pygame.image.load('image/tree.png').convert_alpha()

for i in range(42):
    row=[]
    for k in range(i):
        row.append([Grass_ground1,''])
    for j in range(i,42):
        row.append([Grass_ground,''])
    Map.append(row)

Map[10][11] = [flower,'']
Map[10][12] = [flower,'']
Map[11][11] = [flower,'']
Map[11][12] = [flower,'']
Map[12][11] = [flower,'']
Map[12][12] = [flower,'']

Player_location = [10,10]





def add_tree(location):
    Map[location[0]][location[1]-1][1] = 'tree_image'
    Map[location[0]][location[1]][1] = 'tree'
    Map[location[0]][location[1]+1][1] = 'tree'
    Map[location[0]+1][location[1]][1] = 'tree'
    Map[location[0]+1][location[1]+1][1] = 'tree'


for i in range(0,41,2):
    for j in range(-1,39,2):
        if j<7 or j >29 or i<8 or i>31:
            add_tree([i,j])
            #print(i,j)



def refresh():
    global screen
    global Grass_ground
    global Player_location
    global x
    global y
    global Dynamicstate_point
    global press

    Dynamicstate_point +=1


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type==pygame.KEYDOWN and player.Clock == 0:
            if event.key==K_w:
                press = True
                if player.Direction == 1 and Player_location[1]>6:
                    Player_location[1]-=1
                    y = -1
                    x = 0
                else:
                    player.Direction = 1    
                player.Clock = 9
            elif event.key==K_a:
                press = True
                if player.Direction == 2 and Player_location[0]>8:
                    Player_location[0]-=1
                    y = 0
                    x = -1
                else:
                    player.Direction = 2
                player.Clock = 9
            elif event.key==K_s:
                press = True
                if player.Direction == 0 and 29>Player_location[1]:
                    Player_location[1]+=1
                    y = 1
                    x = 0
                else:
                    player.Direction = 0
                player.Clock = 9
            elif event.key==K_d:
                press = True
                if player.Direction == 3 and 31>Player_location[0]:
                    Player_location[0]+=1
                    y = 0
                    x = 1
                else:
                    player.Direction = 3
                player.Clock = 9


        if event.type==pygame.KEYUP:
                if event.key==pygame.K_w:
                    press=False                 
                elif event.key==pygame.K_a:
                    press=False
                elif event.key==pygame.K_s:
                    press=False
                elif event.key==pygame.K_d:
                    press=False


    
    #连续方向键前进
    if press == True and player.Clock == 0:
        player.Clock = 9

        if player.Direction == 1 and Player_location[1]>6:
            Player_location[1]-=1
            y = -1
            x = 0
 
        if player.Direction == 2 and Player_location[0]>8:
            Player_location[0]-=1
            y = 0
            x = -1

        if player.Direction == 0 and 29>Player_location[1]:
            Player_location[1]+=1
            y = 1
            x = 0

        if player.Direction == 3 and 31>Player_location[0]:
            Player_location[0]+=1
            y = 0
            x = 1

    pianyi = 6*player.Clock
    #加载草插图
    for i in range(11):
        for j in range(-2,17):
            if len((Map[Player_location[0]-7+j][Player_location[1]-5+i][0]).Image)==1 :
                screen.blit((Map[Player_location[0]-7+j][Player_location[1]-5+i][0]).Image[0],[j*60+x*pianyi,i*60+y*pianyi])
            else:
                #print((Dynamicstate_point%4+1)%2+2*((Dynamicstate_point%4+1)//4))
                screen.blit((Map[Player_location[0]-7+j][Player_location[1]-5+i][0]).Image[(Dynamicstate_point%36//9+1)%2+2*((Dynamicstate_point%36//9+1)//4)],[j*60+x*pianyi,i*60+y*pianyi])


    for i in range(-2,17):
        for j in range(-2,17):
            #加载人物插图
            if i==7 and j==4:
                if player.Clock ==0 :
                    screen.blit(player.Image[player.Direction][0],[7*60,4*60])
                    x=0
                    y=0
                else:
                    player.Clock -=1
                    screen.blit(player.Image[player.Direction][1+player.Point%2],[7*60,4*60])
                    if player.Clock == 0:
                        player.Point +=1
                  
            #加载边界树插图
            if  Map[Player_location[0]-7+j][Player_location[1]-5+i][1] == 'tree_image':
                screen.blit(Tree,[j*60+x*pianyi,(i-1)*60+y*pianyi])

    

    
    

while 1: 
    refresh() 

    pygame.display.flip()

    pygame.time.delay(30)

    
    


    




        
