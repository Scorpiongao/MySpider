import pygame
from pygame .sprite import  Sprite


class AlienBullet(Sprite ):
    '''单个外星人子弹类'''
    def __init__(self,ai_settings,screen,alien):
        super ().__init__()
        self.screen = screen

        self.rect=pygame .Rect (0,0,ai_settings .alien_bullet_width,
                                ai_settings .alien_bullet_height)
        self.rect.centerx = alien.rect.centerx
        self.rect.y = alien.rect.y

        self.y=float (self.rect .y)

        self.color=ai_settings .alien_bullet_color
        self.speed_factor = ai_settings .alien_bullet_apeed_factor

    def update(self):
        '''下移子弹'''
        self.y +=self.speed_factor
        self.rect.y=self.y

    def draw_bullet(self):
        '''绘制子弹'''
        pygame .draw.rect(self.screen ,self.color ,self.rect )