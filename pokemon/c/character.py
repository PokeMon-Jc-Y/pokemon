import pygame
from abc import ABCMeta, abstractmethod

class Character(object):
    __metaclass__=ABCMeta

    def __init__(self,Name,Image,Direction,Point,Clock,Poke_ball):
        "Character name, character map list, map pointer (which foot is next), action delay frames"
        self.Name=Image
        self.Image=Image
        self.Direction=Direction
        self.Point = Point
        self.Clock = Clock
        self.Poke_ball = Poke_ball


    @abstractmethod
    
    
    def p(self):
        print('p')
