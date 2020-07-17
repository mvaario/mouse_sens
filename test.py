from pynput.mouse import Button, Controller
import time
import pygame


class main():

    def __init__(self):
        self.count = 1974
        self.sleep = 0.005
        self.width = 1920
        self.height = 1080


    def start(self):
        # mouse.position = (main.width / 2, main.height / 2)
        mouse.position = (959, 539)
        return

    def time(self):
        countsec = 3
        for i in range(countsec):
            print(countsec)
            time.sleep(1)
            countsec -= 1
        return


    def move(self):
        for i in range(main.count):
            mouse.move(1, 0)
            clock.tick(120)
        return

    def move_back(self):
        for i in range(main.count):
            mouse.move(-1, 0)
            clock.tick(1000)
        return


if __name__ == '__main__':
    main = main()
    mouse = Controller()
    clock = pygame.time.Clock()

    main.start()
    main.time()
    main.start()
    print("Start pos = ", mouse.position)
    main.move()
    print("Mid point pos = ", mouse.position)
    main.time()
    main.move_back()
    print("End pos = ", mouse.position)