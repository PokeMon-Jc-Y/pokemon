import pygame,sys
from pygame.locals import *


class AttackSystem:

    def __init__(self):
        pygame.init()
        # The location of arrow
        self.background_default_options = 1
        # Load the image from local and resize them
        self.arrow_image = pygame.transform.scale(pygame.image.load('image/attack_system_images/arrow_for_options.jpg'),(40, 25))
        self.monster_image_front = pygame.transform.scale(pygame.image.load('image/monster_images/mudkip_front.png'), (80, 80))
        self.player_monster_image = pygame.transform.scale(pygame.image.load('image/monster_images/mudkip_back.png'), (130, 130))
        self.background_image = pygame.transform.scale(pygame.image.load('image/attack_system_images/white_background.jpg'),(40, 40))
        self.background_image_screen = pygame.transform.scale(pygame.image.load('image/attack_system_images/battle_background.jpg'),(600, 440))
        self.arrow_image_angle = pygame.transform.rotate(self.arrow_image,270)
        # Set the title
        pygame.display.set_caption("Attack System")
        self.screen = pygame.display.set_mode((600, 600))
        self.screen.fill((255,255,255))
        # Monster and player's distance ti the left screen
        self.monster_left = 0
        self.player_left = 0
        # FPS
        self.FPS_CLOCK = pygame.time.Clock()

    # Load the 4 position in the option rect
    def __options_refresh(self):
        if self.background_default_options == 1:
            self.screen.blit(self.arrow_image,[300,460])
        if self.background_default_options == 2:
            self.screen.blit(self.arrow_image,[440,460])
        if self.background_default_options == 3:
            self.screen.blit(self.arrow_image,[300,530])
        if self.background_default_options == 4:
            self.screen.blit(self.arrow_image,[440,530])

    # Change the background_default_option by input, in order to change the arrow's location by map
    def __arrow_movement(self,direction):
        # get the location of the arrow
        if self.background_default_options == 1:
            if direction == 'd':
                self.background_default_options = 2
            if direction == 's':
                self.background_default_options = 3
        if self.background_default_options == 2:
            if direction == 'a':
                self.background_default_options = 1
            if direction == 's':
                self.background_default_options = 4
        if self.background_default_options == 3:
            if direction == 'w':
                self.background_default_options = 1
            if direction == 'd':
                self.background_default_options = 4
        if self.background_default_options == 4:
            if direction == 'w':
                self.background_default_options = 2
            if direction == 'a':
                self.background_default_options = 3

    # Draw a rect to hold the options
    def __draw_attack_rect(self,press):
        # Draw the rect
        to_top = 440
        to_left = 0
        rect_width = 600
        rect_height = 160
        pygame.draw.rect(self.screen, (0, 0, 0), [to_left,to_top,rect_width,rect_height], 2)
        # Draw the text for 4 options(Attack,Package,Monster,Run)
        font = pygame.font.Font('freesansbold.ttf', 22)
        attack_text = font.render('Attack', True, (0, 0, 0))
        package_text = font.render('Package', True, (0, 0, 0))
        monster_text = font.render('Monster', True, (0, 0, 0))
        run_text = font.render('Run', True, (0, 0, 0))
        first_talk_text = font.render('The monster *** came out', True, (0, 0, 0))

        if press == 'j':
            self.screen.blit(attack_text, (350, 460))
            self. screen.blit(package_text, (490, 460))
            self.screen.blit(monster_text, (350, 530))
            self.screen.blit(run_text, (490, 530))
        else:
            self.screen.blit(first_talk_text, (10, 460))
            self.screen.blit(self.arrow_image_angle, (550, 550))

    # monster and player's intro
    def monster_player_intro(self):
        self.screen.blit(self.background_image_screen, [0, 0])
        if self.monster_left <= 400:
            self.monster_left += 5
        if self.player_left <= 150:
            self.player_left += 3
        self.screen.blit(self.monster_image_front, [self.monster_left, 50])
        self.screen.blit(self.player_monster_image, [self.player_left, 300])

    # Get new event from keyboard(change options by click W,A,S,D)
    def attack_start(self):
        talk_continue = False
        animation_finish = False
        while True:
            print(self.FPS_CLOCK)
            self.screen.fill((255, 255, 255))
            self.monster_player_intro()
            # Show the options and conversation when the animation is finished
            if self.player_left >= 150 and self.monster_left >= 400:
                animation_finish = True
                if talk_continue:
                    self.__draw_attack_rect('j')
                else:
                    self.__draw_attack_rect('')
            if animation_finish and talk_continue:
                self.__options_refresh()
            for event in pygame.event.get():
                # Quit the system
                if event.type == pygame.QUIT:
                    print('-Test end-')
                    pygame.quit()
                    quit()
                # Get input from keyboard and react
                if animation_finish:
                    if event.type == pygame.KEYDOWN:
                        if event.key == K_w:
                            self.__arrow_movement('w')
                            self.__options_refresh()
                        if event.key == K_a:
                            self.__arrow_movement('a')
                            self.__options_refresh()
                        if event.key == K_s:
                            self.__arrow_movement('s')
                            self.__options_refresh()
                        if event.key == K_d:
                            self.__arrow_movement('d')
                            self.__options_refresh()
                        if event.key == K_j:
                            if not talk_continue:
                                talk_continue = True

            pygame.display.update()
            self.FPS_CLOCK.tick(30)


a = AttackSystem
b = a()
b.attack_start()

