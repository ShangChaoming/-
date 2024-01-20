import pygame
import random
from Bullet import Bullet
from config import *
from Bomb import Bomb



class EnemyPlane:
    def __init__(self,scene,speed=5):
        self.scene=scene
        self.image=pygame.image.load(f'source\\plane\\enemy-{random.randint(1,7)}.png')
        self.bbox=self.image.get_rect()
        self.speed=speed
        self.visible=False
        self.bullet=Bullet(scene,True)
        self.bomb=Bomb(scene)
    def calc_position(self):
        if self.visible:
            self.bbox.move_ip(0,self.speed)
            if self.bbox[1]>SCRENN_H:
                self.set_unused()
        if self.bullet.visible:
            self.bullet.move(0,self.speed+3)
        self.bomb.switch_frame()

    def draw_element(self):
        if self.visible:
            self.scene.blit(self.image, self.bbox)
        if self.bullet.visible:
            self.bullet.draw_element()
        self.bomb.draw_element()
    def set_unused(self):
        self.visible=False
        self.bbox[0]=-1000
        self.bbox[1]=-1000


    def set_used(self,start_x,start_y):
        self.visible=True
        self.bbox[0]=start_x
        self.bbox[1]=start_y
        self.speed = random.randint(4, 8)
    def shoot(self):
        if self.bullet.visible:
            return
        start_x=self.bbox[0]+self.bbox[2]/2-self.bullet.bbox[2]/2
        start_y=self.bbox[1]+self.bbox[3]/2-10
        self.bullet.set_used(start_x,start_y)

if __name__ == '__main__':
    pygame.init()
    window=pygame.display.set_mode([512,768])
    clock=pygame.time.Clock()
    enemy_plane=EnemyPlane(window)
    enemy_plane.set_used(random.randint(0,SCRENN_W-enemy_plane.bbox[2]),-enemy_plane.bbox[3])
    index=0
    while True:
        window.fill((0,0,0))
        enemy_plane.calc_position()
        enemy_plane.draw_element()
        index+=1
        if index>120 and enemy_plane.bbox[1]<100 and random.randint(1,100)>50:
            enemy_plane.shoot()
        if not enemy_plane.visible:
            enemy_plane.set_used(random.randint(0,SCRENN_W-enemy_plane.bbox[2]),-enemy_plane.bbox[3])
        pygame.event.get()
        pygame.display.update()
        clock.tick(60)







