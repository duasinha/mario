import pygame
import spritesheet

pygame.init()

SCREEN_WIDTH = 150
SCREEN_HEIGTH = 150

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
pygame.display.set_caption('Mario Foguinho')

sprite_sheet_image = pygame.image.load('mario_fire.png').convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

BG =(50, 50, 50)
BLACK = (0, 0, 0)

animation_list = []
animation_steps = [2, 5, 2, 2, 2]
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 500
frame = 0
step_counter = 0

for animation in animation_steps:
    temp_img_list = []
    for _ in range(animation):
        temp_img_list.append(sprite_sheet.get_image(step_counter, 50, 50, 3, BLACK))
        step_counter += 1
    animation_list.append(temp_img_list)

while True:

    screen.fill(BG)

    current_time = pygame.time.get_ticks()

    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list[action]):
            frame = 0

    screen.blit(animation_list[action][frame], (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and action > 0:
                action -= 1
                frame = 0

            if event.key == pygame.K_UP and action < len(animation_list) - 1:
                action += 1
                frame = 0

        pygame.display.update()

pygame.quit()
