from pygame.sprite import Sprite


class alienship(Sprite):
    def __init__(self, ai_settings, screen):
        super(alienship, self).__init__()
        # screen, settings, score values
        self.screen = screen
        self.ai_settings = ai_settings
        self.possible_scores = ai_settings.ufo_point_values
        self.score = None