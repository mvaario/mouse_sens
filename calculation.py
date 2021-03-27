# Calculating same sensitivity to different games

import math
from objects import *

class games:

    def __init__(self):
        # Games
        self.games = ['cs go', 'Cod 1', 'Valorant', 'Quake', 'Eft', 'R6']

        self.fov_1 = 0
        self.fov_2 = 0

        self.default_aspect_1 = 0
        self.default_aspect_2 = 0

        self.fov_h1 = False
        self.fov_h2 = False

        self.multiplier = 0

        self.aspect_ratio1 = [0, 0]
        self.aspect_ratio2 = [0, 0]

        self.sensitivity = 0


    def print(self):
        print("")
        print("Choose games")
        print("Cs Go = 0")
        print("Cod = 1")
        print("Valorant = 2")
        print("Quake = 3")
        print("EFT = 4")
        print("R6 = 5")
        print("Else = 6")
        print("")

        return

    def getting_info(self, game):
        try:
            if game == 0:
                multi, fov, fov_h, aspect = objects.cs_go()
            elif game == 1:
                multi, fov, fov_h, aspect = objects.cod_1()
            elif game == 2:
                multi, fov, fov_h, aspect = objects.EFT()
            elif game == 3:
                multi, fov, fov_h, aspect = objects.EFT()
            elif game == 4:
                multi, fov, fov_h, aspect = objects.EFT()
            elif game == 5:
                multi, fov, fov_h, aspect = objects.EFT()
            else:
                multi, fov, fov_h, aspect = objects.cs_go()

            # if game has FOV slider
            if fov == 0:
                fov = int(input(f'{games.games[game]} Field of view: '))

            x = int(input("Aspect x: "))
            y = int(input("Aspect y: "))

            aspect_ratio = [x, y]

        except:
            print("Error")
            quit()

        return multi, fov, fov_h, aspect, aspect_ratio

    def calculation(self):
        fov_1 = games.fov_1
        fov_2 = games.fov_2

        # Changing game 1 vertical FOV to horizontal
        if not games.fov_h1:
            fov = games.fov_1
            fov = math.radians(fov)

            aspect_ratio = games.default_aspect_1
            aspect_ratio = [aspect_ratio[1], aspect_ratio[0]]

            fov_1 = games.fov_changer(fov, aspect_ratio)

        # Changing game 2 vertical FOV to horizontal
        if not games.fov_h2:
            fov = games.fov_2
            fov = math.radians(fov)

            aspect_ratio = games.default_aspect_2
            aspect_ratio = [aspect_ratio[1], aspect_ratio[0]]

            fov_2 = games.fov_changer(fov, aspect_ratio)


        # Actual horizontal FOV in game 1
        if sum(games.aspect_ratio1) != sum(games.default_aspect_1):
            fov_1 = games.fov_calculation(fov_1)
        else:
            fov_1 = math.degrees(fov_1)


        # Actual horizontal FOV in game 2
        if sum(games.aspect_ratio2) != sum(games.default_aspect_2):
            fov_2 = games.fov_calculation(fov_2)
        else:
            fov_2 = math.degrees(fov_2)

        games.fov_1 = fov_1
        games.fov_2 = fov_2



        return

    def fov_calculation(self, fov):
        # Calculating vertical FOV
        aspect_ratio = games.default_aspect_1
        fov_v = games.fov_changer(fov, aspect_ratio)

        # Calculating new horizontal FOV
        x = games.aspect_ratio1[0]
        y = games.aspect_ratio1[1]

        c = y / math.tan(math.radians(fov_v) / 2)

        fov_h = math.atan(x / c) * 2
        fov_h = math.degrees(fov_h)

        return fov_h

    def fov_changer(self, fov, aspect_ratio):
        # Calculating vertical FOV
        x = aspect_ratio[0]
        y = aspect_ratio[1]

        fov = math.atan(y / (x / math.tan(fov / 2))) * 2
        fov = math.degrees(fov)

        return fov

    def new_sensitivity(self):
        multi = games.multiplier
        fov_1 = games.fov_1 / 2
        fov_2 = games.fov_2 / 2
        sensitivity = games.sensitivity

        # Calculating fov difference
        fov_1 = math.radians(fov_1)
        fov_2 = math.radians(fov_2)

        fov = math.tan(fov_2) / math.tan(fov_1)

        new_sensitivity = multi * fov * sensitivity

        print("")
        print("FOV difference:", round(fov, 3))
        print("Game engine multiplier difference:", round(multi, 3))
        print("New sensitivity:", new_sensitivity)

        return


if __name__ == '__main__':
    games = games()

    # Ask games
    games.print()
    game = int(input("From game: "))
    multi, fov, fov_h, aspect, aspect_ratio = games.getting_info(game)

    multi_1 = multi
    games.fov_1 = fov
    games.fov_h1 = fov_h
    games.default_aspect_1 = aspect
    games.aspect_ratio1 = aspect_ratio

    sensitivity = float(input("Sensitivity: "))
    games.sensitivity = sensitivity
    print("")


    game = int(input("To game: "))
    multi, fov, fov_h, aspect, aspect_ratio = games.getting_info(game)

    multi_2 = multi
    games.fov_2 = fov
    games.fov_h2 = fov_h
    games.default_aspect_2 = aspect
    games.aspect_ratio2 = aspect_ratio

    games.multiplier = multi_2 / multi_1

    games.calculation()

    # Calculating new sensitivity
    games.new_sensitivity()