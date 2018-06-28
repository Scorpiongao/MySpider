class Settings():
    '''存储《外星人入侵》的所有设置的类'''
    def __init__(self):
        '''初始化游戏的静态设置'''
        #屏幕设置
        self.screen_width=1000
        self.screen_height=600
        self.bg_color=(230,230,230)

        #飞船的设置
        self.ship_limit=4

         #飞船子弹设置
        # self.bullet_width=300
        self.bullet_height=15
        self.bullet_color=255,0,0
        self.bullets_allowed=10

        #外星人子弹设置
        self.alien_bullet_width=3
        self.alien_bullet_height = 15
        self.alien_bullet_color = 0, 0, 255

        #外星人设置
        # self.fleet_drop_speed = 10
        #节奏加快的速度
        self.speedup_scale=1.1
        #点数加快的速度
        self.score_scale=1.5

        #子弹变宽
        # self.width_scale=2

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        '''初始化动态设置'''
        # 飞船的设置
        self.ship_speed_factor = 1.5

        # 子弹设置
        self.bullet_width = 20
        self.bullet_speed_factor = 3
        self.alien_bullet_apeed_factor=1
        # 外星人设置
        self.alien_speed_factor = 1
        # fleet_direction=1:右
        # fleet_direction=-1:左
        self.fleet_direction = 1

        self.alien_bullets_allowed = 10

        self.fleet_drop_speed = 10

        #记分
        self.alien_points=100

    def increase_speed(self):
        '''提高速度的设置'''
        self.ship_speed_factor *=self.speedup_scale
        self.bullet_speed_factor *=self.speedup_scale
        self.alien_speed_factor *=self.speedup_scale

        self.fleet_drop_speed *=self.speedup_scale

        self.alien_bullets_allowed *=self.speedup_scale

        if self.bullet_width < self.screen_width :
            self.bullet_width = int(self.bullet_width * self.score_scale)
        else:
            self.bullet_width = self.screen_width

        self.alien_points = int(self.alien_points *self.score_scale )
