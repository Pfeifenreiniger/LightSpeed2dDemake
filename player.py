
import pygame

#-----------------CONSTANTS-----------------#
SCREEN = pygame.display.set_mode((800, 600))

UP = "up"
LEFT = "left"
RIGHT = "right"
DOWN = "down"

P1_START_X = 35
P1_START_Y = 338
P2_START_X = 608
P2_START_Y = 119

PLAYER_SPRITE_ORIGINAL_SCALE = (84, 88)
SHADOW_SPRITE_ORIGINAL_SCALE = (96, 80)

ROW_0_LOWER_EDGE = 503
ROW_0_TO_1 = 422
ROW_1_TO_2 = 364
ROW_2_TO_3 = 311
ROW_3_TO_4 = 263
ROW_4_TO_5 = 221
ROW_5_TO_6 = 182
ROW_6_TO_7 = 144
ROW_6_UPPER_EDGE = 134
ROW_7_UPPER_EDGE = 95

ROW_1_COL_0_TO_1 = 149
ROW_1_COL_1_TO_2 = 232
ROW_1_COL_2_TO_3 = 315
ROW_1_COL_3_TO_4 = 400
ROW_1_COL_4_TO_5 = 485
ROW_1_COL_5_TO_6 = 568
ROW_1_COL_6_RIGHT_EDGE = 651

ROW_2_COL_1_LEFT_EDGE = 165
ROW_2_COL_1_TO_2 = 242
ROW_2_COL_2_TO_3 = 321
ROW_2_COL_3_TO_4 = 400
ROW_2_COL_4_TO_5 = 480
ROW_2_COL_5_TO_6 = 559
ROW_2_COL_6_RIGHT_EDGE = 636

ROW_3_COL_1_LEFT_EDGE = 178
ROW_3_COL_1_TO_2 = 251
ROW_3_COL_2_TO_3 = 325
ROW_3_COL_3_TO_4 = 400
ROW_3_COL_4_TO_5 = 475
ROW_3_COL_5_TO_6 = 549
ROW_3_COL_6_RIGHT_EDGE = 623

ROW_4_COL_1_LEFT_EDGE = 191
ROW_4_COL_1_TO_2 = 259
ROW_4_COL_2_TO_3 = 329
ROW_4_COL_3_TO_4 = 400
ROW_4_COL_4_TO_5 = 471
ROW_4_COL_5_TO_6 = 542
ROW_4_COL_6_RIGHT_EDGE = 611

ROW_5_COL_1_LEFT_EDGE = 201
ROW_5_COL_1_TO_2 = 266
ROW_5_COL_2_TO_3 = 333
ROW_5_COL_3_TO_4 = 400
ROW_5_COL_4_TO_5 = 467
ROW_5_COL_5_TO_6 = 534
ROW_5_COL_6_RIGHT_EDGE = 601

ROW_6_COL_1_LEFT_EDGE = 211
ROW_6_COL_1_TO_2 = 273
ROW_6_COL_2_TO_3 = 337
ROW_6_COL_3_TO_4 = 400
ROW_6_COL_4_TO_5 = 464
ROW_6_COL_5_TO_6 = 528
ROW_6_COL_6_TO_7 = 593

