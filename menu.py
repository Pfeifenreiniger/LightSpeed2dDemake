'''
Game Menu
Graphics and code by Kevin Spathmann (Pfeifenreiniger on GitHub: https://github.com/Pfeifenreiniger)
Look and feel inspired by Nintendo™ originals
'''

import pygame, random
pygame.init()

numb_of_players = 0
SCREEN = pygame.display.set_mode((800, 600))

## menu music ##
title_music = pygame.mixer.Sound("music/mparty3_Inside_the_Castle.mp3")
title_music.set_volume(0.5)
title_music_played = False

score_music = pygame.mixer.Sound("music/mparty3_The_Winner_is....Me!.mp3")
score_music.set_volume(0.7)
score_music_played = False

# menu sfx #
sfx_cursor_movement = pygame.mixer.Sound("sfx/menu/ssb_dot.wav")
sfx_cursor_movement.set_volume(0.4)
sfx_cursor_select = pygame.mixer.Sound("sfx/menu/ssb_select.wav")
sfx_cursor_select.set_volume(0.4)

sfx_koopa = pygame.mixer.Sound("sfx/menu/ssb_dot.wav")
sfx_koopa.set_volume(0.2)

sfx_score_screen = pygame.mixer.Sound("sfx/menu/sm64_high_score.wav")
sfx_score_screen.set_volume(0.8)
sfx_score_screen_played = False

voice_mario_selected = pygame.mixer.Sound("voices/mario/sm64_mario_its_me_(selected).wav")
voice_mario_selected.set_volume(0.5)
voice_peach_selected = pygame.mixer.Sound("voices/peach/mparty5_hooray_(selected).wav")
voice_peach_selected.set_volume(0.5)
voice_yoshi_selected = pygame.mixer.Sound("voices/yoshi/mparty5_yoshi_yooshi_(selected).wav")
voice_yoshi_selected.set_volume(0.5)
voice_waluigi_selected1 = pygame.mixer.Sound("voices/waluigi/mparty5_waluigi_whoahaha_(selected).wav")
voice_waluigi_selected1.set_volume(0.5)
voice_waluigi_selected2 = pygame.mixer.Sound("voices/waluigi/mparty5_waluigi_good_choice_(selected).wav")
voice_waluigi_selected2.set_volume(0.5)

## menu graphics ##
# bgs #
bg_numb_of_players = pygame.image.load("graphics/menu/bg_number_of_players.png").convert()
bg_char_select = pygame.image.load("graphics/menu/bg_character_selection.png").convert()
bg_cpu_difficulty = pygame.image.load("graphics/menu/bg_cpu_difficulty.png").convert()
bg_control_mapping = pygame.image.load("graphics/menu/bg_control_mapping.png").convert()
bg_score_screen = pygame.image.load("graphics/menu/bg_score_screen.png").convert()
# control key mapping #
keys_numb_players_up_down = pygame.image.load("graphics/menu/control_mapping/control_keys_numbOfPlayers.png").convert_alpha()
keys_numb_players_enter = pygame.image.load("graphics/menu/control_mapping/control_keys_enter.png").convert_alpha()
keys_char_select_p1 = pygame.image.load("graphics/menu/control_mapping/p1_char_select.png").convert_alpha()
keys_char_select_p2 = pygame.image.load("graphics/menu/control_mapping/p2_char_select.png").convert_alpha()
keys_ingame_p1 = pygame.image.load("graphics/menu/control_mapping/p1_ingame_control.png").convert_alpha()
keys_ingame_p2 = pygame.image.load("graphics/menu/control_mapping/p2_ingame_control.png").convert_alpha()

# koopas #
menu_koopas = [pygame.image.load("graphics/menu/koopa/menu_koopa_1.png").convert_alpha(),
               pygame.image.load("graphics/menu/koopa/menu_koopa_2.png").convert_alpha()]
menu_koopa_counter = 0
menu_koopa_frameanimation = 0.005
menu_koopa_balloon = pygame.image.load("graphics/menu/koopa/balloon_koopa.png").convert_alpha()

which_menu = "numb_of_players"

