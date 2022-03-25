import pygame
from config import *
from sprites import *
import math
import random

class Spritesheet:
    def __init__(self, file):

        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):

        sprite = pygame.Surface([width,height])

        sprite.blit(self.sheet, (0,0), (x,y,width,height))
        sprite.set_colorkey(BLACK)
        
        return sprite


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0
        self.y_change = 0

        self.facing = "right"
        self.animation_loop = 1

        self.image = self.game.character_i_right_spritesheet.get_sprite(0,0,self.width,self.height)
        #self.image = pygame.Surface([self.width, self.height])
        #self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    def animate(self):

        right_idle_animations = [self.game.character_i_right_spritesheet.get_sprite(0, 0, self.width, self.height),
                            self.game.character_i_right_spritesheet.get_sprite(16, 0, self.width, self.height),
                            self.game.character_i_right_spritesheet.get_sprite(32, 0, self.width, self.height),
                            self.game.character_i_right_spritesheet.get_sprite(48, 0, self.width, self.height),]

        left_idle_animations = [self.game.character_i_left_spritesheet.get_sprite(48, 0, self.width, self.height),
                            self.game.character_i_left_spritesheet.get_sprite(32, 0, self.width, self.height),
                            self.game.character_i_left_spritesheet.get_sprite(16, 0, self.width, self.height),
                            self.game.character_i_left_spritesheet.get_sprite(0, 0, self.width, self.height),]

        right_animations = [self.game.character_m_right_spritesheet.get_sprite(0, 0, self.width, self.height),
                            self.game.character_m_right_spritesheet.get_sprite(16, 0, self.width, self.height),
                            self.game.character_m_right_spritesheet.get_sprite(32, 0, self.width, self.height),
                            self.game.character_m_right_spritesheet.get_sprite(48, 0, self.width, self.height),
                            self.game.character_m_right_spritesheet.get_sprite(64, 0, self.width, self.height),
                            self.game.character_m_right_spritesheet.get_sprite(80, 0, self.width, self.height)]

        left_animations = [self.game.character_m_left_spritesheet.get_sprite(80, 0, self.width, self.height),
                           self.game.character_m_left_spritesheet.get_sprite(64, 0, self.width, self.height),
                           self.game.character_m_left_spritesheet.get_sprite(48, 0, self.width, self.height),
                           self.game.character_m_left_spritesheet.get_sprite(32, 0, self.width, self.height),
                           self.game.character_m_left_spritesheet.get_sprite(16, 0, self.width, self.height),
                           self.game.character_m_left_spritesheet.get_sprite(0, 0, self.width, self.height)]

        #up_animations = [self.game.character_spritesheet.get_sprite(3, 34, self.width, self.height),
        #                 self.game.character_spritesheet.get_sprite(35, 34, self.width, self.height),
         #                self.game.character_spritesheet.get_sprite(68, 34, self.width, self.height)]
        if self.facing == "right":
            if self.x_change == 0:
                self.image = right_idle_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.15
                if self.animation_loop >=3:
                    self.animation_loop = 1

            else:
                self.image = right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.15
                if self.animation_loop >=3:
                    self.animation_loop = 1
        if self.facing == "left":
            if self.x_change == 0:
                self.image = left_idle_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.15
                if self.animation_loop >=3:
                    self.animation_loop = 1

            else:
                self.image = left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.15
                if self.animation_loop >=3:
                    self.animation_loop = 1


    def update(self):
        self.movement()
        self.animate()
        self.rect.x +=self.x_change
        self.x_change = 0
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x_change -= PLAYER_SPEED
            self.facing = "left"

        if keys[pygame.K_RIGHT]:
            self.x_change += PLAYER_SPEED
            self.facing = "right"
class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self,self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.background_spritesheet.get_sprite(16,0,self.width,self.height)
        

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Dirt(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = DIRT_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self,self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.dirt_spritesheet.get_sprite(16,16,self.width,self.height)
        

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


