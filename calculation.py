# Calculating same sensitivity to different games

import math
from objects import *

class calculations:
    def __init__(self):
        # Games
        self.games = ['cs go', 'Cod 1', 'Valorant', 'Quake', 'Eft', 'R6', 'Overwatch 2']
        self.game_1 = 0
        self.game_2 = 0

        self.multi_1 = 0
        self.multi_2 = 0

        self.fov_1 = 0
        self.fov_2 = 0

        self.used_aspect_1 = []
        self.used_aspect_2 = []

        self.sensitivity = 0
        self.new_sensitivity = 0

    # Calculating vertical
    def fov_changer(self, fov, default_aspect):
        x = default_aspect[0]
        y = default_aspect[1]

        c = x / math.tan(fov / 2)

        v_fov = math.atan(y / c) * 2
        return v_fov

    # Calculating actual horizontal FOV
    def aspect_ratio_calculation(self, v_fov, used_aspect):
        x = used_aspect[0] / 2
        y = used_aspect[1] / 2

        c = y / math.tan(v_fov / 2)

        h_fov = math.atan(x / c) * 2
        return h_fov

    # Calculate FOV difference
    def fov_difference(self):
        fov_1 = self.fov_1 / 2
        fov_2 = self.fov_2 / 2

        f_1 = math.tan(fov_1)
        f_2 = math.tan(fov_2)

        difference = f_2 / f_1

        return difference

    # Calculating new sensitivity
    def calculate_sensitivity(self, difference):
        # multiplier difference
        multiplier = self.multi_2 / self.multi_1

        # new sensitivity
        new_sensitivity = multiplier * difference * self.sensitivity

        return new_sensitivity
