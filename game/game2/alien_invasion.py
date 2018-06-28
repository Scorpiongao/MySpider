import pygame
from settings import Settings
from ship import Ship
import game_function as gf
from pygame .sprite import  Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from alien import Alien


def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings=Settings ()
    screen=pygame .display .set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display .set_caption('Alien Invasion')

    #创建Play按钮
    play_button =Button (ai_settings ,screen ,'Play')
    ship=Ship (ai_settings,screen)
    alien=Alien (ai_settings,screen)
    #设置背景颜色
    # bg_color=(230,230,230)
    #存储飞船子弹的编组
    bullets=Group ()

    # 存储外星人子弹的编组
    alien_bullets = Group()

    # alien=Alien (ai_settings,screen)
    aliens=Group ()

    #创建外星人群
    gf.create_fleet(ai_settings ,screen ,ship, aliens)

    #创建一个用于存储游戏统计信息的实例
    stats=GameStats (ai_settings )

    sb=Scoreboard (ai_settings,screen ,stats )

    while True :
        #监听键盘和鼠标事件
        gf.check_events(ai_settings,stats,screen,sb,ship,aliens ,bullets,play_button,alien_bullets )

        if stats.game_active :

            ship.update()

            #删除消失的子弹
            gf.update_alien_bullets(ai_settings ,stats,screen ,sb,ship,aliens,bullets ,alien_bullets )

            gf.update_bullets(ai_settings ,stats,screen ,sb,ship,aliens,bullets)

            gf.update_aliens(ai_settings,stats,screen,sb,ship,alien,aliens,bullets,alien_bullets)



        gf.update_screen(ai_settings,stats,screen,sb,ship,aliens,bullets,play_button,alien_bullets )

run_game()