def menu_change():
    global which_menu, Menucursor, koopa_advice1_t_counter, koopa_advice2_t_counter, koopa_advice3_t_counter, koopa_advice4_t_counter, koopa_advice5_t_counter, koopa_advice6_t_counter, koopa_advice7_t_counter, koopa_advice8_t_counter, koopa_advice_cpu1_t_counter, koopa_advice_cpu2_t_counter
    if which_menu == "numb_of_players":
        Menucursor.pressed = True
        which_menu = "char_select"
        koopa_advice1_t_counter = 0
        koopa_advice2_t_counter = 0
    elif which_menu == "char_select" and p1_char_select.cpu_character != "":
        which_menu = "cpu_difficulty"
        koopa_advice3_t_counter = 0
        koopa_advice4_t_counter = 0
    elif which_menu == "char_select":
        which_menu = "control_mapping"
        koopa_advice3_t_counter = 0
        koopa_advice4_t_counter = 0
    elif which_menu == "cpu_difficulty":
        which_menu = "control_mapping"
        koopa_advice_cpu1_t_counter = 0
        koopa_advice_cpu2_t_counter = 0
    elif which_menu == "control_mapping":
        which_menu = "score_screen"
        koopa_advice5_t_counter = 0
        koopa_advice6_t_counter = 0
    elif which_menu == "score_screen":
        which_menu = "numb_of_players"
        koopa_advice7_t_counter = 0
        koopa_advice8_t_counter = 0

p1_char = False
p2_char = False

def char_selected():
    global p1_char, p2_char
    # first player
    if p1_char_select.character != "":
        p1_char = True
    # second player
    if p2_char_select.character != "":
        p2_char = True
    # cpu
    if p1_char_select.cpu_character != "":
        p2_char = True

def char_selected_reset():
    global menu_cursor, p1_char, p2_char, p1_char_select, p2_char_select, cpu_diff_cursor
    menu_cursor.x = 520
    menu_cursor.y = 83
    menu_cursor.number_of_players = 0
    menu_cursor.pressed = False
    cpu_diff_cursor.pressed = False
    p1_char = False
    p1_char_select.character = ""
    p1_char_select.cpu_character = ""
    p1_char_select.x = 288
    p1_char_select.y = 50
    p1_char_select.pressed = False
    p2_char = False
    p2_char_select.character = ""
    p2_char_select.x = 305
    p2_char_select.y = 50
    p2_char_select.pressed = False

    # if p1_char_select.character != "":
    #     p1_char = False
    #     p1_char_select.character = ""
    #     p1_char_select.cpu_character = ""
    #     p1_char_select.x = 288
    #     p1_char_select.y = 50
    #     p1_char_select.pressed = False
    # if p2_char_select.character != "" or p1_char_select.cpu_character != "":
    #     p2_char = False
    #     p2_char_select.character = ""
    #     p1_char_select.cpu_character = ""
    #     p2_char_select.x = 305
    #     p2_char_select.y = 50
    #     p2_char_select.pressed = False

p1_rect_color = (255, 0, 0)
p2_rect_color = (0, 26, 255)
p3_rect_color = (37, 218, 21)
p4_rect_color = (235, 181, 47)
def char_select_rect():
    if p1_char:
        if p1_char_select.character == "mario":
            pygame.draw.rect(SCREEN, p1_rect_color, p1_char_select.char_select_rect, 3, 2) # 3 line stroke, 2 smooth edges
        elif p1_char_select.character == "peach":
            pygame.draw.rect(SCREEN, p1_rect_color, p1_char_select.char_select_rect, 3, 2)
        elif p1_char_select.character == "yoshi":
            pygame.draw.rect(SCREEN, p1_rect_color, p1_char_select.char_select_rect, 3, 2)
        elif p1_char_select.character == "waluigi":
            pygame.draw.rect(SCREEN, p1_rect_color, p1_char_select.char_select_rect, 3, 2)
    if p2_char:
        if p2_char_select.character == "mario":
            pygame.draw.rect(SCREEN, p2_rect_color, p2_char_select.char_select_rect, 3, 2)
        elif p2_char_select.character == "peach":
            pygame.draw.rect(SCREEN, p2_rect_color, p2_char_select.char_select_rect, 3, 2)
        elif p2_char_select.character == "yoshi":
            pygame.draw.rect(SCREEN, p2_rect_color, p2_char_select.char_select_rect, 3, 2)
        elif p2_char_select.character == "waluigi":
            pygame.draw.rect(SCREEN, p2_rect_color, p2_char_select.char_select_rect, 3, 2)


