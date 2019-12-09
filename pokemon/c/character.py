import pygame
from abc import ABCMeta, abstractmethod

class Character(object):
    __metaclass__=ABCMeta

    def __init__(self,Name,Image,Direction,Point,Clock,Poke_ball):
        "角色姓名，角色贴图list，贴图指针（下次迈哪只脚），动作延时帧数"
        self.Name=Image
        self.Image=Image
        self.Direction=Direction
        self.Point = Point
        self.Clock = Clock
        self.Poke_ball = Poke_ball


    @abstractmethod
    
    
    def p(self):
        print('p')
