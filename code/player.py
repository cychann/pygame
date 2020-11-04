import math
import pygame

class Player:
    nodamgetime = False #비행기를 깜빡이게 하는 시간 체크하기 위한 bool 변수
    
    def __init__(self, x, y):
        self.image = pygame.image.load('player.png')
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.pos = [x, y]
        self.to = [0, 0] # 가르키고 있는 방향
        self.acc = [0, 0]
        self.angle = 0
        self.life = 5 #생명력

    def draw(self, screen):
        if self.to == [-1, -1]: self.angle = 45
        elif self.to == [-1, 0]: self.angle = 90
        elif self.to == [-1, 1]: self.angle = 135
        elif self.to == [0, 1]: self.angle = 180
        elif self.to == [1, 1]: self.angle = -135
        elif self.to == [1, 0]: self.angle = -90
        elif self.to == [1, -1]: self.angle = -45
        elif self.to == [0, -1]: self.angle = 0

        if self.nodamgetime == False:   #이 변수가 False 일때만 출력하게 하면 True 일때는 출력이 안되므로 비행기를 깜박이게 구현할 수 있다.
            rotated = pygame.transform.rotate(self.image, self.angle) #회전
            calib_pos = (self.pos[0] - rotated.get_width()/2,
                    self.pos[1] - rotated.get_height()/2)
            screen.blit(rotated, calib_pos)
            
    
    def goto(self, x, y):
        self.to[0] += x
        self.to[1] += y

    def update(self, dt, screen):
        width, height = screen.get_size()
        self.pos[0] = self.pos[0] + dt*self.to[0]*0.6
        self.pos[1] = self.pos[1] + dt*self.to[1]*0.6 # 0.6을 곱해서 비행기의 속도 조절
        self.pos[0] = min(max(self.pos[0], 32), width-32)
        self.pos[1] = min(max(self.pos[1], 32), height-32)