p1_rect_breite = 98
p1_rect_hoehe = 92
p2_rect_breite = 100
p2_rect_hoehe = 94

class Menucursor():
    def __init__(self, player=0, which_menu="numb_of_players"):
        self.player = player
        self.which_menu = which_menu
        if self.player == 0:
            self.img = pygame.image.load("graphics/menu/menu_cursor.png").convert_alpha()
        elif self.player == 1:
            self.img = pygame.image.load("graphics/menu/menu_cursor_p1.png").convert_alpha()
        elif self.player == 2:
            self.img = pygame.image.load("graphics/menu/menu_cursor_p2.png").convert_alpha()
        if self.which_menu == "numb_of_players":
            self.x = 520
            self.y = 83
        elif self.which_menu == "char_select":
            self.y = 50
            if self.player == 1:
                self.x = 288
            elif self.player == 2:
                self.x = 305
        elif self.which_menu == "cpu_difficulty":
            self.y = 55
            self.x = 520
        self.pressed = False
        self.number_of_players = 0
        self.char_select_rect = pygame.Rect(self.x, self.y, 98, 92)
        self.character = ""
        self.cpu_character = ""
        self.cpu_difficulty = ""
        self.player_initialized = False
    def menu_input(self):
        global numb_of_players
        keys = pygame.key.get_pressed()
        if self.which_menu == "numb_of_players":
            if keys[pygame.K_w] and (self.y - 93 >= 83) and self.pressed != True:
                self.y -= 93
                self.pressed = True
                sfx_cursor_movement.play()
            elif keys[pygame.K_s] and (self.y + 93 <= 176) and self.pressed != True:
                self.y += 93
                self.pressed = True
                sfx_cursor_movement.play()
            elif keys[pygame.K_RETURN] and self.y == 83:
                self.number_of_players = 2
                self.pressed = True
                numb_of_players = 2
                sfx_cursor_select.play()
                menu_change()
            elif keys[pygame.K_RETURN] and self.y == 176:
                self.number_of_players = 1
                self.pressed = True
                numb_of_players = 1
                sfx_cursor_select.play()
                menu_change()
        elif self.which_menu == "char_select":
            if self.player == 1 and keys[pygame.K_w] and (self.y - 110 >= 50) and self.pressed != True:
                self.y -= 110
                self.pressed = True
                sfx_cursor_movement.play()
            elif self.player == 1 and keys[pygame.K_s] and (self.y + 110 <= 160) and self.pressed != True:
                self.y += 110
                self.pressed = True
                sfx_cursor_movement.play()
            elif self.player == 1 and keys[pygame.K_a] and (self.x - 132 >= 288) and self.pressed != True:
                self.x -= 132
                self.pressed = True
                sfx_cursor_movement.play()
            elif self.player == 1 and keys[pygame.K_d] and (self.x + 132 <= 420) and self.pressed != True:
                self.x += 132
                self.pressed = True
                sfx_cursor_movement.play()
            elif self.player == 1 and keys[pygame.K_x] and self.x == 288 and self.y == 50 and self.pressed != True and p1_char != True:  # upper left
                self.character = "mario"
                self.char_select_rect = pygame.Rect(self.x-2, self.y+31, 98, 92)
                self.pressed = True
                voice_mario_selected.play()
                char_selected()
            elif self.player == 1 and keys[pygame.K_x] and self.x == 420 and self.y == 50 and self.pressed != True and p1_char != True:  # upper right
                self.character = "peach"
                self.char_select_rect = pygame.Rect(self.x - 2, self.y + 31, p1_rect_breite, p1_rect_hoehe)
                self.pressed = True
                voice_peach_selected.play()
                char_selected()
            elif self.player == 1 and keys[pygame.K_x] and self.x == 288 and self.y == 160 and self.pressed != True and p1_char != True: # down left
                self.character = "yoshi"
                self.char_select_rect = pygame.Rect(self.x - 2, self.y + 30, p1_rect_breite, p1_rect_hoehe)
                self.pressed = True
                voice_yoshi_selected.play()
                char_selected()
            elif self.player == 1 and keys[pygame.K_x] and self.x == 420 and self.y == 160 and self.pressed != True and p1_char != True: # down right
                self.character = "waluigi"
                self.char_select_rect = pygame.Rect(self.x - 2, self.y + 30, p1_rect_breite, p1_rect_hoehe)
                self.pressed = True
                if random.randint(0,10) > 8:
                    voice_waluigi_selected2.play()
                else: voice_waluigi_selected1.play()
                char_selected()
            # selecting the cpu
            if p1_char:
                if self.player == 1 and keys[pygame.K_x] and self.x == 288 and self.y == 50 and self.pressed != True:
                    self.cpu_character = "mario"
                    self.char_select_rect = pygame.Rect(self.x - 2, self.y + 31, 98, 92)
                    self.pressed = True
                    voice_mario_selected.play()
                    char_selected()
                elif self.player == 1 and keys[
                    pygame.K_x] and self.x == 420 and self.y == 50 and self.pressed != True:  # upper right
                    self.cpu_character = "peach"
                    self.char_select_rect = pygame.Rect(self.x - 2, self.y + 31, p1_rect_breite, p1_rect_hoehe)
                    self.pressed = True
                    voice_peach_selected.play()
                    char_selected()
                elif self.player == 1 and keys[
                    pygame.K_x] and self.x == 288 and self.y == 160 and self.pressed != True:  # down left
                    self.cpu_character = "yoshi"
                    self.char_select_rect = pygame.Rect(self.x - 2, self.y + 30, p1_rect_breite, p1_rect_hoehe)
                    self.pressed = True
                    voice_yoshi_selected.play()
                    char_selected()
                elif self.player == 1 and keys[
                    pygame.K_x] and self.x == 420 and self.y == 160 and self.pressed != True:  # down right
                    self.cpu_character = "waluigi"
                    self.char_select_rect = pygame.Rect(self.x - 2, self.y + 30, p1_rect_breite, p1_rect_hoehe)
                    self.pressed = True
                    if random.randint(0, 10) > 8:
                        voice_waluigi_selected2.play()
                    else:
                        voice_waluigi_selected1.play()
                    char_selected()
            if self.player == 2 and keys[pygame.K_UP] and (self.y - 110 >= 50) and self.pressed != True:
                self.y -= 110
                self.pressed = True
                sfx_cursor_movement.play()
            elif self.player == 2 and keys[pygame.K_DOWN] and (self.y + 110 <= 160) and self.pressed != True:
                self.y += 110
                self.pressed = True
                sfx_cursor_movement.play()
            elif self.player == 2 and keys[pygame.K_LEFT] and (self.x - 132 >= 305) and self.pressed != True:
                self.x -= 132
                self.pressed = True
                sfx_cursor_movement.play()
            elif self.player == 2 and keys[pygame.K_RIGHT] and (self.x + 132 <= 437) and self.pressed != True:
                self.x += 132
                self.pressed = True
                sfx_cursor_movement.play()
            elif self.player == 2 and keys[pygame.K_KP0] and self.x == 305 and self.y == 50 and self.pressed != True:
                self.character = "mario"
                self.char_select_rect = pygame.Rect(self.x - 21, self.y + 30, p2_rect_breite, p2_rect_hoehe)
                self.pressed = True
                voice_mario_selected.play()
                char_selected()
            elif self.player == 2 and keys[pygame.K_KP0] and self.x == 437 and self.y == 50 and self.pressed != True:
                self.character = "peach"
                self.char_select_rect = pygame.Rect(self.x - 21, self.y + 30, p2_rect_breite, p2_rect_hoehe)
                self.pressed = True
                voice_peach_selected.play()
                char_selected()
            elif self.player == 2 and keys[pygame.K_KP0] and self.x == 305 and self.y == 160 and self.pressed != True:
                self.character = "yoshi"
                self.char_select_rect = pygame.Rect(self.x - 21, self.y + 30, p2_rect_breite, p2_rect_hoehe)
                self.pressed = True
                voice_yoshi_selected.play()
                char_selected()
            elif self.player == 2 and keys[pygame.K_KP0] and self.x == 437 and self.y == 160 and self.pressed != True:
                self.character = "waluigi"
                self.char_select_rect = pygame.Rect(self.x - 21, self.y + 30, p2_rect_breite, p2_rect_hoehe)
                self.pressed = True
                if random.randint(0,10) > 8:
                    voice_waluigi_selected2.play()
                else: voice_waluigi_selected1.play()
                char_selected()
        elif self.which_menu == "cpu_difficulty":
            if keys[pygame.K_w] and (self.y - 78 >= 55) and self.pressed != True:
                self.y -= 78
                self.pressed = True
                sfx_cursor_movement.play()
            elif keys[pygame.K_s] and (self.y + 78 <= 211) and self.pressed != True:
                self.y += 78
                self.pressed = True
                sfx_cursor_movement.play()
            elif keys[pygame.K_RETURN] and self.y == 55:
                self.cpu_difficulty = "easy"
                self.pressed = True
                sfx_cursor_select.play()
                menu_change()
            elif keys[pygame.K_RETURN] and self.y == 133:
                self.cpu_difficulty = "hard"
                self.pressed = True
                sfx_cursor_select.play()
                menu_change()
            elif keys[pygame.K_RETURN] and self.y == 211:
                self.cpu_difficulty = "very hard"
                self.pressed = True
                sfx_cursor_select.play()
                menu_change()
    def menu_display(self):
        SCREEN.blit(self.img, (self.x, self.y))
    def menu_update(self):
        self.menu_input()
        self.menu_display()