class Player(pygame.sprite.Sprite):
    def __init__(self, char, numb):
        super().__init__()
        self.char = char
        self.numb = numb
        self.player_reset()

    def load_imgs_down(self):
        self.down_imgs = [
            pygame.image.load(f"graphics/player/{self.char}/down/{self.char}_down_f1.png").convert_alpha(),
            pygame.image.load(f"graphics/player/{self.char}/down/{self.char}_down_f2.png").convert_alpha()
        ]

    def load_imgs_left(self):
        self.left_imgs = [
            pygame.image.load(f"graphics/player/{self.char}/left/{self.char}_left_f1.png").convert_alpha(),
            pygame.image.load(f"graphics/player/{self.char}/left/{self.char}_left_f2.png").convert_alpha()
        ]

    def load_imgs_right(self):
        self.right_imgs = [
            pygame.image.load(f"graphics/player/{self.char}/right/{self.char}_right_f1.png").convert_alpha(),
            pygame.image.load(f"graphics/player/{self.char}/right/{self.char}_right_f2.png").convert_alpha()
        ]

    def load_imgs_up(self):
        self.up_imgs = [
            pygame.image.load(f"graphics/player/{self.char}/up/{self.char}_up_f1.png").convert_alpha(),
            pygame.image.load(f"graphics/player/{self.char}/up/{self.char}_up_f2.png").convert_alpha()
        ]

    def load_img_shadow(self):
        self.shadow_img = pygame.image.load("graphics/player/shadow.png").convert_alpha()

    def load_current_imgs(self):
        if self.up:
            self.load_imgs_up()
            self.current_imgs = self.up_imgs
        elif self.left:
            self.load_imgs_left()
            self.current_imgs = self.left_imgs
        elif self.right:
            self.load_imgs_right()
            self.current_imgs = self.right_imgs
        elif self.down:
            self.load_imgs_down()
            self.current_imgs = self.down_imgs

    def load_rect(self):
        self.rect = pygame.rect.Rect(self.x, (round(self.y) + (round(self.img_scale[1]/4))), self.img_scale[0], round(self.img_scale[1]/1.5))

    def set_direction(self):
        self.up = False
        if self.numb == 2:
            self.left = True
        else:
            self.left = False
        if self.numb == 1:
            self.right = True
        else:
            self.right = False
        self.down = False

    def set_rows(self):
        self.row0 = False
        if self.numb == 1:
            self.row1 = True
        else: self.row1 = False
        self.row2 = False
        self.row3 = False
        self.row4 = False
        self.row5 = False
        if self.numb == 1:
            self.row6 = False
        else: self.row6 = True
        self.row7 = False

    def return_row_number(self):
        if self.row0:
            return 0
        elif self.row1:
            return 1
        elif self.row2:
            return 2
        elif self.row3:
            return 3
        elif self.row4:
            return 4
        elif self.row5:
            return 5
        elif self.row6:
            return 6
        elif self.row7:
            return 7

    def set_columns(self):
        if self.numb == 1:
            self.column0 = True
        else: self.column0 = False
        self.column1 = False
        self.column2 = False
        self.column3 = False
        self.column4 = False
        self.column5 = False
        self.column6 = False
        if self.numb == 2:
            self.column7 = True
        else: self.column7 = False

    def set_cells(self):
        """active cells which represent the player's current score"""
        self.cell_r1c1 = False  # row 1 column 1
        self.cell_r1c2 = False  # row 1 column 2
        self.cell_r1c3 = False  # row 1 column 3
        self.cell_r1c4 = False  # row 1 column 4
        self.cell_r1c5 = False
        self.cell_r1c6 = False
        self.cell_r2c1 = False
        self.cell_r2c2 = False
        self.cell_r2c3 = False
        self.cell_r2c4 = False
        self.cell_r2c5 = False
        self.cell_r2c6 = False
        self.cell_r3c1 = False
        self.cell_r3c2 = False
        self.cell_r3c3 = False
        self.cell_r3c4 = False
        self.cell_r3c5 = False
        self.cell_r3c6 = False
        self.cell_r4c1 = False
        self.cell_r4c2 = False
        self.cell_r4c3 = False
        self.cell_r4c4 = False
        self.cell_r4c5 = False
        self.cell_r4c6 = False
        self.cell_r5c1 = False
        self.cell_r5c2 = False
        self.cell_r5c3 = False
        self.cell_r5c4 = False
        self.cell_r5c5 = False
        self.cell_r5c6 = False
        self.cell_r6c1 = False
        self.cell_r6c2 = False
        self.cell_r6c3 = False
        self.cell_r6c4 = False
        self.cell_r6c5 = False
        self.cell_r6c6 = False

    def calculate_score(self):
        self.cells = [
            self.cell_r1c1,
            self.cell_r1c2,
            self.cell_r1c3,
            self.cell_r1c4,
            self.cell_r1c5,
            self.cell_r1c6,
            self.cell_r2c1,
            self.cell_r2c2,
            self.cell_r2c3,
            self.cell_r2c4,
            self.cell_r2c5,
            self.cell_r2c6,
            self.cell_r3c1,
            self.cell_r3c2,
            self.cell_r3c3,
            self.cell_r3c4,
            self.cell_r3c5,
            self.cell_r3c6,
            self.cell_r4c1,
            self.cell_r4c2,
            self.cell_r4c3,
            self.cell_r4c4,
            self.cell_r4c5,
            self.cell_r4c6,
            self.cell_r5c1,
            self.cell_r5c2,
            self.cell_r5c3,
            self.cell_r5c4,
            self.cell_r5c5,
            self.cell_r5c6,
            self.cell_r6c1,
            self.cell_r6c2,
            self.cell_r6c3,
            self.cell_r6c4,
            self.cell_r6c5,
            self.cell_r6c6
        ]
        for cell in self.cells:
            if cell == True:
                self.score += 1

    def scale_imgs(self):
        self.load_img_shadow()
        self.load_current_imgs()
        if self.row7:
            self.img_scale = (PLAYER_SPRITE_ORIGINAL_SCALE[0] - 32, PLAYER_SPRITE_ORIGINAL_SCALE[1] - 32)
            self.shadow_scale = (SHADOW_SPRITE_ORIGINAL_SCALE[0] - 32, SHADOW_SPRITE_ORIGINAL_SCALE[1] - 32)
        elif self.row6:
            self.img_scale = (PLAYER_SPRITE_ORIGINAL_SCALE[0] - 24, PLAYER_SPRITE_ORIGINAL_SCALE[1] - 24)
            self.shadow_scale = (SHADOW_SPRITE_ORIGINAL_SCALE[0] - 24, SHADOW_SPRITE_ORIGINAL_SCALE[1] - 24)
        elif self.row5:
            self.img_scale = (PLAYER_SPRITE_ORIGINAL_SCALE[0] - 18, PLAYER_SPRITE_ORIGINAL_SCALE[1] - 18)
            self.shadow_scale = (SHADOW_SPRITE_ORIGINAL_SCALE[0] - 18, SHADOW_SPRITE_ORIGINAL_SCALE[1] - 18)
        elif self.row4:
            self.img_scale = (PLAYER_SPRITE_ORIGINAL_SCALE[0] - 14, PLAYER_SPRITE_ORIGINAL_SCALE[1] - 14)
            self.shadow_scale = (SHADOW_SPRITE_ORIGINAL_SCALE[0] - 14, SHADOW_SPRITE_ORIGINAL_SCALE[1] - 14)
        elif self.row3:
            self.img_scale = (PLAYER_SPRITE_ORIGINAL_SCALE[0] - 8, PLAYER_SPRITE_ORIGINAL_SCALE[1] - 8)
            self.shadow_scale = (SHADOW_SPRITE_ORIGINAL_SCALE[0] - 8, SHADOW_SPRITE_ORIGINAL_SCALE[1] - 8)
        elif self.row2:
            self.img_scale = (PLAYER_SPRITE_ORIGINAL_SCALE[0] - 4, PLAYER_SPRITE_ORIGINAL_SCALE[1] - 4)
            self.shadow_scale = (SHADOW_SPRITE_ORIGINAL_SCALE[0] - 4, SHADOW_SPRITE_ORIGINAL_SCALE[1] - 4)
        elif self.row1:
            self.img_scale = (PLAYER_SPRITE_ORIGINAL_SCALE[0], PLAYER_SPRITE_ORIGINAL_SCALE[1])
            self.shadow_scale = (SHADOW_SPRITE_ORIGINAL_SCALE[0], SHADOW_SPRITE_ORIGINAL_SCALE[1])
        elif self.row0:
            self.img_scale = (PLAYER_SPRITE_ORIGINAL_SCALE[0] + 4, PLAYER_SPRITE_ORIGINAL_SCALE[1] + 4)
            self.shadow_scale = (SHADOW_SPRITE_ORIGINAL_SCALE[0] + 4, SHADOW_SPRITE_ORIGINAL_SCALE[1] + 4)
        self.current_imgs[0] = pygame.transform.smoothscale(self.current_imgs[0], self.img_scale)
        self.current_imgs[1] = pygame.transform.smoothscale(self.current_imgs[1], self.img_scale)
        self.shadow_img = pygame.transform.smoothscale(self.shadow_img, self.shadow_scale)

    def animation(self):
        if round(self.animation_counter + 0.1) > 1:
            self.animation_counter = 0
        else:
            self.animation_counter += 0.1

    def teleport_animation(self):
        self.x += self.img_scale[0] / 3
        self.img_scale = (self.img_scale[0] / 4, self.img_scale[1])
        self.current_imgs[0] = pygame.transform.smoothscale(self.current_imgs[0], self.img_scale)
        self.current_imgs[1] = pygame.transform.smoothscale(self.current_imgs[1], self.img_scale)
        self.draw_player()

    def draw_player(self):
        SCREEN.blit(self.shadow_img, (self.x - round(self.shadow_scale[0]/14), self.y + round(self.shadow_scale[1]/5)))
        SCREEN.blit(self.current_imgs[round(self.animation_counter)], (self.x, self.y))
        #pygame.draw.rect(SCREEN, (000, 000, 000), self.rect)
        #print(f"Player number {self.numb} at {self.rect.bottom}")

    def player_input(self):
        """Keyboard controls for up to two players simultaneously at one keyboard"""
        self.keys = pygame.key.get_pressed()
        # player 1: w a s d
        if self.numb == 1:
            if self.key_pressed != True:
                if self.keys[pygame.K_w] and ((self.row6 != True) or (self.row6 and self.column1)) and \
                        self.row7 != True:
                    self.up = True
                    self.left = False
                    self.right = False
                    self.down = False
                    self.key_direction = UP
                    self.key_pressed = True
                elif self.keys[pygame.K_a] and (((self.row2 or self.row3 or self.row4 or self.row5 or self.row6)
                                                 and self.column1 != True) or (self.row1 and self.column0 != True)):
                    self.up = False
                    self.left = True
                    self.right = False
                    self.down = False
                    self.key_direction = LEFT
                    self.key_pressed = True
                elif self.keys[pygame.K_s] and ((self.row1 != True) or (self.row1 and self.column6)) and \
                        self.row0 != True:
                    self.up = False
                    self.left = False
                    self.right = False
                    self.down = True
                    self.key_direction = DOWN
                    self.key_pressed = True
                elif self.keys[pygame.K_d] and (((self.row1 or self.row2 or self.row3 or self.row4 or self.row5)
                                                 and self.column6 != True) or (self.row6 and self.column7 != True)):
                    self.up = False
                    self.left = False
                    self.right = True
                    self.down = False
                    self.key_direction = RIGHT
                    self.key_pressed = True
        # player 2: arrow keys
        if self.numb == 2:
            if self.key_pressed != True:
                if self.keys[pygame.K_UP] and ((self.row6 != True) or (self.row6 and self.column1)) and \
                        self.row7 != True:
                    self.up = True
                    self.left = False
                    self.right = False
                    self.down = False
                    self.key_direction = UP
                    self.key_pressed = True
                elif self.keys[pygame.K_LEFT] and (((self.row2 or self.row3 or self.row4 or self.row5 or self.row6) and
                                                 self.column1 != True) or (self.row1 and self.column0 != True)):
                    self.up = False
                    self.left = True
                    self.right = False
                    self.down = False
                    self.key_direction = LEFT
                    self.key_pressed = True
                elif self.keys[pygame.K_DOWN] and ((self.row1 != True) or (self.row1 and self.column6)) and \
                        self.row0 != True:
                    self.up = False
                    self.left = False
                    self.right = False
                    self.down = True
                    self.key_direction = DOWN
                    self.key_pressed = True
                elif self.keys[pygame.K_RIGHT] and (((self.row1 or self.row2 or self.row3 or self.row4 or self.row5)
                                                 and self.column6 != True) or (self.row6 and self.column7 != True)):
                    self.up = False
                    self.left = False
                    self.right = True
                    self.down = False
                    self.key_direction = RIGHT
                    self.key_pressed = True

    def scale_move_speed(self):
        if self.row0 or self.row1 or self.row2 or self.row3:
            self.move_speed = 5
        elif self.row4 or self.row5 or self.row6 or self.row7:
            self.move_speed = 4

    def movement(self):
        if self.key_pressed:
            self.scale_move_speed()
            if self.key_direction == UP:
                if self.row0:
                    if self.rect.bottom - self.move_speed <= ROW_0_TO_1:
                        self.row0 = False
                        self.row1 = True
                        self.key_pressed = False
                        self.key_direction = ""
                        return
                elif self.row1:
                    if self.rect.bottom - self.move_speed <= ROW_1_TO_2:
                        self.row1 = False
                        self.row2 = True
                        self.key_pressed = False
                        self.key_direction = ""
                        return
                elif self.row2:
                    if self.rect.bottom - self.move_speed <= ROW_2_TO_3:
                        self.row2 = False
                        self.row3 = True
                        self.key_pressed = False
                        self.key_direction = ""
                        return
                elif self.row3:
                    if self.rect.bottom - self.move_speed <= ROW_3_TO_4:
                        self.row3 = False
                        self.row4 = True
                        self.key_pressed = False
                        self.key_direction = ""
                        return
                elif self.row4:
                    if self.rect.bottom - self.move_speed <= ROW_4_TO_5:
                        self.row4 = False
                        self.row5 = True
                        self.key_pressed = False
                        self.key_direction = ""
                        return
                elif self.row5:
                    if self.rect.bottom - self.move_speed <= ROW_5_TO_6:
                        self.row5 = False
                        self.row6 = True
                        self.key_pressed = False
                        self.key_direction = ""
                        return
                elif self.row6 and self.column1:
                    if self.rect.bottom - self.move_speed <= ROW_6_TO_7:
                        self.row6 = False
                        self.row0 = True
                        self.column1 = False
                        self.column6 = True
                        self.teleport_animation()
                        self.x = 584
                        self.y = 424
                        return
                elif self.row6:
                    if self.rect.top - self.move_speed <= ROW_6_UPPER_EDGE:
                        self.key_pressed = False
                        self.key_direction = ""
                        return
                if self.column1:
                    if self.row0 or self.row1 or self.row2 or self.row3:
                        self.x += 1.18
                    elif self.row4 or self.row5 or self.row6 or self.row7:
                        self.x += 1.5
                elif self.column2:
                    if self.row0 or self.row1 or self.row2 or self.row3:
                        self.x += 0.82
                    elif self.row4 or self.row5 or self.row6 or self.row7:
                        self.x += 0.9
                elif self.column3:
                    if self.row0 or self.row1 or self.row2 or self.row3:
                        self.x += 0.43
                    elif self.row4 or self.row5 or self.row6 or self.row7:
                        self.x += 0.5
                elif self.column4:
                    self.x -= 0.01
                elif self.column5:
                    if self.row0 or self.row1 or self.row2 or self.row3:
                        self.x -= 0.37
                    elif self.row4 or self.row5 or self.row6 or self.row7:
                        self.x -= 0.42
                elif self.column6:
                    if self.row0 or self.row1 or self.row2 or self.row3:
                        self.x -= 0.8
                    elif self.row4 or self.row5 or self.row6 or self.row7:
                        self.x -= 0.88
                self.y -= self.move_speed
            elif self.key_direction == LEFT:
                if self.row1:
                    if self.column6:
                        if self.rect.right - self.move_speed <= ROW_1_COL_5_TO_6:
                            self.column6 = False
                            self.column5 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column5:
                        if self.rect.right - self.move_speed <= ROW_1_COL_4_TO_5:
                            self.column5 = False
                            self.column4 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column4:
                        if self.rect.right - self.move_speed <= ROW_1_COL_3_TO_4:
                            self.column4 = False
                            self.column3 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column3:
                        if self.rect.right - self.move_speed <= ROW_1_COL_2_TO_3:
                            self.column3 = False
                            self.column2 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column2:
                        if self.rect.right - self.move_speed <= ROW_1_COL_1_TO_2:
                            self.column2 = False
                            self.column1 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column1:
                        if self.rect.right - self.move_speed <= ROW_1_COL_0_TO_1:
                            self.column1 = False
                            self.teleport_animation()
                            self.x = P2_START_X
                            self.y = P2_START_Y
                            self.row1 = False
                            self.row6 = True
                            self.column7 = True
                            return
                elif self.row2:
                    if self.column6:
                        if self.rect.right - self.move_speed <= ROW_2_COL_5_TO_6:
                            self.column6 = False
                            self.column5 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column5:
                        if self.rect.right - self.move_speed <= ROW_2_COL_4_TO_5:
                            self.column5 = False
                            self.column4 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column4:
                        if self.rect.right - self.move_speed <= ROW_2_COL_3_TO_4:
                            self.column4 = False
                            self.column3 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column3:
                        if self.rect.right - self.move_speed <= ROW_2_COL_2_TO_3:
                            self.column3 = False
                            self.column2 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column2:
                        if self.rect.right - self.move_speed <= ROW_2_COL_1_TO_2:
                            self.column2 = False
                            self.column1 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column1:
                        if self.rect.left - self.move_speed < ROW_2_COL_1_LEFT_EDGE:
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                elif self.row3:
                    if self.column6:
                        if self.rect.right - self.move_speed <= ROW_3_COL_5_TO_6:
                            self.column6 = False
                            self.column5 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column5:
                        if self.rect.right - self.move_speed <= ROW_3_COL_4_TO_5:
                            self.column5 = False
                            self.column4 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column4:
                        if self.rect.right - self.move_speed <= ROW_3_COL_3_TO_4:
                            self.column4 = False
                            self.column3 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column3:
                        if self.rect.right - self.move_speed <= ROW_3_COL_2_TO_3:
                            self.column3 = False
                            self.column2 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column2:
                        if self.rect.right - self.move_speed <= ROW_3_COL_1_TO_2:
                            self.column2 = False
                            self.column1 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column1:
                        if self.rect.left - self.move_speed < ROW_3_COL_1_LEFT_EDGE:
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                elif self.row4:
                    if self.column6:
                        if self.rect.right - self.move_speed <= ROW_4_COL_5_TO_6:
                            self.column6 = False
                            self.column5 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column5:
                        if self.rect.right - self.move_speed <= ROW_4_COL_4_TO_5:
                            self.column5 = False
                            self.column4 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column4:
                        if self.rect.right - self.move_speed <= ROW_4_COL_3_TO_4:
                            self.column4 = False
                            self.column3 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column3:
                        if self.rect.right - self.move_speed <= ROW_4_COL_2_TO_3:
                            self.column3 = False
                            self.column2 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column2:
                        if self.rect.right - self.move_speed <= ROW_4_COL_1_TO_2:
                            self.column2 = False
                            self.column1 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column1:
                        if self.rect.left - self.move_speed < ROW_4_COL_1_LEFT_EDGE:
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                elif self.row5:
                    if self.column6:
                        if self.rect.right - self.move_speed <= ROW_5_COL_5_TO_6:
                            self.column6 = False
                            self.column5 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column5:
                        if self.rect.right - self.move_speed <= ROW_5_COL_4_TO_5:
                            self.column5 = False
                            self.column4 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column4:
                        if self.rect.right - self.move_speed <= ROW_5_COL_3_TO_4:
                            self.column4 = False
                            self.column3 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column3:
                        if self.rect.right - self.move_speed <= ROW_5_COL_2_TO_3:
                            self.column3 = False
                            self.column2 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column2:
                        if self.rect.right - self.move_speed <= ROW_5_COL_1_TO_2:
                            self.column2 = False
                            self.column1 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column1:
                        if self.rect.left - self.move_speed < ROW_5_COL_1_LEFT_EDGE:
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                elif self.row6:
                    if self.column7:
                        if self.rect.right - self.move_speed <= ROW_6_COL_6_TO_7:
                            self.column7 = False
                            self.column6 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column6:
                        if self.rect.right - self.move_speed <= ROW_6_COL_5_TO_6:
                            self.column6 = False
                            self.column5 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column5:
                        if self.rect.right - self.move_speed <= ROW_6_COL_4_TO_5:
                            self.column5 = False
                            self.column4 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column4:
                        if self.rect.right - self.move_speed <= ROW_6_COL_3_TO_4:
                            self.column4 = False
                            self.column3 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column3:
                        if self.rect.right - self.move_speed <= ROW_6_COL_2_TO_3:
                            self.column3 = False
                            self.column2 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column2:
                        if self.rect.right - self.move_speed <= ROW_6_COL_1_TO_2:
                            self.column2 = False
                            self.column1 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column1:
                        if self.rect.left - self.move_speed < ROW_6_COL_1_LEFT_EDGE:
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                self.x -= self.move_speed
            elif self.key_direction == RIGHT:
                if self.row1:
                    if self.column6:
                        if self.rect.right + self.move_speed >= ROW_1_COL_6_RIGHT_EDGE:
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column5:
                        if self.rect.left + self.move_speed >= ROW_1_COL_5_TO_6:
                            self.column5 = False
                            self.column6 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column4:
                        if self.rect.left + self.move_speed >= ROW_1_COL_4_TO_5:
                            self.column4 = False
                            self.column5 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column3:
                        if self.rect.left + self.move_speed >= ROW_1_COL_3_TO_4:
                            self.column3 = False
                            self.column4 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column2:
                        if self.rect.left + self.move_speed >= ROW_1_COL_2_TO_3:
                            self.column2 = False
                            self.column3 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column1:
                        if self.rect.left + self.move_speed >= ROW_1_COL_1_TO_2:
                            self.column1 = False
                            self.column2 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column0:
                        if self.rect.left + self.move_speed >= ROW_1_COL_0_TO_1:
                            self.column0 = False
                            self.column1 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                elif self.row2:
                    if self.column6:
                        if self.rect.right + self.move_speed >= ROW_2_COL_6_RIGHT_EDGE:
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column5:
                        if self.rect.left + self.move_speed >= ROW_2_COL_5_TO_6:
                            self.column5 = False
                            self.column6 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column4:
                        if self.rect.left + self.move_speed >= ROW_2_COL_4_TO_5:
                            self.column4 = False
                            self.column5 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column3:
                        if self.rect.left + self.move_speed >= ROW_2_COL_3_TO_4:
                            self.column3 = False
                            self.column4 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column2:
                        if self.rect.left + self.move_speed >= ROW_2_COL_2_TO_3:
                            self.column2 = False
                            self.column3 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column1:
                        if self.rect.left + self.move_speed >= ROW_2_COL_1_TO_2:
                            self.column1 = False
                            self.column2 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                elif self.row3:
                    if self.column6:
                        if self.rect.right + self.move_speed >= ROW_3_COL_6_RIGHT_EDGE:
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column5:
                        if self.rect.left + self.move_speed >= ROW_3_COL_5_TO_6:
                            self.column5 = False
                            self.column6 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column4:
                        if self.rect.left + self.move_speed >= ROW_3_COL_4_TO_5:
                            self.column4 = False
                            self.column5 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column3:
                        if self.rect.left + self.move_speed >= ROW_3_COL_3_TO_4:
                            self.column3 = False
                            self.column4 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column2:
                        if self.rect.left + self.move_speed >= ROW_3_COL_2_TO_3:
                            self.column2 = False
                            self.column3 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column1:
                        if self.rect.left + self.move_speed >= ROW_3_COL_1_TO_2:
                            self.column1 = False
                            self.column2 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                elif self.row4:
                    if self.column6:
                        if self.rect.right + self.move_speed >= ROW_4_COL_6_RIGHT_EDGE:
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column5:
                        if self.rect.left + self.move_speed >= ROW_4_COL_5_TO_6:
                            self.column5 = False
                            self.column6 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column4:
                        if self.rect.left + self.move_speed >= ROW_4_COL_4_TO_5:
                            self.column4 = False
                            self.column5 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column3:
                        if self.rect.left + self.move_speed >= ROW_4_COL_3_TO_4:
                            self.column3 = False
                            self.column4 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column2:
                        if self.rect.left + self.move_speed >= ROW_4_COL_2_TO_3:
                            self.column2 = False
                            self.column3 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column1:
                        if self.rect.left + self.move_speed >= ROW_4_COL_1_TO_2:
                            self.column1 = False
                            self.column2 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                elif self.row5:
                    if self.column6:
                        if self.rect.right + self.move_speed >= ROW_5_COL_6_RIGHT_EDGE:
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column5:
                        if self.rect.left + self.move_speed >= ROW_5_COL_5_TO_6:
                            self.column5 = False
                            self.column6 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column4:
                        if self.rect.left + self.move_speed >= ROW_5_COL_4_TO_5:
                            self.column4 = False
                            self.column5 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column3:
                        if self.rect.left + self.move_speed >= ROW_5_COL_3_TO_4:
                            self.column3 = False
                            self.column4 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column2:
                        if self.rect.left + self.move_speed >= ROW_5_COL_2_TO_3:
                            self.column2 = False
                            self.column3 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column1:
                        if self.rect.left + self.move_speed >= ROW_5_COL_1_TO_2:
                            self.column1 = False
                            self.column2 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                elif self.row6:
                    if self.column6:
                        if self.rect.left + self.move_speed >= ROW_6_COL_6_TO_7:
                            self.column6 = False
                            self.column0 = True
                            self.row6 = False
                            self.row1 = True
                            self.teleport_animation()
                            self.x = P1_START_X
                            self.y = P1_START_Y
                            return
                    elif self.column5:
                        if self.rect.left + self.move_speed >= ROW_6_COL_5_TO_6:
                            self.column5 = False
                            self.column6 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column4:
                        if self.rect.left + self.move_speed >= ROW_6_COL_4_TO_5:
                            self.column4 = False
                            self.column5 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column3:
                        if self.rect.left + self.move_speed >= ROW_6_COL_3_TO_4:
                            self.column3 = False
                            self.column4 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column2:
                        if self.rect.left + self.move_speed >= ROW_6_COL_2_TO_3:
                            self.column2 = False
                            self.column3 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                    elif self.column1:
                        if self.rect.left + self.move_speed >= ROW_6_COL_1_TO_2:
                            self.column1 = False
                            self.column2 = True
                            self.key_pressed = False
                            self.key_direction = ""
                            return
                self.x += self.move_speed
            elif self.key_direction == DOWN:
                if self.row1 and self.column6:
                    if self.rect.bottom + self.move_speed >= ROW_0_LOWER_EDGE:
                        self.row1 = False
                        self.row7 = True
                        self.column6 = False
                        self.column1 = True
                        self.teleport_animation()
                        self.x = 222
                        self.y = 89
                        return
                elif self.row1:
                    if self.rect.bottom + self.move_speed >= ROW_0_TO_1:
                        self.key_pressed = False
                        self.key_direction = ""
                        return
                elif self.row2:
                    if self.rect.bottom + self.move_speed >= ROW_0_TO_1:
                        self.row2 = False
                        self.row1 = True
                        self.key_pressed = False
                        self.key_direction = ""
                        return
                elif self.row3:
                    if self.rect.bottom + self.move_speed >= ROW_1_TO_2:
                        self.row3 = False
                        self.row2 = True
                        self.key_pressed = False
                        self.key_direction = ""
                        return
                elif self.row4:
                    if self.rect.bottom + self.move_speed >= ROW_2_TO_3:
                        self.row4 = False
                        self.row3 = True
                        self.key_pressed = False
                        self.key_direction = ""
                        return
                elif self.row5:
                    if self.rect.bottom + self.move_speed >= ROW_3_TO_4:
                        self.row5 = False
                        self.row4 = True
                        self.key_pressed = False
                        self.key_direction = ""
                        return
                elif self.row6:
                    if self.rect.bottom + self.move_speed >= ROW_4_TO_5:
                        self.row6 = False
                        self.row5 = True
                        self.key_pressed = False
                        self.key_direction = ""
                        return
                elif self.row7:
                    if self.rect.bottom + self.move_speed >= ROW_5_TO_6:
                        self.row7 = False
                        self.row6 = True
                        self.key_pressed = False
                        self.key_direction = ""
                        return
                if self.column1:
                    if self.row0 or self.row1 or self.row2 or self.row3:
                        self.x -= 1.22
                    elif self.row4 or self.row5 or self.row6 or self.row7:
                        self.x -= 1.25
                elif self.column2:
                    if self.row0 or self.row1 or self.row2 or self.row3:
                        self.x -= 0.82
                    elif self.row4 or self.row5 or self.row6 or self.row7:
                        self.x -= 0.83
                elif self.column3:
                    if self.row0 or self.row1 or self.row2 or self.row3:
                        self.x -= 0.43
                    elif self.row4 or self.row5 or self.row6 or self.row7:
                        self.x -= 0.44
                elif self.column4:
                    self.x += 0.01
                elif self.column5:
                    if self.row0 or self.row1 or self.row2 or self.row3:
                        self.x += 0.37
                    elif self.row4 or self.row5 or self.row6 or self.row7:
                        self.x += 0.38
                elif self.column6:
                    if self.row0 or self.row1 or self.row2 or self.row3:
                        self.x += 0.77
                    elif self.row4 or self.row5 or self.row6 or self.row7:
                        self.x += 0.75
                self.y += self.move_speed

    def update(self):
        self.load_rect()
        self.scale_imgs()
        self.animation()
        self.draw_player()
        self.player_input()
        self.movement()

    def player_reset(self):
        if self.numb == 1:
            self.x = P1_START_X
            self.y = P1_START_Y
        else:
            self.x = P2_START_X
            self.y = P2_START_Y
        self.score = 0
        self.set_direction()
        self.set_rows()
        self.set_columns()
        self.set_cells()
        self.scale_move_speed()
        self.key_pressed = False
        self.key_direction = ""
        if self.numb == 1:
            self.img_scale = (84, 88)
        else:
            self.img_scale = (60, 64)
        if self.numb == 1:
            self.shadow_scale = (96, 80)
        else:
            self.shadow_scale = (72, 56)
        self.animation_counter = 0
        self.update()
