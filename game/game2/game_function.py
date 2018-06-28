import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
from alien_bullet import AlienBullet

filename = 'high_score.txt'



def check_events(ai_settings,stats,screen,sb,ship,aliens,bullets,play_button,alien_bullets):
    '''响应按键和鼠标事件'''
    # 监听键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            remember_high_score(stats,filename)
            sys.exit()

        elif event .type==pygame .KEYDOWN :
            check_keydown_events(event,ai_settings,stats,screen,ship,aliens,bullets,alien_bullets)

        elif event.type ==pygame .KEYUP :
            check_keyup_events(event,ship)

        elif event .type==pygame .MOUSEBUTTONDOWN :
            mouse_x,mouse_y =pygame .mouse.get_pos()
            check_play_button(ai_settings,stats,screen,sb,ship,aliens,bullets,play_button,mouse_x ,mouse_y )

def check_keydown_events(event,ai_settings,stats,screen,ship,aliens,bullets,alien_bullets):
    '''响应按键'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    elif event .key ==pygame .K_UP :
        ship.moving_up =True

        alien_fire_bullet(ai_settings, screen, aliens, alien_bullets)

    elif event .key ==pygame .K_DOWN  :
        ship.moving_down =True

    elif event .key ==pygame .K_SPACE :
        fire_bullet(ai_settings,screen,ship,bullets)

        alien_fire_bullet(ai_settings, screen, aliens, alien_bullets)

    elif event.key==pygame .K_q :
        remember_high_score(stats,filename)
        sys.exit()

def fire_bullet(ai_settings ,screen,ship,bullets) :
    if len(bullets ) < ai_settings .bullets_allowed:
        new_bullet=Bullet (ai_settings ,screen,ship)
        bullets .add(new_bullet )

def alien_fire_bullet(ai_settings,screen,aliens,alien_bullents):
    for alien in aliens .sprites ():
        if len(alien_bullents ) < ai_settings .alien_bullets_allowed:
            alien_new_bullet=AlienBullet (ai_settings ,screen ,alien )
            alien_bullents .add(alien_new_bullet )



def check_keyup_events(event,ship):
    '''响应松开'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP :
        ship.moving_up = False
    elif event.key == pygame.K_DOWN  :
        ship.moving_down = False

def update_screen(ai_settings,stats,screen,sb,ship,aliens,bullets,play_button,alien_bullets):
    '''更新屏幕的图像，并切换到新屏幕'''
    # 背景颜色
    screen.fill(ai_settings.bg_color)

    for bullet in bullets .sprites():
        bullet .draw_bullet()

    for alien_bullet in alien_bullets .sprites():
        alien_bullet .draw_bullet()

    ship.blitme()
    # alien.blitme()
    aliens.draw(screen )


    #显示得分
    sb.show_score()
    #如果游戏处于非活动状态，绘制play按钮
    if not stats.game_active:
        play_button .draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(ai_settings,stats,screen,sb,ship,aliens,bullets):
    '''更新子弹位置，删除消失的子弹'''
    bullets.update()
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # print(len(bullets))
    check_bullet_alien_collisions(ai_settings,stats,screen,sb,ship,aliens,bullets)

def update_alien_bullets(ai_settings,stats,screen,sb,ship,aliens,bullets,alien_bullets):

    # alien_bullets.update()
    #删除消失的子弹
    alien_bullets .update()
    for alien_bullet in alien_bullets .copy() :
        if alien_bullet .rect.top >= ai_settings .screen_height :
            alien_bullets .remove(alien_bullet)

    #检查双方的子弹是否碰撞,并删除
    collisions=pygame .sprite.groupcollide(bullets ,alien_bullets ,True ,True)

    #检查是否被击中
    if pygame .sprite.spritecollideany(ship,alien_bullets):
        ship_hit(ai_settings ,stats,screen,sb,ship,aliens,bullets,alien_bullets)


def check_bullet_alien_collisions(ai_settings,stats,screen,sb,ship,aliens,bullets):
    # 检查是否有子弹击中了外星人
    # 如果是，就删除相应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions :
        for aliens in collisions .values() :
            stats.score += ai_settings .alien_points *len(aliens )
            sb.prep_score()
        check_high_score(stats ,sb)

    start_new_level(ai_settings,stats,screen,sb,ship,aliens,bullets)


def start_new_level(ai_settings,stats,screen,sb,ship,aliens,bullets):
    if len(aliens) == 0:
        # 清空子弹,加快节奏并新建一群外星人
        bullets.empty()
        ai_settings.increase_speed()
        #提高等级
        stats .level +=1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)