menu_cursor = Menucursor()  # without arguments; therefore, for number of players selector

p1_char_select = Menucursor(1,"char_select")
p2_char_select = Menucursor(2,"char_select")

cpu_diff_cursor = Menucursor(1, "cpu_difficulty")

## texts ##
## fonts ##
mario64_font = pygame.font.Font("font/Super-Mario-64-DS.ttf", 20)
# select number of players #
twoPlayers = mario64_font.render("1 vs 2 Player", False, (25, 25, 25))
twoPlayers_rect = twoPlayers.get_rect(center=(406, 133))
onePlayer_CPU = mario64_font.render("1 Player vs CPU", False, (25, 25, 25))
onePlayer_CPU_rect = onePlayer_CPU.get_rect(center=(400, 228))

# koopa advice - textspeed #
koopa_t_speed = 0.4
# koopa advice - number of players #
koopa_advice1_text = "Select the number of players"
koopa_advice1_t_counter = 0
koopa_advice2_text = "who would like to play."
koopa_advice2_t_counter = 0

def display_menu_numb_of_players():
    global menu_koopa_counter, koopa_advice1_t_counter, koopa_advice2_t_counter
    SCREEN.blit(bg_numb_of_players, (0, 0))
    SCREEN.blit(keys_numb_players_up_down, (22, 97))
    SCREEN.blit(keys_numb_players_enter, (682, 97))
    # text koopa advice
    koopa_advice1 = mario64_font.render(koopa_advice1_text[:round(koopa_advice1_t_counter)], False, (25, 25, 25))
    koopa_advice1_rect = koopa_advice1.get_rect(topleft=(95, 444))
    koopa_advice2 = mario64_font.render(koopa_advice2_text[:round(koopa_advice2_t_counter)], False, (25, 25, 25))
    koopa_advice2_rect = koopa_advice2.get_rect(topleft=(95, 500))
    SCREEN.blit(menu_koopa_balloon, (69, 422))
    if round(koopa_advice1_t_counter) + 1 > len(koopa_advice1_text):
        koopa_advice1_t_counter = len(koopa_advice1_text)
        if round(koopa_advice2_t_counter)+ 1 > len(koopa_advice2_text):
            koopa_advice2_t_counter = len(koopa_advice2_text)
        else:
            koopa_advice2_t_counter += koopa_t_speed
            if round(koopa_advice2_t_counter) == (int(koopa_advice2_t_counter + 1)):
                sfx_koopa.play()
    else:
        koopa_advice1_t_counter += koopa_t_speed
        if round(koopa_advice1_t_counter) == (int(koopa_advice1_t_counter + 1)):
            sfx_koopa.play()
    SCREEN.blit(koopa_advice1, koopa_advice1_rect)
    SCREEN.blit(koopa_advice2, koopa_advice2_rect)
    # animated koopa
    SCREEN.blit(menu_koopas[round(menu_koopa_counter)], (565, 320))
    if menu_koopa_counter > 0.55:
        menu_koopa_counter = 0
    else:
        menu_koopa_counter += menu_koopa_frameanimation
    # text of number of players
    SCREEN.blit(twoPlayers, twoPlayers_rect)
    SCREEN.blit(onePlayer_CPU, onePlayer_CPU_rect)

