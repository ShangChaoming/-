from EnemyPlane import EnemyPlane
import pygame, random
from config import *


class EnemyManager:
    ENEMY_START_EVNET = pygame.USEREVENT + 1
    ENEMY_SHOOT_EVNET = pygame.USEREVENT + 2

    def __init__(self, scene):
        self.enemies = [EnemyPlane(scene) for _ in range(8)]
        pygame.time.set_timer(EnemyManager.ENEMY_START_EVNET,2000)
        pygame.time.set_timer(EnemyManager.ENEMY_SHOOT_EVNET, 1000)

    def calc_position(self):
        for enemy in self.enemies:
            enemy.calc_position()

    def draw_element(self):
        for enemy in self.enemies:
            enemy.draw_element()

    def set_out(self):
        number = random.randint(1, 4)
        wait_for_out = []
        for enemy in self.enemies:
            if not enemy.visible:
                wait_for_out.append(enemy)
            if len(wait_for_out) == number:
                break
        position_xs = []
        if len(wait_for_out) == number:
            range_distance = int((SCRENN_W - 100) / number)
            for index in range(number):
                x = random.randint(index * range_distance, index * range_distance + range_distance - 100)
                position_xs.append(x)
        for enemy, x in zip(wait_for_out, position_xs):
            enemy.set_used(x, -enemy.bbox[3])

    def shoot(self):
        for enemy in self.enemies:
            if not enemy.visible:
                continue
            if enemy.bbox[1] < 200:
                enemy.shoot()
if __name__ == '__main__':
    pygame.init()
    window = pygame.display.set_mode([512, 768])
    clock = pygame.time.Clock()
    enemies=EnemyManager(window)
    while True:
        window.fill((0,0,0))
        enemies.calc_position()
        enemies.draw_element()
        events=pygame.event.get()
        for event in events:
            if event.type==EnemyManager.ENEMY_START_EVNET:
                enemies.set_out()
            if event.type==EnemyManager.ENEMY_SHOOT_EVNET:
                enemies.shoot()

        pygame.display.update()
        clock.tick(60)