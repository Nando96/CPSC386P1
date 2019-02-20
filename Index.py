import spritesheet, pygame

class index:


    def __init__(self):
        Ss = spritesheet.spritesheet('images/SS.bmp')
        Sss = spritesheet.spritesheet('images/laz.png')

        self.a1 = []
        self.a1.append(Ss.image_at((0, 0, 32, 32)))
        self.a1.append(Ss.image_at((0, 32, 32, 32)))
        self.a2 = []
        self.a2.append(Ss.image_at((0, 32 * 2, 32, 32)))
        self.a2.append(Ss.image_at((0, 32 * 3, 32, 32)))
        self.a3 = []
        self.a3.append(Ss.image_at((0, 32 * 4, 32, 32)))
        self.a3.append(Ss.image_at((0, 32 * 5, 32, 32)))
        self.a4 = []
        self.a4.append(Ss.image_at((0, 32 * 6, 32, 32)))
        self.a4.append(Ss.image_at((0, 32 * 7, 32, 32)))
        self.s1 = []
        self.s1.append(Ss.image_at((0, 32 * 19, 32, 32)))
        self.s1.append(Ss.image_at((0, 32 * 20, 32, 32)))
        self.E1 = []
        self.E1.append(Ss.image_at((0, 32 * 14, 32, 32)))
        self.E1.append(Ss.image_at((0, 32 * 15, 32, 32)))
        self.E1.append(Ss.image_at((0, 32 * 16, 32, 32)))
        self.E1.append(Ss.image_at((0, 32 * 17, 32, 32)))
        self.E1.append(Ss.image_at((0, 32 * 18, 32, 32)))
        self.L1 = []
        self.L1.append(Sss.image_at((0, 0, 32, 32)))
        self.L1.append(Sss.image_at((0, 32, 32, 32)))
        self.L1.append(Sss.image_at((0, 32 * 2, 32, 32)))
        self.L1.append(Sss.image_at((0, 32 * 3, 32, 32)))
        self.L1.append(Sss.image_at((0, 32 * 4, 32, 32)))
        self.L1.append(Sss.image_at((0, 32 * 5, 32, 32)))
        self.L1.append(Sss.image_at((0, 32 * 6, 32, 32)))
        self.L1.append(Sss.image_at((0, 32 * 7, 32, 32)))
        self.L1.append(Sss.image_at((0, 32 * 8, 32, 32)))