# koopa advice - char select #
koopa_advice3_text = "" # text will be set in display_char_select() function
koopa_advice3_t_counter = 0
koopa_advice4_text = ""
koopa_advice4_t_counter = 0

# graphics of characters for char select screen #
mar_head1 = pygame.image.load("graphics/menu/char_select_heads/mar_unselected.png").convert_alpha()
mar_head2 = pygame.image.load("graphics/menu/char_select_heads/mar_selected.png").convert_alpha()
pea_head1 = pygame.image.load("graphics/menu/char_select_heads/pea_unselected.png").convert_alpha()
pea_head2 = pygame.image.load("graphics/menu/char_select_heads/pea_selected.png").convert_alpha()
yos_head1 = pygame.image.load("graphics/menu/char_select_heads/yos_unselected.png").convert_alpha()
yos_head2 = pygame.image.load("graphics/menu/char_select_heads/yos_selected.png").convert_alpha()
wal_head1 = pygame.image.load("graphics/menu/char_select_heads/wal_unselected.png").convert_alpha()
wal_head2 = pygame.image.load("graphics/menu/char_select_heads/wal_selected.png").convert_alpha()
def display_char_heads():
    # mario
    if p1_char_select.character == "mario" or p2_char_select.character == "mario":
        SCREEN.blit(mar_head2, (285, 83))
    else: SCREEN.blit(mar_head1, (285, 83))
    # peach
    if p1_char_select.character == "peach" or p2_char_select.character == "peach":
        SCREEN.blit(pea_head2, (418, 83))
    else: SCREEN.blit(pea_head1, (418, 83))
    # yoshi
    if p1_char_select.character == "yoshi" or p2_char_select.character == "yoshi":
        SCREEN.blit(yos_head2, (285, 190))
    else: SCREEN.blit(yos_head1, (285, 190))
    # waluigi
    if p1_char_select.character == "waluigi" or p2_char_select.character == "waluigi":
        SCREEN.blit(wal_head2, (418, 190))
    else: SCREEN.blit(wal_head1, (418, 190))

