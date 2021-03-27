# Same sensitivity different games
# game multiplayers

import math


class games:

    def __init__(self):

        self.cs_fov = 106.260205
        self.cod_fov = 90
        self.val_fov = 103
        self.qua_fov = 106
        self.r6_fov = 74

        # sensitivity multiply
        self.cs = 1
        self.cod = 1
        self.valo = 0.314285714
        self.qua = 1
        self.eft = 0.1760000
        self.r6 = 3.8397238

        self.game_1 = 0
        self.game_2 = 0
        self.sens = 0

        self.new_sens = 0
        self.new = 0

        # eft changes (turning speed is not static)
        self.eft_diff = 15

    def print(self):
        print("")
        print("Choose games")
        print("Cs Go = 1")
        print("Cod = 2")
        print("Valorant = 3")
        print("Quake = 4")
        print("EFT = 5")
        print("R6 = 6")
        print("Else = 7")
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
            fov_1 = float(input("EFT fov: "))
        elif games.game_1 == 6:
            multi_1 = games.r6
            fov_1 = games.r6_fov
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
            fov_2 = float(input("EFT fov: "))
        elif games.game_2 == 6:
            multi_2 = games.r6
            fov_2 = games.r6_fov


        else:
            multi_2 = float(input("Game multiply "))
            fov_2 = float(input("Game HFov "))

        games.calculation(multi_1, multi_2, fov_1, fov_2)

        return

    def calculation(self, multi_1, multi_2, fov_1, fov_2):
        if games.game_1 == 5:
            fov_1 = math.degrees(math.atan((8 / (4.5 / math.tan(math.radians(fov_1 / 2)))))) * 2
            print("Escape from Tarkov Hfov", round(fov_1, 4))

        if games.game_2 == 5:
            fov_2 = math.degrees(math.atan((8 / (4.5 / math.tan(math.radians(fov_2 / 2)))))) * 2
            print("Escape from Tarkov Hfov", round(fov_2, 4))

        multi = multi_2 / multi_1

        f_1 = math.radians(fov_1)
        f_2 = math.radians(fov_2)

        f_1 = f_1 / 2
        f_2 = f_2 / 2

        c1 = math.tan(f_1)
        c2 = math.tan(f_2)

        c = c2 / c1

        games.new_sens = c * games.sens * multi

        if games.game_1 == 5 or games.game_2 == 5:
            diff = games.eft_diff

            diff = 1 + (diff / 100)

            if games.game_1 == 5:
                games.new = games.new_sens / (diff)
            if games.game_2 == 5:
                games.new = games.new_sens * (diff)

        print("")
        print("Fov difference", round(c, 5))
        print("Multiplier", round(multi, 5))
        print("")

        return


if __name__ == '__main__':
    t = ["Cs:go", "Cod.1", "Valorant", "Quake", "EFT", "R6"]
    x = 0.905184
    x = x * 600
    x = x / 400
    print(x)

    games = games()
    games.print()

    games.ask()
    games.choice()

    try:
        print("Sensitivity for", t[int(games.game_2 - 1)], ":", round(games.new_sens, 5))

    except:
        print("New sensitivity = ", round(games.new_sens, 5))

    if games.new != 0:
        print("")
        print("Recommended tweaks +", games.eft_diff, "%")
        print("Recommended sensitivty = ", round(games.new, 5))

    print("")
    input("Press enter to close")

    # cod    = 1.357776
    # cs go  = 1.81037
    # quake  = 1.80183
    # eft    = 0.33578
