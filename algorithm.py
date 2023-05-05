import pygame
import random

from math import *

# set up pygame window
#                         lxwxh
def card_board_box_net_lw(dimension, ear_size=2):

    length = (2*dimension[0]) + (2*dimension[2]) + (ear_size)
    width = (2*dimension[2]) + (2*ear_size) + (dimension[1])

    errorx = ceil(length) - length
    errory = ceil(width) - width

    return ((length, width), errorx, errory)


# define rectangle class
class Rectangle:
    def __init__(self, w, h, errorx, errory, win):
        self.width = w
        self.height = h
        self.x = None
        self.y = None
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        self.win = win

        self.errorx = errorx
        self.errory = errory

    def set_position(self, x, y):
        self.x = x
        self.y = y
        if self.x != 0:
            self.x = x - self.errorx

        if self.y != 0:
            self.y = y - self.errory
    def draw(self):
        pygame.draw.rect(self.win, self.color, (self.x, self.y, self.width-self.errorx, self.height-self.errory))
        

# list of rectangles to draw
rectangles = []

# define function to find the most valuable place on canvas
def find_best_position(rect):
    min_waste = float("inf")
    best_x, best_y = None, None
    for y in range(HEIGHT - rect.height):
        for x in range(WIDTH - rect.width):
            waste = 0
            for other_rect in rectangles:
                if x < other_rect.x + other_rect.width and x + rect.width > other_rect.x and y < other_rect.y + other_rect.height and y + rect.height > other_rect.y:
                    waste += min(
                        abs(x - (other_rect.x + other_rect.width)),
                        abs(y - (other_rect.y + other_rect.height)),
                        abs((x + rect.width) - other_rect.x),
                        abs((y + rect.height) - other_rect.y)
                    )
            if waste < min_waste:
                min_waste = waste
                best_x, best_y = x, y
    return best_x, best_y

boxlist = []

run = 1
WIDTH = 800
HEIGHT = 800

def main(dimensions):
    global run, WIDTH, HEIGHT
    pygame.init()
    run = 1
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Rectangles")
    clock = pygame.time.Clock()
    # main game loop
    for ind in range(0, len(dimensions)):

        box_size = card_board_box_net_lw(dimensions[ind])
        boxlist.append((int(box_size[0][0]),int(box_size[0][1])))

    print(boxlist)
    sorted_list = sorted(boxlist, key=lambda x: (-x[0], -x[1]))
    running = True
    while running:
        clock.tick(120)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                # the list we input
        if run == 1:
            for i in sorted_list:
                # add a new rectangle
                new_rect = Rectangle(i[0], i[1], box_size[1], box_size[2], win)
                # find the best position for the new rectangle
                new_x, new_y = find_best_position(new_rect)
                new_rect.set_position(new_x, new_y)
                # draw all rectangles
                win.fill((255, 255, 255))
                for rect in rectangles:
                    rect.draw()
                # draw new rectangle
                new_rect.draw()
                # update screen
                pygame.display.update()
                # add new rectangle to list of rectangles
                rectangles.append(new_rect)

                run = 0

    pygame.quit()

main()