def display_char_select():
    global menu_koopa_counter, koopa_advice3_text, koopa_advice4_text, koopa_advice3_t_counter, koopa_advice4_t_counter
    if numb_of_players == 1:    # in case of single player vs CPU
        koopa_advice3_text = "Choose which characters"
        koopa_advice4_text = "the player and CPU will use."
    else:   # else multi player
        koopa_advice3_text = "Choose which characters"
        koopa_advice4_text = "the players will use."
    SCREEN.blit(bg_char_select, (0,0))
    display_char_heads()
    SCREEN.blit(keys_char_select_p1, (10, 97))
    if numb_of_players > 1:
        SCREEN.blit(keys_char_select_p2, (560, 97))

    # text koopa advice
    koopa_advice3 = mario64_font.render(koopa_advice3_text[:round(koopa_advice3_t_counter)], False, (25, 25, 25))
    koopa_advice3_rect = koopa_advice3.get_rect(topleft=(95, 444))
    koopa_advice4 = mario64_font.render(koopa_advice4_text[:round(koopa_advice4_t_counter)], False, (25, 25, 25))
    koopa_advice4_rect = koopa_advice4.get_rect(topleft=(95, 500))
    SCREEN.blit(menu_koopa_balloon, (69, 422))
    if round(koopa_advice3_t_counter) + 1 > len(koopa_advice3_text):
        koopa_advice3_t_counter = len(koopa_advice3_text)
        if round(koopa_advice4_t_counter)+ 1 > len(koopa_advice4_text):
            koopa_advice4_t_counter = len(koopa_advice4_text)
        else:
            koopa_advice4_t_counter += koopa_t_speed
            if round(koopa_advice4_t_counter) == (int(koopa_advice4_t_counter + 1)):
                sfx_koopa.play()
    else:
        koopa_advice3_t_counter += koopa_t_speed
        if round(koopa_advice3_t_counter) == (int(koopa_advice3_t_counter + 1)):
            sfx_koopa.play()
    SCREEN.blit(koopa_advice3, koopa_advice3_rect)
    SCREEN.blit(koopa_advice4, koopa_advice4_rect)
    # animated koopa
    SCREEN.blit(menu_koopas[round(menu_koopa_counter)], (565, 320))
    if menu_koopa_counter > 0.55:
        menu_koopa_counter = 0
    else:
        menu_koopa_counter += menu_koopa_frameanimation

