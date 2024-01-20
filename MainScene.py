import pygame
from config import *
from GameMap import GameMap
from HeroPlane import HeroPlane
from EnemyManager import EnemyManager
import sys



class MainScene:
    def __init__(self):
        pygame.init()
        self.scene = pygame.display.set_mode([SCRENN_W, SCRENN_H])
        pygame.display.set_caption('飞机大战')
        self.clock = pygame.time.Clock()
        self.init_elements()
        self.defeat_count = 0
        self.damage_count = 0
        self.impact_count = 0
        pygame.mixer.music.load(r'source\\music\\bg.wav')
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)

    def init_elements(self):
        self.map = GameMap(self.scene)
        self.hero = HeroPlane(self.scene)
        self.enemy = EnemyManager(self.scene)

    def detect_colision(self):
        for bullet in self.hero.bullets.bullet_list:
            if bullet.visible == False:
                continue
            for ene in self.enemy.enemies:
                if not ene.visible:
                    continue
                if pygame.Rect.colliderect(bullet.bbox, ene.bbox):
                    ene.bomb.set_used(ene.bbox[0], ene.bbox[1])
                    bullet.set_unused()
                    ene.set_unused()
                    self.defeat_count += 1

        for ene in self.enemy.enemies:
            if not ene.visible:
                continue
            if pygame.Rect.colliderect(ene.bullet.bbox, self.hero.bbox):
                ene.bullet.set_unused()
                self.damage_count += 1
        for bullet in self.hero.bullets.bullet_list:
            if bullet.visible == False:
                continue
            for ene in self.enemy.enemies:
                if ene.visible == False:
                    continue
                if pygame.Rect.colliderect(ene.bullet.bbox, bullet.bbox):
                    ene.bullet.set_unused()
                    bullet.set_unused()
        for enemy in self.enemy.enemies:
            if not enemy.visible:
                continue
            if pygame.Rect.colliderect(enemy.bbox, self.hero.bbox):
                enemy.bomb.set_used(enemy.bbox[0], enemy.bbox[1])
                enemy.set_unused()
                self.impact_count += 1


    def draw_battle_data(self):
        font = pygame.font.Font(r'source\\fonts\\SimHei.ttf', 16)
        text = f'击毁数：{self.defeat_count}  被击中：{self.damage_count}  碰撞数：{self.impact_count}'
        text = font.render(text, True, (255, 255, 255))
        self.scene.blit(text, (150, 20))

    def calc_position(self):
        self.map.calc_position()
        self.hero.calc_position()
        self.enemy.calc_position()

    def draw_element(self):
        self.map.draw_element()
        self.hero.draw_element()
        self.enemy.draw_element()
        self.draw_battle_data()

    def handle_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            if event.type == EnemyManager.ENEMY_START_EVNET:
                self.enemy.set_out()
            if event.type == EnemyManager.ENEMY_SHOOT_EVNET:
                self.enemy.shoot()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_j]:
            self.hero.shoot(1)
        if keys[pygame.K_k]:
            self.hero.shoot(3)
        if keys[pygame.K_l]:
            self.hero.shoot(5)
        if keys[pygame.K_w]:
            self.hero.top()
        if keys[pygame.K_s]:
            self.hero.bottom()
        if keys[pygame.K_a]:
            self.hero.left()
        if keys[pygame.K_d]:
            self.hero.right()

    def run(self):
        while True:
            self.detect_colision()
            self.calc_position()
            self.draw_element()
            self.handle_events()
            pygame.display.update()
            self.clock.tick(60)
