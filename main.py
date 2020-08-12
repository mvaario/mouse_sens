# mouse sens to different games

import pygame
import win32api, win32con
import time
from getkeys import key_check

class main():

    def __init__(self):
        self.count = 1815
        # 2005
        self.x = 959
        self.y = 540
        self.countsec = 3

        self.setup = True
        self.running = False

    def start(self):
        win32api.SetCursorPos((main.x, main.y))
        count = main.count
        while count > 0:
            main.count_left()
            count -= 1
            clock.tick(60)
        return



    def count_left(self):
        x, y = win32api.GetCursorPos()
        win32api.SetCursorPos((x-1, y))
        return

    # def count_right(self):
    #     x, y = win32api.GetCursorPos()
    #     win32api.SetCursorPos((x-1, y))
    #     return

    def countdown(self):
        print("")
        print("Left")
        main.countsec = 3
        for i in range(main.countsec):
            print(main.countsec)
            time.sleep(1)
            main.countsec -= 1

        return

    def restart(self):
        print("Done, ticks: ", main.count)
        print("a/d to change counts, w to start, s to quit")
        setup = True
        while setup == True:
            if '1' in key_check():
                # main.count -= 1
                time.sleep(0.2)
                print(self.count)
            elif '3' in key_check():
                # main.count += 1
                time.sleep(0.2)
                print(main.count)
            elif 'F' in key_check():
                self.running = True
                setup = False
            elif '2' in key_check():
                self.running = False
                setup = False
            clock.tick(60)

if __name__ == '__main__':
    check_key = key_check()
    pygame.init()
    main = main()
    clock = pygame.time.Clock()
    print("Counts", main.count)
    while not main.running:
        if 'F' in key_check():
            main.running = True
    while main.running:
        main.countdown()
        main.start()
        main.restart()
