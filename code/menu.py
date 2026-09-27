#!/usr/bin/python
# -*- coding: utf-8 -*-


import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, MENU_OPTION, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./asset/BG_Decor.png")
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer.music.load('./asset/Battle_theme_loopable.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size= 80, text="Forest",text_color= (255,128,0),text_center_pos=((WIN_WIDTH/2), 70))
            self.menu_text(text_size=80, text="Survival",text_color=(255,128,0), text_center_pos=((WIN_WIDTH / 2), 150))

            for i in range(len(MENU_OPTION)):
                self.menu_text(text_size= 40, text=MENU_OPTION[i],text_color= COLOR_WHITE,text_center_pos=((WIN_WIDTH/2), 300 + 50 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                      pygame.quit()
                      quit()
    def menu_text(self, text_size:int, text: str, text_color: tuple, text_center_pos: tuple, antialias=None):
        text_font: Font = pygame.font.SysFont(name= "Impact", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

