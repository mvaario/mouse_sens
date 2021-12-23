# Games objects
# Fov 0 = game has slider for FOV
# fov_h = if fov is horizontal
# Aspect ratio = FOV aspect ratio
import math

class objects:
    def cs_go():
        multi = 1
        fov = math.radians(90)
        fov_h = True
        default_aspect = [4, 3]

        return multi, fov, fov_h, default_aspect

    def cod_1():
        multi = 1
        fov = math.radians(80)
        fov_h = True
        default_aspect = [4, 3]

        return multi, fov, fov_h, default_aspect

    def valorant():
        multi = 0.314285714
        fov = math.radians(103)
        fov_h = True
        default_aspect = [16, 9]

        return multi, fov, fov_h, default_aspect

    def quake_champions():
        multi = 1
        fov = 0
        fov_h = True
        default_aspect = [16, 9]

        return multi, fov, fov_h, default_aspect

    def EFT():
        multi = 0.1760000
        fov = 0
        fov_h = False
        default_aspect = [16, 9]

        return multi, fov, fov_h, default_aspect

    def r6():
        multi = 3.8397238
        fov = 0
        fov_h = False
        default_aspect = [16, 9]

        return multi, fov, fov_h, default_aspect

    def new_game():
        multi = float(input("Game sensitivity multiplier:"))
        fov = float(input("Game horizontal FOV:"))
        fov_h = True
        default_aspect = [16, 9]
        return multi, fov, fov_h, default_aspect






