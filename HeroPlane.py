import pygame
from config import *
from BulletHero import BulletHero

class HeroPlane:
    def __init__(self, scene):
        self.scene = scene
        self.image = pygame.image.load(r'source\\plane\\hero.png')
        self.bbox = self.image.get_rect()
        self.bbox[0] = SCRENN_W / 2 - self.bbox[2]/2
        self.bbox[1] = SCRENN_H-self.bbox[3] - 10
        self.speed=5
        self.bullets=BulletHero(scene)
    def top(self):
        if self.bbox[1]<=0:
            return
        self.bbox.move_ip(0,-self.speed)

    def bottom(self):
        if self.bbox[1] >= SCRENN_H-self.bbox[3]:
            return

        self.bbox.move_ip(0, self.speed)

    def left(self):
        if self.bbox[0]<=0:
            return
        self.bbox.move_ip(-self.speed,0)
    def right(self):
        if self.bbox[0]>=SCRENN_W-self.bbox[2]:
            return
        self.bbox.move_ip(self.speed,0)

    def shoot(self,num):
        start_x=self.bbox[0]+self.bbox[2]/2
        start_y=self.bbox[1]
        self.bullets.shoot(start_x,start_y,num)
    def draw_element(self):
        self.scene.blit(self.image,self.bbox)
        self.bullets.draw_element()
    def calc_position(self):
        self.bullets.calc_position()

if __name__ == '__main__':
    pygame.init()
    window=pygame.display.set_mode([512,768])
    pygame.display.set_caption('飞机大战')
    clock=pygame.time.Clock()
    hero=HeroPlane(window)


    while True:
        window.fill((0,0,0))
        hero.calc_position()
        hero.draw_element()
        hero.shoot(3)
        pygame.event.get()


        pygame.display.update()
        clock.tick(60)

