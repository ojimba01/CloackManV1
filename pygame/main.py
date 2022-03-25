import pygame
### The star (*) simply is saying "all", so it is importing all the content of the file
from sprites import *
from config import *
import sys
class Game:
    def __init__(self):
        pygame.init()
        #pygame.init() is simply initializing pygame so it can be ran your system
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

        #self.screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
        #self.screen is setting up the window of the pygame program
        self.clock = pygame.time.Clock()
        self.running = True

        self.character_i_right_spritesheet = Spritesheet("spritesheets/hero/herochar_idle_anim_strip_4.png")
        self.character_i_left_spritesheet = Spritesheet("spritesheets/hero/herochar_idle_anim_strip_4_left.png")
        self.character_m_right_spritesheet = Spritesheet("spritesheets/hero/herochar_run_anim_strip_right.png")
        self.character_m_left_spritesheet = Spritesheet("spritesheets/hero/herochar_run_anim_strip_left.png")

        self.background_spritesheet = Spritesheet("spritesheets/background/tileset.png")
        self.dirt_spritesheet = Spritesheet("spritesheets/background/tileset.png")
        self.sky_spritesheet = Spritesheet("spritesheets/background/background.png")



    def createTilemap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                if column == "B":
                    Block(self, j, i)
                if column == "P":
                    Player(self, j, i)
                if column == "G":
                    Dirt(self, j, i)
                #if column == ".":
                 #   sky2(self, j, i)




    def new(self):
        self.playing = True
        
        self.all_sprites = pygame.sprite.LayeredUpdates()
        #This is an object that contains all of the sprites within the game
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        self.createTilemap()

        


    def events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
    def update(self):
        #esstially all of the main game loop updates
        self.all_sprites.update()


    def draw(self):
        #self.screen.fill(SKY)
        #self.display = pygame.Surface((320,240))
        scene = pygame.image.load("spritesheets/background/background.png")
        full_scene = pygame.transform.scale(scene, (WIN_WIDTH, WIN_HEIGHT))
        self.screen.blit(full_scene,(0,0))
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        #actual game loop
        while self.playing:
            #this is currently true unless sys.exit
            self.events()
            self.update()
            self.draw()
            
        self.running = False

    def game_over(self):
        pass
    def intro_screen(self):
        pass

g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()

pygame.quit()
sys.exit
