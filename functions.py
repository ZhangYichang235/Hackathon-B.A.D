import pygame
import random
from math import *

def cardboard_box_frigile(length_box, width_box, height, ear_size):
    length_box += 5
    height += 5
    width_box += 5
    # Find the dimensions of the cardboard box
    length = length_box + height + length_box + height + ear_size
    width = (2*height) + width_box + (2*ear_size)
    
    errorx = ceil(length) - length
    errory = ceil(width) - width
    
    # Print the dimensions of the cardboard box
    return (ceil(length), ceil(width)), errorx, errory

def cardboard_box_normal(length_box, width_box, height, ear_size):
    # Find the dimensions of the cardboard box
    length = length_box + height + length_box + height + ear_size
    width = (2*height) + width_box + (2*ear_size)

    errorx = ceil(length) - length
    errory = ceil(width) - width
    
    # Print the dimensions of the cardboard box
    return (ceil(length), ceil(width)), errorx, errory

print(cardboard_box_normal(length_box=13, width_box=6, height=1, ear_size=2))

# set up pygame window
pygame.init()
WIDTH = 800
HEIGHT = 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rectangles")

# define rectangle class
class Rectangle:
    def __init__(self, l, w, errorx, errory):
        self.width = l
        self.height = w
        self.x = None
        self.y = None
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

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
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width - self.errorx, self.height - self.errory))
        

# list of rectangles to draw
rectangles = []


rects = []

y = 0
x = 0

# define function to find the most valuable place on canvas
def find_best_position(rect):

    global y, x

    min_waste = float("inf")
    best_x, best_y = None, None
    for y in range(0, (HEIGHT - rect.height), 1):
    # while y < (HEIGHT - rect.height):
        for x in range(0, (WIDTH - rect.width), 1):
        # while x < (WIDTH - rect.width):
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

        #     x += 1
        # y += 1
    return best_x, best_y

# main game loop
while True:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
    # add a new rectangle with random dimensions
    new_rect = Rectangle()
    
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
    
    # wait for a short time to slow down the loop
    pygame.time.wait(100)
