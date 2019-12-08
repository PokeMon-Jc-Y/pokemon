import pygame


class Character(object):
    def __init__(self,Name,Image,Direction,Point,Clock):
        "角色姓名，角色贴图list，贴图指针（下次迈哪只脚），动作延时帧数"
        self.Name=Image
        self.Image=Image
        self.Direction=Direction
        self.Point = Point
        self.Clock = Clock
