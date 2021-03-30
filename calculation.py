# Calculating same sensitivity to different games

import math
from objects import *

class games:

    def __init__(self):
        # Games
        self.games = ['cs go', 'Cod 1', 'Valorant', 'Quake', 'Eft', 'R6']
        self.game_1 = 0
        self.game_2 = 0

        self.fov_1 = 0
        self.fov_2 = 0

        self.multiplier = 0
        self.sensitivity = 0
        self.new_sensitivity = 0



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

    # Asking game and getting game info
    def getting_info(self, game):
        try:
            if game == 0:
                multi, fov, fov_h, default_aspect = objects.cs_go()
            elif game == 1:
                multi, fov, fov_h, default_aspect = objects.cod_1()
            elif game == 2:
                multi, fov, fov_h, default_aspect = objects.valorant()
            elif game == 3:
                multi, fov, fov_h, default_aspect = objects.quake_champions()
            elif game == 4:
                multi, fov, fov_h, default_aspect = objects.EFT()
            elif game == 5:
                multi, fov, fov_h, default_aspect = objects.r6()
            else:
                multi, fov, fov_h, default_aspect = objects.cs_go()

            # if game has FOV slider
            if fov == 0:
                fov = int(input(f'{games.games[game]} Field of view: '))
                fov = math.radians(fov)


            x = int(input("Aspect x: "))
            y = int(input("Aspect y: "))

            used_aspect = [x, y]

            # if fov is horizontal change it to vertical
            if fov_h:
                v_fov = games.fov_changer(fov, default_aspect)
            else:
                v_fov = fov

            # calculating actual h_fov
            h_fov = games.aspect_ratio_calculation(v_fov, used_aspect)

        except:
            print("Error")
            quit()

        return h_fov, multi

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

    # Calculating new sensitivity
    def calculate_sensitivity(self):
        multi = games.multiplier
        fov_1 = games.fov_1 / 2
        fov_2 = games.fov_2 / 2
        sensitivity = games.sensitivity

        fov_1 = math.tan(fov_1)
        fov_2 = math.tan(fov_2)

        fov = fov_2 / fov_1

        games.new_sensitivity = multi * fov * sensitivity
        print("New sensitivity", games.new_sensitivity)

        return

    # game tweaks
    def tweak(self):
        fov_1 = round(math.degrees(games.fov_1), 3)
        fov_2 = round(math.degrees(games.fov_2), 3)

        print(f'Actual horizontal FOV in {games.games[games.game_1]} {fov_1} degree')
        print(f'Actual horizontal FOV in {games.games[games.game_2]} {fov_2} degree')

        if games.game_1 == 4 or games.game_2 == 4:
            print("EFT change turning speed")
            # around -15% (probably)
            if games.game_1 == 4:
                sensitivity = games.new_sensitivity * 1.15
            else:
                sensitivity = games.new_sensitivity * 0.85

            print("Recommended sensitivity", round(sensitivity, 5))
            print("")

        return


if __name__ == '__main__':
    games = games()

    # Ask games
    games.print()
    game = int(input("From game: "))

    games.game1 = game
    h_fov, multi = games.getting_info(game)
    multi_1 = multi
    games.fov_1 = h_fov

    # Ask sensitivity
    sensitivity = float(input("Sensitivity: "))
    games.sensitivity = sensitivity
    print("")


    # Ask second game
    game = int(input("To game: "))

    games.game_2 = game
    h_fov, multi = games.getting_info(game)
    multi_2 = multi
    games.fov_2 = h_fov

    # Game multiplier
    games.multiplier = multi_2 / multi_1


    # New sensitivity calculations
    games.calculate_sensitivity()


    # Tweaks
    games.tweak()







