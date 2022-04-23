import sys
import pygame as pg

pg.init()

FPS = 60

WIDTH, HEIGTH = 600, 500
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

players_speed = 7
PLAYER_COLOR = BLUE

MOB_WIDTH, MOB_HEIGTH = 100, 100
MOB_COLOR = RED


class Game():
    def __init__(self):

        self.screen = pg.display.set_mode((WIDTH, HEIGTH), pg.DOUBLEBUF | pg.HWSURFACE)
        self.screen.fill(WHITE)
        pg.display.set_caption("Scavenger")
        #pg.display.set_icon(pg.image.load("resources/app.bmp"))
        self.clock = pg.time.Clock()       
        
    def run(self):

        flRunning = True       

        player_one = Player()
        mobs = create_Mob()

        while flRunning:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                    flRunning = False

            player_one.update()
            mobs.draw(self.screen)

            collisions(player_one, mobs)

            pg.display.update()
            self.clock.tick(FPS)


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        PLAYER_WIDTH, PLAYER_HEIGTH = 50, 50

        self.image  = pg.Surface((PLAYER_WIDTH, PLAYER_HEIGTH))
        self.image.fill(PLAYER_COLOR)
        self.mask  = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=(WIDTH/2, HEIGTH/2))

    def player_keys_input(self):

        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and self.rect.left>=0:
            self.rect.x = self.rect.x - players_speed            
        elif keys[pg.K_RIGHT] and self.rect.right<=WIDTH:            
            self.rect.x = self.rect.x + players_speed
        elif keys[pg.K_UP] and self.rect.y>=0:
            self.rect.y = self.rect.top - players_speed
        elif keys[pg.K_DOWN] and self.rect.bottom<=HEIGTH:
            self.rect.y = self.rect.y + players_speed        

    def update(self):

        self.player_keys_input()
        game.screen.fill(WHITE)
        game.screen.blit(self.image, self.rect)



class Mob(pg.sprite.Sprite):

    def __init__(self, pos_center=(100, 100), group=[]):
        super().__init__()

        self.image = pg.image.load('resources/green_circle.png').convert()
        self.image = pg.transform.scale(self.image, (50, 50))
        self.image.set_colorkey(BLACK)        
        self.mask  = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=pos_center)

        self.add(group)

    def update(self, player_one):
        pass


def create_Mob():
        mobs = pg.sprite.Group()

        mob_inst = Mob((100, 100), group=mobs)
        mob_inst2 = Mob((100, 400), group=mobs)
        mob_inst3 = Mob((400, 400), group=mobs)

        return mobs



class Interaction():
    def __init__(self, player, mobs):

        self.player = player
        self.mobs = mobs

    def collisions(self):

        if pg.sprite.collide_mask(player_one, mob_inst):
                print("333",mob_inst.rect, pg.sprite.collide_mask(player_one, mob_inst))
                return True


def collisions(player, mobs):
    for mob in mobs:
        if pg.sprite.collide_mask(player, mob):
            print("Mob catched!!!", pg.sprite.collide_mask(player, mob))
            mob.kill()



if __name__ == "__main__":
    game = Game()
    game.run()