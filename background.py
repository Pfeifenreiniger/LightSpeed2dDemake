
import pygame, random

SCREEN = pygame.display.set_mode((800, 600))

class Background:
    def __init__(self):
        self.load_assets()

    def load_assets(self):
        self.bg_1 = pygame.image.load("graphics/bg/bg_1.png").convert_alpha()
        self.bg_2 = pygame.image.load("graphics/bg/bg_2.png").convert_alpha()

        self.spectators_up = [
            Spectator("up", 1),
            Spectator("up", 2),
            Spectator("up", 3),
            Spectator("up", 4)
        ]
        self.spectators_left = [
            Spectator("left", 1),
            Spectator("left", 2),
            Spectator("left", 3),
            Spectator("left", 4)
        ]
        self.spectators_right = [
            Spectator("right", 1),
            Spectator("right", 2),
            Spectator("right", 3),
            Spectator("right", 4)
        ]
        self.spectators_down = [
            Spectator("down", 1),
            Spectator("down", 2),
            Spectator("down", 3),
            Spectator("down", 4)
        ]

    def draw_assets(self):
        SCREEN.blit(self.bg_1, (0, 0))
        for spectator in self.spectators_up:
            spectator.draw_assets()
        SCREEN.blit(self.bg_2, (341, 67))
        for spectator in self.spectators_left:
            spectator.draw_assets()
        for spectator in self.spectators_right:
            spectator.draw_assets()
        for spectator in self.spectators_down:
            spectator.draw_assets()


class LightColumn:
    def __init__(self, location):
        self.location = location
        if self.location == "up":
            self.x = 212
            self.y = 85
        elif self.location == "left":
            self.x = 32
            self.y = 338
        elif self.location == "right":
            self.x = 604
            self.y = 128
        elif self.location == "down":
            self.x = 575
            self.y = 408
        self.frame_counter = 0
        self.frames_up = True
        self.load_assets()

    def load_assets(self):
        self.frames = [
            pygame.image.load(f"graphics/bg/starfields_light_column/{self.location}/f1.png").convert_alpha(),
            pygame.image.load(f"graphics/bg/starfields_light_column/{self.location}/f2.png").convert_alpha(),
            pygame.image.load(f"graphics/bg/starfields_light_column/{self.location}/f3.png").convert_alpha(),
            pygame.image.load(f"graphics/bg/starfields_light_column/{self.location}/f4.png").convert_alpha()
        ]

    def animation(self):
        if self.frames_up:
            if round(self.frame_counter + 0.5) > 3:
                self.frames_up = False
            else:
                self.frame_counter += 0.5
        else:
            if round(self.frame_counter - 0.5) < 0:
                self.frames_up = True
            else:
                self.frame_counter -= 0.5

    def draw_assets(self):
        self.animation()
        SCREEN.blit(self.frames[round(self.frame_counter)], (self.x, self.y))

class Spectator:
    def __init__(self, location, no):
        self.location = location
        self.no = no
        self.frame_counter = random.randint(0,3)
        if self.location == "up":
            self.y = 60
            if self.no == 1:
                self.x = 353
            elif self.no == 2:
                self.x = 428
            elif self.no == 3:
                self.x = 483
            elif self.no == 4:
                self.x = 538
        elif self.location == "left":
            if self.no == 1:
                self.x = 31
                self.y = 255
            elif self.no == 2:
                self.x = 51
                self.y = 198
            elif self.no == 3:
                self.x = 73
                self.y = 144
            elif self.no == 4:
                self.x = 93
                self.y = 101
        elif self.location == "right":
            if self.no == 1:
                self.x = 770
                self.y = 354
            elif self.no == 2:
                self.x = 752
                self.y = 306
            elif self.no == 3:
                self.x = 734
                self.y = 262
            elif self.no == 4:
                self.x = 716
                self.y = 221
        elif self.location == "down":
            self.y = 500
            if self.no == 1:
                self.x = 58
            elif self.no == 2:
                self.x = 168
            elif self.no == 3:
                self.x = 278
            elif self.no == 4:
                self.x = 388
        self.load_assets()
        self.scale_assets()
        if self.location == "up":
            self.sleeping = False
            self.sleep_frames = 300

    def load_assets(self):
        self.frames = [
            pygame.image.load(f"graphics/bg/spectators/{self.location}/f1.png").convert_alpha(),
            pygame.image.load(f"graphics/bg/spectators/{self.location}/f2.png").convert_alpha(),
            pygame.image.load(f"graphics/bg/spectators/{self.location}/f3.png").convert_alpha(),
            pygame.image.load(f"graphics/bg/spectators/{self.location}/f4.png").convert_alpha()
        ]

    def scale_assets(self):
        if self.location == "left":
            if self.no == 2:
                for i in range(4):
                    self.frames[i] = pygame.transform.smoothscale(self.frames[i], (36, 38))
            elif self.no == 3:
                for i in range(4):
                    self.frames[i] = pygame.transform.smoothscale(self.frames[i], (34, 36))
            elif self.no == 4:
                for i in range(4):
                    self.frames[i] = pygame.transform.smoothscale(self.frames[i], (32, 34))
        elif self.location == "right":
            if self.no == 1:
                for i in range(4):
                    self.frames[i] = pygame.transform.smoothscale(self.frames[i], (40, 42))
            elif self.no == 3:
                for i in range(4):
                    self.frames[i] = pygame.transform.smoothscale(self.frames[i], (36, 38))
            elif self.no == 4:
                for i in range(4):
                    self.frames[i] = pygame.transform.smoothscale(self.frames[i], (34, 36))

    def falls_asleep(self):
        if self.location == "up":
            if self.sleeping != True:
                if random.randint(0, 100) == 0:
                    self.sleeping = True
                    self.sleep_frames = 300
                    self.frames = [
                        pygame.image.load(f"graphics/bg/spectators/{self.location}/sleep/f1.png").convert_alpha(),
                        pygame.image.load(f"graphics/bg/spectators/{self.location}/sleep/f2.png").convert_alpha(),
                        pygame.image.load(f"graphics/bg/spectators/{self.location}/sleep/f3.png").convert_alpha(),
                        pygame.image.load(f"graphics/bg/spectators/{self.location}/sleep/f2.png").convert_alpha()
                    ]
            else:
                if self.sleep_frames - 1 < 0:
                    self.sleeping = False
                    self.load_assets()
                else:
                    self.sleep_frames -= 1

    def animation(self):
        if round(self.frame_counter + 0.1) > 3:
            self.frame_counter = 0
        else:
            self.frame_counter += 0.1

    def draw_assets(self):
        self.animation()
        self.falls_asleep()
        SCREEN.blit(self.frames[round(self.frame_counter)], (self.x, self.y))
