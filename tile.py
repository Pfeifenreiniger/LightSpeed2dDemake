
import pygame

SCREEN = pygame.display.set_mode((800, 600))

class Tile(pygame.sprite.Sprite):
    def __init__(self, color, row, column):
        super().__init__()
        self.color = color
        self.row = row
        self.column = column
        self.place()
        self.load_img()
        self.load_rect()
        self.active = False

    def place(self):
        if self.row == 1:
            self.y = 366
            if self.column == 1:
                self.x = 141
            elif self.column == 2:
                self.x = 228
            elif self.column == 3:
                self.x = 315
            elif self.column == 4:
                self.x = 402
            elif self.column == 5:
                self.x = 484
            elif self.column == 6:
                self.x = 565
        elif self.row == 2:
            self.y = 312
            if self.column == 1:
                self.x = 157
            elif self.column == 2:
                self.x = 239
            elif self.column == 3:
                self.x = 320
            elif self.column == 4:
                self.x = 402
            elif self.column == 5:
                self.x = 479
            elif self.column == 6:
                self.x = 556
        elif self.row == 3:
            self.y = 265
            if self.column == 1:
                self.x = 172
            elif self.column == 2:
                self.x = 249
            elif self.column == 3:
                self.x = 325
            elif self.column == 4:
                self.x = 402
            elif self.column == 5:
                self.x = 474
            elif self.column == 6:
                self.x = 547
        elif self.row == 4:
            self.y = 222
            if self.column == 1:
                self.x = 185
            elif self.column == 2:
                self.x = 257
            elif self.column == 3:
                self.x = 329
            elif self.column == 4:
                self.x = 402
            elif self.column == 5:
                self.x = 470
            elif self.column == 6:
                self.x = 539
        elif self.row == 5:
            self.y = 184
            if self.column == 1:
                self.x = 196
            elif self.column == 2:
                self.x = 265
            elif self.column == 3:
                self.x = 333
            elif self.column == 4:
                self.x = 402
            elif self.column == 5:
                self.x = 467
            elif self.column == 6:
                self.x = 533
        elif self.row == 6:
            self.y = 149
            if self.column == 1:
                self.x = 206
            elif self.column == 2:
                self.x = 271
            elif self.column == 3:
                self.x = 337
            elif self.column == 4:
                self.x = 401
            elif self.column == 5:
                self.x = 464
            elif self.column == 6:
                self.x = 526

    def load_rect(self):
        self.rect = self.img.get_rect(topleft=(self.x, self.y))
        self.rect = pygame.rect.Rect(round(self.x + self.rect.width/3), round(self.y + self.rect.height/6), self.rect.width/4, self.rect.height/6)

    def load_img(self):
        self.img = pygame.image.load(f"graphics/tiles/{self.color}/r{self.row}c{self.column}.png").convert_alpha()

    def draw(self):
        if self.active:
            SCREEN.blit(self.img, (self.x, self.y))
            #pygame.draw.rect(SCREEN, (000, 000, 000), self.rect)

    def destroy(self):
        self.kill()
