import pygame

pygame.mixer.pre_init(44100)
pygame.init()

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

first = pygame.mixer.Sound("first.mp3")
second = pygame.mixer.Sound("second.mp3")
third = pygame.mixer.Sound("third.mp3")
first_img = pygame.image.load("first.png")
second_img = pygame.image.load("second.png")
third_img = pygame.image.load("third.png")
background_surface = pygame.Surface((800, 800))
background_surface.fill((255, 255, 255))
images = [first_img, second_img, third_img]
sounds = [first, second, third]
current_sound_index = 0 
started = False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            if not started:
                sounds[current_sound_index].play()
                started = True
                print("started")
            else:
                print("already started")
            pygame.time.delay(200)
        if event.key == pygame.K_RIGHT:
            if sounds[current_sound_index]:
                sounds[current_sound_index].stop()
                current_sound_index = (current_sound_index + 1)
            if current_sound_index == len(sounds):
                current_sound_index = 0
            sounds[current_sound_index].play()
            print("next sound")
            pygame.time.delay(200)
        if event.key == pygame.K_LEFT:
            if sounds[current_sound_index]:
                sounds[current_sound_index].stop()
                current_sound_index = (current_sound_index - 1)
            if current_sound_index == -1:
                current_sound_index = 2
            sounds[current_sound_index].play()
            print("prev sound")
            pygame.time.delay(200)
        elif event.key == pygame.K_DOWN:
            if sounds[current_sound_index]:
                sounds[current_sound_index].stop()
                pygame.time.delay(200)
                print("stopped")
                started = False
            print("not stopped")
        



    if started:
        if current_sound_index == 0:
            background_surface.fill((172, 0, 166))
        elif current_sound_index == 1:
            background_surface.fill((12, 0, 58))
        elif current_sound_index == 2:
            background_surface.fill((0, 172, 204))
        screen.blit(background_surface, (0, 0))
        screen.blit(images[current_sound_index], (80, 80))
    else:
        background_surface.fill((255, 255, 255))
        screen.blit(background_surface, (0, 0))


    

    pygame.display.flip()
    clock.tick(60)
