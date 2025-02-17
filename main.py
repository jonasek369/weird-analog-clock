import pygame
from datetime import datetime
import math

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

font = pygame.font.SysFont("arial", 12)

running = True


def draw_degree_line(degrees, size, draw_surface: pygame.Surface):
    for i in range(12, size, 12):
        screen.blit(pygame.transform.rotate(draw_surface, -degrees), (
            200 + math.cos(math.radians(degrees)) * i - 6, 200 + math.sin(math.radians(degrees)) * i - 6
        ))


while running:
    screen.fill(0)

    current_time = datetime.now()

    pygame.draw.circle(screen, (255, 255, 255), (200, 200), 190)
    pygame.draw.circle(screen, (0, 0, 0), (200, 200), 180)
    pygame.draw.circle(screen, (222, 222, 222), (200, 200), 6)
    draw_degree_line((current_time.second * 6) - 90, 180, font.render(f"{current_time.second}", True, (255, 212, 212)))
    draw_degree_line((current_time.minute * 6) - 90, 130, font.render(f"{current_time.minute}", True, (255, 255, 255)))
    draw_degree_line((current_time.hour * 15) - 90, 100, font.render(f"{current_time.hour}", True, (255, 255, 255)))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    pygame.display.flip()
    clock.tick(60)
