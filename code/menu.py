#!/usr/bin/python
# -*- coding: utf-8 -*-


import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW, CONTROLS


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./asset/Cartoon_Forest_BG_03.png")
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option=0

        pygame.mixer.music.load('./asset/Battle_theme_loopable.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size= 80, text="Forest",text_color= (255,128,0),text_center_pos=((WIN_WIDTH/2), 70),font_name="Impact")
            self.menu_text(text_size=80, text="Survival",text_color=(255,128,0), text_center_pos=((WIN_WIDTH / 2), 150),font_name="Impact")

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(text_size= 40, text=MENU_OPTION[i],text_color=COLOR_YELLOW,text_center_pos=((WIN_WIDTH/2), 300 + 50 * i))
                else:
                    self.menu_text(text_size=40, text=MENU_OPTION[i], text_color=COLOR_WHITE,
                               text_center_pos=((WIN_WIDTH / 2), 300 + 50 * i))


            self.menu_text(
                text_size=30,
                text="CONTROLES",
                text_color=(255, 128, 0),
                text_center_pos=(730, 500)
            )

            for i in range(len(CONTROLS)):
                self.menu_text(
                    text_size=20,
                    text=CONTROLS[i],
                    text_color=COLOR_WHITE,
                    text_center_pos=(730, 545 + 35 * i)
                )
            pygame.display.flip()

            for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                      pygame.quit()
                      quit()
                 if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # ENTER
                        return MENU_OPTION[menu_option]



    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, antialias=None,
        font_name="Arial"):
        text_font: Font = pygame.font.SysFont(name=font_name, size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