# cpu difficulty #
easy = mario64_font.render("easy", False, (25, 25, 25))
easy_rect = easy.get_rect(center=(406, 102))
hard = mario64_font.render("hard", False, (25, 25, 25))
hard_rect = hard.get_rect(center=(400, 180))
very_hard = mario64_font.render("very hard", False, (25, 25, 25))
very_hard_rect = very_hard.get_rect(center=(400, 258))
# koopa advice - cpu difficulty +
koopa_advice_cpu1_text = "The CPUs difficulty..."
koopa_advice_cpu1_t_counter = 0
koopa_advice_cpu2_text = "Choose wisely!"
koopa_advice_cpu2_t_counter = 0
def display_cpu_difficulty():
    global menu_koopa_counter, koopa_advice_cpu1_t_counter, koopa_advice_cpu2_t_counter
    SCREEN.blit(bg_cpu_difficulty, (0, 0))
    SCREEN.blit(keys_numb_players_up_down, (22, 97))
    SCREEN.blit(keys_numb_players_enter, (682, 97))

    # text koopa advice
    koopa_advice_cpu1 = mario64_font.render(koopa_advice_cpu1_text[:round(koopa_advice_cpu1_t_counter)], False, (25, 25, 25))
    koopa_advice_cpu1_rect = koopa_advice_cpu1.get_rect(topleft=(95, 444))
    koopa_advice_cpu2 = mario64_font.render(koopa_advice_cpu2_text[:round(koopa_advice_cpu2_t_counter)], False, (25, 25, 25))
    koopa_advice_cpu2_rect = koopa_advice_cpu2.get_rect(topleft=(95, 500))
    SCREEN.blit(menu_koopa_balloon, (69, 422))
    if round(koopa_advice_cpu1_t_counter) + 1 > len(koopa_advice_cpu1_text):
        koopa_advice_cpu1_t_counter = len(koopa_advice_cpu1_text)
        if round(koopa_advice_cpu2_t_counter) + 1 > len(koopa_advice_cpu2_text):
            koopa_advice_cpu2_t_counter = len(koopa_advice_cpu2_text)
        else:
            koopa_advice_cpu2_t_counter += koopa_t_speed
            if round(koopa_advice_cpu2_t_counter) == (int(koopa_advice_cpu2_t_counter + 1)):
                sfx_koopa.play()
    else:
        koopa_advice_cpu1_t_counter += koopa_t_speed
        if round(koopa_advice_cpu1_t_counter) == (int(koopa_advice_cpu1_t_counter + 1)):
            sfx_koopa.play()
    SCREEN.blit(koopa_advice_cpu1, koopa_advice_cpu1_rect)
    SCREEN.blit(koopa_advice_cpu2, koopa_advice_cpu2_rect)
    # animated koopa
    SCREEN.blit(menu_koopas[round(menu_koopa_counter)], (565, 320))
    if menu_koopa_counter > 0.55:
        menu_koopa_counter = 0
    else:
        menu_koopa_counter += menu_koopa_frameanimation
    # text of difficulty
    SCREEN.blit(easy, easy_rect)
    SCREEN.blit(hard, hard_rect)
    SCREEN.blit(very_hard, very_hard_rect)

