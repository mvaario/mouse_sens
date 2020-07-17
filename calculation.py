# Same sensitivity different games
# game multiplayers

import math

class games:

    def __init__(self):

        self.cs_fov = 106.260205
        self.cod_fov = 96.418343
        self.val_fov = 103
        self.qua_fov = 110
        self.eft_fov = 107

        # sensitivity multiply
        self.cs = 1
        self.cod = 1.333333333333
        self.valo = 3.181818181818
        self.qua = 1
        self.eft = 5.6818

        self.game_1 = 0
        self.game_2 = 0
        self.sens = 0

        self.new_sens = 0

    def print(self):
        print("")
        print("Choose games")
        print("Cs Go = 1")
        print("Cod = 2")
        print("Valorant = 3")
        print("Quake = 4")
        print("EFT = 5")
        print("Else = 6")
        print("")

        return

    def ask(self):
        try:
            game_1 = float(input("From game: "))
            game_2 = float(input("To game: "))
            sens = float(input("Sensitivity = "))
        except:
            print("Error")

        games.game_1 = game_1
        games.game_2 = game_2
        games.sens = sens
        return

    def choice(self):
        if games.game_1 == 1:
            multi_1 = games.cs
            fov_1 = games.cs_fov
        elif games.game_1 == 2:
            multi_1 = games.cod
            fov_1 = games.cod_fov
        elif games.game_1 == 3:
            multi_1 = games.valo
            fov_1 = games.val_fov
        elif games.game_1 == 4:
            multi_1 = games.qua
            fov_1 = games.qua_fov
        elif games.game_1 == 5:
            multi_1 = games.eft
            fov_1 = games.eft_fov
        else:
            multi_1 = float(input("Game multiply "))
            fov_1 = float(input("Game HFov "))

        if games.game_2 == 1:
            multi_2 = games.cs
            fov_2 = games.cs_fov
        elif games.game_2 == 2:
            multi_2 = games.cod
            fov_2 = games.cod_fov
        elif games.game_2 == 3:
            multi_2 = games.valo
            fov_2 = games.val_fov
        elif games.game_2 == 4:
            multi_2 = games.qua
            fov_2 = games.qua_fov
        elif games.game_2 == 5:
            multi_2 = games.eft
            fov_2 = games.eft_fov
        else:
            multi_2 = float(input("Game multiply "))
            fov_2 = float(input("Game HFov "))

        games.calculation(multi_1, multi_2, fov_1, fov_2)

        return

    def calculation(self, multi_1, multi_2, fov_1, fov_2):
        if games.game_1 == 5:
            fov_1 = math.degrees(math.atan((8 / (4.5 / math.tan(math.radians(fov_1 / 2)))))) * 2
        if games.game_2 == 5:
            fov_2 = math.degrees(math.atan((8 / (4.5 / math.tan(math.radians(fov_2 / 2)))))) * 2

        multi = multi_1 / multi_2

        fov_1 = math.radians(fov_1)
        fov_2 = math.radians(fov_2)
        fov_1 = math.sqrt(1 ** 2 + 1 ** 2 - 2 * 1 * 1 * math.cos(fov_1))
        fov_2 = math.sqrt(1 ** 2 + 1 ** 2 - 2 * 1 * 1 * math.cos(fov_2))
        fov = fov_2 / fov_1

        games.new_sens = fov * games.sens * multi
        print("")
        print("Fov difference", round(fov,2))
        print("Multiplier", round(multi,2))
        print("")


        return


if __name__ == '__main__':
    t = ["Cs:go", "Cod.1", "Valorant", "Quake", "EFT"]

    games = games()
    games.print()
    games.ask()
    games.choice()

    try:
        print("Sensitivity for", t[int(games.game_2-1)], ":", games.new_sens)

    except:
        print("New sensitivity = ", games.new_sens)

    # cs go sens = 1.295
    # cod1 sens  = 0.905
    # valo sens  = 0.398152
    # quake sens = 1.4018786196997421
    # EFT sens   = 0.26302