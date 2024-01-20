import pygame

class Bomb:
    def __init__(self,scene):
        self.scene=scene
        self.images=[pygame.image.load(f'source\\bomb\\bomb-{index}.png') for index in range(1,7)]
        self.position=[0,0]
        self.visible=False
        self.draw_index=0
        self.interval=5
        self.interval_index=0
        self.sound=pygame.mixer.Sound(r'source\\music\\bomb.wav')
        self.sound.set_volume(0.1)
    def set_unused(self):
        self.visible=False
        self.position[0]=-1000
        self.position[1]=-1000


    def switch_frame(self):
        if self.visible==False:
            return
        self.interval_index+=1
        if self.interval_index<self.interval:
            return
        self.interval_index=0
        self.draw_index+=1
        if self.draw_index>=len(self.images):
            self.set_unused()
    def draw_element(self):
        if self.visible==False:
            return
        self.scene.blit(self.images[self.draw_index],self.position)
    def set_used(self,start_x,start_y):
        self.visible=True
        self.draw_index=0
        self.position[0]=start_x
        self.position[1]=start_y
        self.sound.play()
if __name__ == '__main__':
    pygame.init()
    window=pygame.display.set_mode([512,768])
    bomb=Bomb(window)
    clock=pygame.time.Clock()
    bomb.set_used(300,400)
    while True:
        window.fill((0,0,0))
        bomb.switch_frame()
        bomb.draw_element()
        if bomb.visible==False:
            bomb.set_used(300,400)


        pygame.event.get()
        pygame.display.update()
        clock.tick(60)






