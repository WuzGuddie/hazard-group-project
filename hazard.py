class HolyWater(Hazard):
    sprite = image.load("assets/sprites/hazards/holy_water.png")

    def __init__(self, x, y):
        super().__init__(x, y, self.sprite)
        self.state = "ACTIVE"

    def active(self):
        if self.rect.colliderect(self.player.rect):
            self.player.take_damage(2)

    def update(self, _dt):
        self.active()


class HazardManager:
    _instance = None
    grid_size = tuple([15, 31])
    hazards: list[Hazard] = []

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance

    def load_hazards(self):
        self.hazards = []
        half_row = self.grid_size[0] // 2
        half_col = self.grid_size[1] // 2
        for row_ind in range(1, self.grid_size[0]):
            for col_ind in range(1, self.grid_size[1]):
                if ((row_ind == half_row or row_ind == half_row + 1) and
                        (col_ind == half_col or col_ind == half_col + 1)):
                    continue
                rand_num = random.randint(1, 100)
                if rand_num <= 10:
                    hazard = Spike(col_ind * 40, row_ind * 40)
                    self.hazards.append(hazard)
#10% chance of spawning spikes
                elif rand_num > 10 and rand_num <=15:
                    hazard = HolyWater(col_ind * 40, row_ind * 40)
                    self.hazards.append(hazard)
#5% chance of spawning holywater
    def update(self, _dt):
        for h in self.hazards:
            h.update(_dt)

    def draw(self):
        for h in self.hazards:
            h.draw()