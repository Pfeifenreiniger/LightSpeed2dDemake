
import pygame
pygame.init()

SCREEN = pygame.display.set_mode((800, 600))
mario64_font = pygame.font.Font("font/Super-Mario-64-DS.ttf", 20)
marioKart_font = pygame.font.Font("font/Mario-Kart-DS.ttf", 50)

LIMIT_TIME = 0

def display_time_limit(time_limit: int):
    """function returns false when time limit is over"""
    current_time = int(time_limit - ((pygame.time.get_ticks() / 1000) - LIMIT_TIME))
    font = marioKart_font
    if current_time <= 10:
        time_color = (255, 0, 0)
    else:
        time_color = (51, 255, 255)
    time_surf = font.render(str(current_time), False, time_color)
    time_rect = time_surf.get_rect(center=(400, 550))
    time_bg = pygame.Surface((76, 56))
    time_bg.fill((0, 0, 0,))
    time_bg.set_alpha(128)
    SCREEN.blit(time_bg, time_bg.get_rect(center = (400, 550)))
    pygame.draw.rect(SCREEN, (204, 204, 0), pygame.Rect(360, 520, 80, 60), 6, 6, 6, 6)
    SCREEN.blit(time_surf, time_rect)
    if current_time <= 0:
        return False
    else:
        return True