# koopa advice - control mapping #
koopa_advice5_text = "Your game control. Be careful!"
koopa_advice5_t_counter = 0
koopa_advice6_text = "Press Enter to start."
koopa_advice6_t_counter = 0
def display_control_mapping():
    global menu_koopa_counter, koopa_advice5_t_counter, koopa_advice6_t_counter
    SCREEN.blit(bg_control_mapping, (0,0))
    SCREEN.blit(keys_ingame_p1, (200, 130))
    if numb_of_players > 1:
        SCREEN.blit(keys_ingame_p2, (400, 130))

    # text koopa advice
    koopa_advice5 = mario64_font.render(koopa_advice5_text[:round(koopa_advice5_t_counter)], False, (25, 25, 25))
    koopa_advice5_rect = koopa_advice5.get_rect(topleft=(95, 444))
    koopa_advice6 = mario64_font.render(koopa_advice6_text[:round(koopa_advice6_t_counter)], False, (25, 25, 25))
    koopa_advice6_rect = koopa_advice6.get_rect(topleft=(95, 500))
    SCREEN.blit(menu_koopa_balloon, (69, 422))
    if round(koopa_advice5_t_counter) + 1 > len(koopa_advice5_text):
        koopa_advice5_t_counter = len(koopa_advice5_text)
        if round(koopa_advice6_t_counter)+ 1 > len(koopa_advice6_text):
            koopa_advice6_t_counter = len(koopa_advice6_text)
        else:
            koopa_advice6_t_counter += koopa_t_speed
            if round(koopa_advice6_t_counter) == (int(koopa_advice6_t_counter + 1)):
                sfx_koopa.play()
    else:
        koopa_advice5_t_counter += koopa_t_speed
        if round(koopa_advice5_t_counter) == (int(koopa_advice5_t_counter + 1)):
            sfx_koopa.play()
    SCREEN.blit(koopa_advice5, koopa_advice5_rect)
    SCREEN.blit(koopa_advice6, koopa_advice6_rect)
    # animated koopa
    SCREEN.blit(menu_koopas[round(menu_koopa_counter)], (565, 320))
    if menu_koopa_counter > 0.55:
        menu_koopa_counter = 0
    else:
        menu_koopa_counter += menu_koopa_frameanimation

# koopa advice - score screen #
koopa_advice7_text = "Press enter to retry..."
koopa_advice7_t_counter = 0
koopa_advice8_text = "...or space to restart the game."
koopa_advice8_t_counter = 0
def display_score_screen():
    global menu_koopa_counter, koopa_advice7_t_counter, koopa_advice8_t_counter, which_menu, sfx_score_screen_played
    if sfx_score_screen_played != True:
        sfx_score_screen.play()
        sfx_score_screen_played = True
    which_menu = "score_screen"
    SCREEN.blit(bg_score_screen, (0, 0))
    # text koopa advice
    koopa_advice7 = mario64_font.render(koopa_advice7_text[:round(koopa_advice7_t_counter)], False, (25, 25, 25))
    koopa_advice7_rect = koopa_advice7.get_rect(topleft=(95, 444))
    koopa_advice8 = mario64_font.render(koopa_advice8_text[:round(koopa_advice8_t_counter)], False, (25, 25, 25))
    koopa_advice8_rect = koopa_advice8.get_rect(topleft=(95, 500))
    SCREEN.blit(menu_koopa_balloon, (69, 422))
    if round(koopa_advice7_t_counter) + 1 > len(koopa_advice7_text):
        koopa_advice7_t_counter = len(koopa_advice7_text)
        if round(koopa_advice8_t_counter) + 1 > len(koopa_advice8_text):
            koopa_advice8_t_counter = len(koopa_advice8_text)
        else:
            koopa_advice8_t_counter += koopa_t_speed
            if round(koopa_advice8_t_counter) == (int(koopa_advice8_t_counter + 1)):
                sfx_koopa.play()
    else:
        koopa_advice7_t_counter += koopa_t_speed
        if round(koopa_advice7_t_counter) == (int(koopa_advice7_t_counter + 1)):
            sfx_koopa.play()
    SCREEN.blit(koopa_advice7, koopa_advice7_rect)
    SCREEN.blit(koopa_advice8, koopa_advice8_rect)
    # animated koopa
    SCREEN.blit(menu_koopas[round(menu_koopa_counter)], (565, 320))
    if menu_koopa_counter > 0.55:
        menu_koopa_counter = 0
    else:
        menu_koopa_counter += menu_koopa_frameanimation