import random
import pygame
import colorsys

class Bullet1: #총알1
    def __init__(self, x, y, to_x, to_y):
        self.pos = [x, y]
        self.to = [to_x, to_y]
        self.radius = 7
        self.color = [190,0,0] # 빨간색총알
        
    def update_and_draw(self, dt, screen):
        width, height = screen.get_size()
        self.pos[0] = (self.pos[0] + dt*self.to[0]) % width
        self.pos[1] = (self.pos[1] + dt*self.to[1]) % height # 총알이 화면 밖으로 나가면 다른쪽에서 나오게 해줌
        pos_int = (int(self.pos[0]), int(self.pos[1]))
        pygame.draw.circle(screen, self.color, pos_int, self.radius) 

class Bullet2:  #총알2
    def __init__(self, x, y, to_x, to_y):
        self.pos = [x, y]
        self.to = [to_x, to_y]
        self.radius = 13 #총알1보다 크기 좀 더 크게
        self.color = [0,200,0] #초록색 총알
        
    def update_and_draw(self, dt, screen):
        width, height = screen.get_size()
        self.pos[0] = (self.pos[0] + dt*self.to[0]) % width
        self.pos[1] = (self.pos[1] + dt*self.to[1]) % height
        pos_int = (int(self.pos[0]), int(self.pos[1]))
        pygame.draw.circle(screen, self.color, pos_int, self.radius) 

class Bullet3:
    def __init__(self, x, y, to_x, to_y):
        self.pos = [x, y]
        self.to = [to_x, to_y]
        self.radius = 30 #총알2보다도 더 크게
        self.color = [0,0,250] #파란색 총알
        
    def update_and_draw(self, dt, screen):
        width, height = screen.get_size()
        self.pos[0] = (self.pos[0] + dt*self.to[0]) % width
        self.pos[1] = (self.pos[1] + dt*self.to[1]) % height
        pos_int = (int(self.pos[0]), int(self.pos[1]))
        pygame.draw.circle(screen, self.color, pos_int, self.radius) 


