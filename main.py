# mouse sens to different games

import pygame
import win32api, win32con
import time


class main():

    def __init__(self):
        self.count = 1975
        # 1975
        self.x = 959
        self.y = 539
        self.countsec = 3
        self.sleep = 3

    def counts(self):
        win32api.SetCursorPos((959+1, main.y))

        return

    def counts_back(self, i):
        # win32api.SetCursorPos((959-1, main.y))
        win32api.SetCursorPos((959 - i, main.y))

        return


    def countdown(self):

        print("")
        print("Back")
        main.countsec = 3
        for i in range(main.countsec):
            win32api.SetCursorPos((main.x, main.y))
            print(main.countsec)
            time.sleep(1)
            main.countsec -= 1



        return

if __name__ == '__main__':
    pygame.init()
    main = main()
    clock = pygame.time.Clock()
    print("Counts", main.count)

    main.countdown()

    # i = 0
    # while i < main.count:
    #
    #     main.counts()
    #     i += 1
    #     clock.tick(30)
    #
    # main.countdown()


    i = 0
    while i < main.count:
        main.counts_back(i)
        i += 1
        clock.tick(175)