def create_fleet(ai_settings,screen,ship,aliens):
    '''创建外人群'''
    #创建一个外星人，并计算一行可容纳多少个外星人
    #外星人间距为外星人宽度
    alien=Alien (ai_settings ,screen )
    number_aliens_x=get_number_aliens_x(ai_settings,alien.rect .width)
    number_rows=get_number_rows(ai_settings,ship.rect.height,alien.rect.height )

    for row_number in range (number_rows ):
    #创建第一行外星人
        for alien_number in range(number_aliens_x ):
            create_alien(ai_settings,screen,aliens ,alien_number,row_number )

def get_number_aliens_x(ai_settings,alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    '''创建一外星人放在当前行'''
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_number * alien_width
    alien.rect.x = alien.x
    alien .rect.y=alien.rect.height+2*alien .rect.height*row_number
    aliens.add(alien)

def get_number_rows(ai_settings,ship_height,alien_height):
    '''计算可容纳多少行外星人'''
    available_space_y=(ai_settings .screen_height - ship_height -(3*alien_height ))
    number_rows=int(available_space_y /(3*alien_height ))
    return number_rows

def update_aliens(ai_settings,stats,screen,sb,ship,alien,aliens,bullets,alien_bullets):
    '''检查是否有外星人位于屏幕边缘并更新外星人群的位置'''
    check_fleet_edges(ai_settings ,alien,aliens )

    aliens .update()

    #检测外星人和飞船的碰撞、
    if pygame .sprite.spritecollideany(ship,aliens ) :
        # print('Ship hit!!!')
        ship_hit(ai_settings,stats,screen,sb,ship,aliens ,bullets,alien_bullets )

    check_aliens_bottom(ai_settings ,stats ,screen ,sb,ship ,aliens ,bullets ,alien_bullets)



def change_fleet_direction(ai_settings,alien,aliens):
    '''整个外星人群下移并改变方向'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings .fleet_drop_speed
    alien.moving_down = True

    ai_settings .fleet_direction *= -1

    alien.moving_down =False

def check_fleet_edges(ai_settings,alien1,aliens):
    '''有外星人到达边缘时采取措施'''
    for alien in aliens .sprites ():
        if alien.check_edges() :
            change_fleet_direction(ai_settings,alien1,aliens)
            break


def ship_hit(ai_settings,stats,screen,sb,ship,aliens,bullets,alien_bullets):
    '''相应被外星人撞到的飞船'''
    if stats .ships_left >0:
        stats .ships_left -=1

        #更新飞船数量
        sb.prep_ships ()

        #清空子弹和外星人列表
        aliens .empty()
        bullets .empty ()
        alien_bullets.empty()

        #创建一群新的外星人，并将飞船放到屏幕底端中央
        create_fleet(ai_settings ,screen ,ship ,aliens)
        ship.center_ship()

        sleep(1)
    else:
        stats .game_active=False
        pygame .mouse.set_visible(True )

def check_aliens_bottom(ai_settings,stats,screen,sb,ship,aliens,bullets,alien_bullets):
    '''检查是否有外星人到达了屏幕底端'''
    screen_rect=screen .get_rect()
    for alien in aliens .sprites ():
        if alien.rect.bottom>=screen_rect.bottom:
            ship_hit(ai_settings ,stats ,screen ,sb,ship,aliens,bullets,alien_bullets )
            break

def check_play_button(ai_settings,stats,screen,sb,ship,aliens,bullets,play_button,mouse_x,mouse_y):
    '''点击play后开始游戏'''
    button_click=play_button .rect.collidepoint(mouse_x ,mouse_y )
    if button_click and not stats .game_active :
        #重置游戏的动态设置
        ai_settings .initialize_dynamic_settings()

        #隐藏光标
        pygame .mouse.set_visible(False)

        #重置游戏统计信息
        stats .reset_stats()
        stats .game_active =True

        #重置记分牌图像
        sb.prep_score ()
        sb.prep_high_score ()
        sb.prep_level ()
        sb.prep_ships()

        #清空外星人和子弹列表
        aliens .empty()
        bullets .empty ()

        #创建一群新的外星人，飞船居中
        create_fleet(ai_settings ,screen ,ship,aliens )
        ship.center_ship()


def check_high_score(stats,sb):
    '''检查是否诞生了最高分'''
    if stats.score > stats .high_score:
        stats .high_score =stats .score
        sb.prep_high_score()

def remember_high_score(stats,filename):
    '''记录最高得分'''
    with open (filename ,'w')as f:
        f.write(str(stats.high_score).strip(",") )

def get_high_score(filename):
    '''游戏开始时读取最高分'''
    with open(filename ,'r')as f:
        high_score=int(f.readline().strip() )
        return high_score