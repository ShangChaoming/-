import pygame
from Bullet import Bullet
import math
from config import *


class BulletHero:
    def __init__(self, scene):
        self.bullet_list = [Bullet(scene) for _ in range(BULLETS)]
        self.frame_limit = 10
        self.frame_index = 0

    def calc_position(self):
        for bullet in self.bullet_list:
            bullet.move(0, -7)

    def draw_element(self):
        for bullet in self.bullet_list:
            bullet.draw_element()

    def shoot(self, start_x, start_y, shoot_number):
        self.frame_index += 1
        if self.frame_index < self.frame_limit:
            return
        self.frame_index = 0
        distance = 31
        middle = math.floor(shoot_number/2)
        position_xs = [start_x + (index - middle) * distance for index in range(shoot_number)]

        wait_for_shoot = []
        for bullet in self.bullet_list:
            if not bullet.visible:
                wait_for_shoot.append(bullet)
            if len(wait_for_shoot) == shoot_number:
                break
        if len(wait_for_shoot) == shoot_number:
            for bullet, x in zip(wait_for_shoot, position_xs):
                bullet.set_used(x - bullet.bbox[2] / 2, start_y - bullet.bbox[3])


if __name__ == '__main__':
    pygame.init()
    window = pygame.display.set_mode([350, 568])
    pygame.display.set_caption('飞机大战')
    clock = pygame.time.Clock()
    bullets = BulletHero(window)

    while True:
        window.fill((0, 0, 0))
        bullets.calc_position()
        bullets.draw_element()

        bullets.shoot(200, 500, 5)

        pygame.event.get()
        pygame.display.update()
        clock.tick(60)
