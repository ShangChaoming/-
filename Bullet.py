import pygame
from config import *
class Bullet:
    def __init__(self,scene,is_enemy=False):
        self.scene=scene
        self.visible=False
        bullet_index=ENEMY_BULLET_INDEX if is_enemy else HERRO_BULLET_INDEX
        bullet_filename=f'source\\bullet\\bullet_{bullet_index}.png'
        self.image=pygame.image.load(bullet_filename)
        if is_enemy:
            self.image=pygame.transform.flip(self.image,False,True)
        self.bbox=self.image.get_rect()
    def draw_element(self):
        if not self.visible:
            return
        self.scene.blit(self.image,self.bbox)
    def move(self,dx,dy):
        if not self.visible:
            return
        self.bbox.move_ip(dx,dy)
        if self.bbox[1]<0 or self.bbox[1]>SCRENN_H:
            self.set_unused()
    def set_used(self,start_x,start_y):
        self.visible=True
        self.bbox[0]=start_x
        self.bbox[1]=start_y
    def set_unused(self):
        self.visible=False
        self.bbox[0]=-1000
        self.bbox[1]=-1000


if __name__ == '__main__':
    pygame.init()
    window=pygame.display.set_mode([350,568])
    clock=pygame.time.Clock()
    bullet = Bullet(window)
    bullet.set_used(100, 500)

    while True:
        window.fill((0,0,0))
        bullet.move(0,-5)
        bullet.draw_element()
        if not bullet.visible:
            bullet.set_used(100,500)





        pygame.display.update()
        pygame.event.get()
        clock.tick(60)


