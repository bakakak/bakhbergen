import pygame
import sys
import datetime


pygame.init()
screen = pygame.display.set_mode((1200, 700))
clock = pygame.time.Clock()

mikey = pygame.image.load("mikey.png")
hour_hand = pygame.image.load("hour.png")
minute_hand = pygame.image.load("min.png")
mikey=pygame.transform.scale(mikey,(700,700))
mikey_rect = mikey.get_rect(center=(600, 350))
hour_hand_rect = hour_hand.get_rect(center=mikey_rect.center)
minute_hand_rect = minute_hand.get_rect(center=mikey_rect.center)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    current_time = datetime.datetime.now() 
    hour_angle = (current_time.minute * 6) - 90
    minute_angle = (current_time.second * 6) - 87

    # Rotate the hands
    rotated_hour_hand = pygame.transform.rotate(hour_hand, -hour_angle)
    rotated_minute_hand = pygame.transform.rotate(minute_hand, -minute_angle)
    hour_hand_rect = rotated_hour_hand.get_rect(center=mikey_rect.center)
    minute_hand_rect = rotated_minute_hand.get_rect(center=mikey_rect.center)

    screen.fill((255, 255, 255))
    screen.blit(mikey, mikey_rect)
    screen.blit(rotated_hour_hand, hour_hand_rect)
    screen.blit(rotated_minute_hand, minute_hand_rect)

    pygame.display.update()
    clock.tick(60)
