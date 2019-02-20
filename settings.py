class Settings():
    def __init__(self):
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 900
        self.bg_color = (0, 0, 0)

        # Ship settings.
        self.ship_limit = 3

        # Bullet settings.
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        #lazer settings
        self.lazer_speed = None
        self.lazer_ok = 2
        self.beam_stamp = None
        self.beam_time = 30

        self.fleet_drop_speed = 10
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.bunker_block_size = 10
        self.bunker_color = (0, 255, 0)

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 3
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        self.lazer_speed = 3

        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)