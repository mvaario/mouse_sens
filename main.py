# Calculating same sensitivity to different games

import math
from objects import *
from calculation import *

class main:
    # print info
    def start_info(self):
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

    # get game info
    def get_game_info(self, game):
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
                fov = int(input(f'{cal.games[game]} Field of view: '))
                fov = math.radians(fov)

            # if fov is horizontal change it to vertical
            if fov_h:
                v_fov = cal.fov_changer(fov, default_aspect)
            else:
                v_fov = fov

            # ask the aspect ratio
            used_aspect = main.get_aspect_ratio()

        except:
            print("Error")
            quit()

        return multi, v_fov, used_aspect

    # get used aspect ratio
    def get_aspect_ratio(self):
        y = int(input("Aspect ratio vertical: "))
        x = int(input("Aspect ratio horizontal: "))

        used_aspect = [x, y]
        return used_aspect

    # print results and tweaks for eft
    def results(self, new_sensitivity):
        print("")
        print(f'Sensitivity for {cal.games[cal.game_2]}: {round(new_sensitivity, 5)} ')

        print("")
        fov_1 = round(math.degrees(cal.fov_1), 3)
        fov_2 = round(math.degrees(cal.fov_2), 3)

        print(f'Actual horizontal FOV in {cal.games[cal.game_1]}: {round(fov_1, 2)} degree')
        print(f'Actual horizontal FOV in {cal.games[cal.game_2]}: {round(fov_2, 2)} degree')
        return

    # tweaks for specific games
    def tweaks(self):
        if cal.game_1 == 4 or cal.game_2 == 4:
            print("EFT changes turning speed")
            # around -15% (probably)
            if cal.game_1 == 4:
                sensitivity = cal.new_sensitivity * 1.15
            else:
                sensitivity = cal.new_sensitivity * 0.85

            print("Recommended sensitivity", round(sensitivity, 5))
            print("")

        return

if __name__ == '__main__':
    main = main()
    cal = calculations()

    # print info
    main.start_info()

    # ask the game
    game = int(input("From a game: "))
    # get game info
    multi, v_fov, used_aspect = main.get_game_info(game)
    # calculate actual horizontal fov
    h_fov = cal.aspect_ratio_calculation(v_fov, used_aspect)
    # save game info
    cal.multi_1 = multi
    cal.game_1 = game
    cal.fov_1 = h_fov
    cal.used_aspect_1 = used_aspect

    # get sensitivity
    sensitivity = float(input("Game sensitivity: "))
    cal.sensitivity = sensitivity
    print("")

    # ask the game
    game = int(input("To a game: "))
    # get game info
    multi, v_fov, used_aspect = main.get_game_info(game)
    # calculate actual horizontal fov
    h_fov = cal.aspect_ratio_calculation(v_fov, used_aspect)
    # save game info
    cal.multi_2 = multi
    cal.game_2 = game
    cal.fov_2 = h_fov
    cal.used_aspect_2 = used_aspect

    # calculate fov difference
    difference = cal.fov_difference()

    # New sensitivity calculations
    new_sensitivity = cal.calculate_sensitivity(difference)

    main.results(new_sensitivity)

    # Tweaks
    main.tweaks()

