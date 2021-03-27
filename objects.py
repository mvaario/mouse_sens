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
        aspect = [4, 3]

        return multi, fov, fov_h, aspect

    def cod_1():
        multi = 1
        fov = math.radians(80)
        fov_h = True
        aspect = [4, 3]

        return multi, fov, fov_h, aspect

    def valorant():
        multi = 1
        fov = 90
        fov_h = True
        aspect = [16, 9]

        return multi, fov, fov_h, aspect

    def quake_live():
        multi = 1
        fov = 0
        fov_h = True
        aspect = [16, 9]

        return multi, fov, fov_h, aspect

    def EFT():
        multi = 1
        fov = 0
        fov_h = False
        aspect = [16, 9]

        return multi, fov, fov_h, aspect

    def r6():
        multi = 1
        fov = 0
        fov_h = False
        aspect = [16, 9]

        return multi, fov, fov_h, aspect

    def new_game():

        return






