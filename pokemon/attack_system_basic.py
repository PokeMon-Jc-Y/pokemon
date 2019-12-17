import pygame,sys
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
FPS = 30
FPS_CLOCK = pygame.time.Clock()
monster_left = -80
player_left = -80
# Load the image from local and resize them
arrow_image = pygame.transform.scale(pygame.image.load('image/attack_system_images/arrow_for_attack_system.png').convert(),(40,25))
monster_image = pygame.transform.scale(pygame.image.load('image/attack_system_images/test_monster_for_attack_system.png').convert(),(80,80))
player_image = pygame.transform.scale(pygame.image.load('image/attack_system_images/test_player_for_attack_system.png').convert(),(80,80))
background_image = pygame.transform.scale(pygame.image.load('image/attack_system_images/white_background.jpg').convert(),(40,40))
background_default_options = [arrow_image, background_image, background_image, background_image]
# Set the title
pygame.display.set_caption("Attack System")
screen.fill((255, 255, 255))


# Load the 4 position in the option rect
def __options_refresh():
    screen.blit(background_default_options[0], [300, 460])
    screen.blit(background_default_options[1], [440, 460])
    screen.blit(background_default_options[2], [300, 530])
    screen.blit(background_default_options[3], [440, 530])


# Change the background_default_option by input, in order to change the arrow's location by map
def __arrow_movement(direction):
    # get the location of the arrow
    if background_default_options[0] == arrow_image:
        if direction == 'd':
            background_default_options[0] = background_image
            background_default_options[1] = arrow_image
        if direction == 's':
            background_default_options[0] = background_image
            background_default_options[2] = arrow_image

    if background_default_options[1] == arrow_image:
        if direction == 'a':
            background_default_options[1] = background_image
            background_default_options[0] = arrow_image
        if direction == 's':
            background_default_options[1] = background_image
            background_default_options[3] = arrow_image

    if background_default_options[2] == arrow_image:
        if direction == 'w':
            background_default_options[2] = background_image
            background_default_options[0] = arrow_image
        if direction == 'd':
            background_default_options[2] = background_image
            background_default_options[3] = arrow_image

    if background_default_options[3] == arrow_image:
        if direction == 'w':
            background_default_options[3] = background_image
            background_default_options[1] = arrow_image
        if direction == 'a':
            background_default_options[3] = background_image
            background_default_options[2] = arrow_image


# Get new event from keyboard(change options by click W,A,S,D)
def __attack_start():
    __options_refresh()
    __draw_attack_rect()

    while True:
        # __set_animation()

        for event in pygame.event.get():
            # Quit the system
            if event.type == pygame.QUIT:
                print('-You quit the attack system successfully-')
                pygame.quit()
                quit()
            # Get input from keyboard and react
            if event.type == pygame.KEYDOWN:
                if event.key == K_w:
                    __arrow_movement('w')
                    __options_refresh()
                if event.key == K_a:
                    __arrow_movement('a')
                    __options_refresh()
                if event.key == K_s:
                    __arrow_movement('s')
                    __options_refresh()
                if event.key == K_d:
                    __arrow_movement('d')
                    __options_refresh()

        pygame.display.update()


# Draw a rect to hold the options
def __draw_attack_rect():
    # Draw the rect
    to_top = 440
    to_left = 290
    rect_width = 300
    rect_height = 150
    pygame.draw.rect(screen, (0,0,0), [to_left,to_top,rect_width,rect_height], 2)
    # Draw the text for 4 options
    font = pygame.font.Font('freesansbold.ttf', 22)
    attack_text = font.render('Attack',True,(0,0,0))
    package_text = font.render('Package',True,(0,0,0))
    monster_text = font.render('Monster',True,(0,0,0))
    run_text = font.render('Run',True,(0,0,0))

    screen.blit(attack_text,(350,460))
    screen.blit(package_text,(490,460))
    screen.blit(monster_text,(350,530))
    screen.blit(run_text,(490,530))

    print('-The attack rect system successfully drew-')


__attack_start()
pygame.time.delay(30)