import pygame
from config import *
import random
class GameMap:
    def __init__(self,scene):
        self.scene=scene
        map_index=MAP_INDEX if MAP_INDEX>=1 and MAP_INDEX<=5 else random.randint(1,5)
        filename=f'source\map\map-{map_index}.jpg'
        self.image1=pygame.image.load(filename)
        self.image2=self.image1.copy()
        self.y1=0
        self.y2=-SCRENN_H
        self.scroll_screen=2


    def draw_element(self):
        self.scene.blit(self.image1,(0,self.y1))
        self.scene.blit(self.image2,(0,self.y2))
    def calc_position(self):
        self.y1+=self.scroll_screen
        if self.y1>=SCRENN_H:
            self.y1=0
        self.y2+=self.scroll_screen
        if self.y2>=0:
            self.y2=-SCRENN_H


