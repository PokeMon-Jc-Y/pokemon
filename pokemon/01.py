import pygame
import c.terrain
import c.character
from pygame.locals import *

screen=pygame.display.set_mode([900,600])
Map = []

Grass_ground = c.terrain.Terrain(pygame.image.load('image/grass.jpg').convert_alpha(),"ground")
Grass_ground1 = c.terrain.Terrain(pygame.image.load('image/grass1.jpg').convert_alpha(),"ground")

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

for i in range(40):
    row=[]
    for j in range(40):
        row.append([Grass_ground,''])
    Map.append(row)

Player_location = [10,10]

def add_tree(location):
    Map[location[0]][location[1]-1][1] = 'tree_image'
    Map[location[0]][location[1]][1] = 'tree'
    Map[location[0]][location[1]+1][1] = 'tree'
    Map[location[0]+1][location[1]][1] = 'tree'
    Map[location[0]+1][location[1]+1][1] = 'tree'

for i in range(0,39,2):
    for j in range(-1,39,2):
        if j<7 or j >29 or i<8 or i>31:
            add_tree([i,j])
            #print(i,j)



def refresh():
    global screen
    global Grass_ground
    global Player_location
    pianyi = 6*player.Clock
    if player.Direction == 0 or player.Direction == 1:
        y = (player.Direction-0.5)*2
        x = 0
    else:
        y = 0
        x = (player.Direction-2.5)*2

    for i in range(11):
        for j in range(0,15):
            screen.blit((Map[Player_location[0]-7+j][Player_location[1]-5+i][0]).Image,[j*60+x*pianyi,i*60+y*pianyi])

    for i in range(-1,15):
        for j in range(-1,15):
            if  Map[Player_location[0]-7+j][Player_location[1]-5+i][1] == 'tree_image':
                screen.blit(Tree,[j*60+x*pianyi,(i-1)*60+y*pianyi])

    if player.Clock ==0 :
        screen.blit(player.Image[player.Direction][0],[7*60,4*60])
    else:
        player.Clock -=1
        screen.blit(player.Image[player.Direction][1+player.Point%2],[7*60,4*60])
        if player.Clock == 0:
            player.Point +=1
    

while 1: 
    refresh() 

    pygame.display.flip()

    pygame.time.delay(20)

    
    


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type==pygame.KEYDOWN and player.Clock == 0:
            if event.key==K_w:
                if player.Direction == 1 and Player_location[1]>8:
                    Player_location[1]-=1
                else:
                    player.Direction = 1
                player.Clock = 10
            elif event.key==K_a:
                if player.Direction == 2 and Player_location[0]>8:
                    Player_location[0]-=1
                else:
                    player.Direction = 2
                player.Clock = 10
            elif event.key==K_s:
                if player.Direction == 0 and 31>Player_location[1]:
                    Player_location[1]+=1
                else:
                    player.Direction = 0
                player.Clock = 10
            elif event.key==K_d:
                if player.Direction == 3 and 31>Player_location[0]:
                    Player_location[0]+=1
                else:
                    player.Direction = 3
                player.Clock = 10




        
