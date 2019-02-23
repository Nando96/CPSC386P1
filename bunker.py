from pygame import sprite, Surface, PixelArray
from random import randrange
from pygame.sprite import Sprite


class BunkerBlock(Sprite):
    def __init__(self, ai_settings, screen, row, col):
        super(BunkerBlock, self).__init__()
        self.screen = screen
        self.height = ai_settings.bunker_block_size
        self.width = ai_settings.bunker_block_size
        self.color = ai_settings.bunker_color
        self.image = Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.row = row
        self.col = col
        self.dmg = False

    def damage(self, top):
        if not self.dmg:
            px_array = PixelArray(self.image)
            if top:
                for i in range(self.height * 3):
                    px_array[randrange(0, self.width - 1),
                             randrange(0, self.height // 2)] = (0, 0, 0, 0)  # transparent pixel
            else:
                for i in range(self.height * 3):
                    px_array[randrange(0, self.width - 1),
                             randrange(self.height // 2, self.height - 1)] = (0, 0, 0, 0)   # transparent pixel
            self.dmg = True
        else:
            self.kill()

    def update(self):
        self.screen.blit(self.image, self.rect)


def make_bunker(ai_settings, screen, position):
    bunker = sprite.Group()
    for row in range(5):
        for col in range(12):
            if not (row > 4 and (4 < col < 10)):
                block = BunkerBlock(ai_settings, screen, row, col)
                block.rect.x = int(ai_settings.screen_width * 0.15) + (250 * position) + (col * block.width)
                block.rect.y = int(ai_settings.screen_height * 0.8) + (row * block.height)
                bunker.add(block)
    return bunker
