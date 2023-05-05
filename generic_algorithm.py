import pygame
import random

from math import *

def card_board_box_net_lw(dimension, ear_size=2):
    length = (2 * dimension[0]) + (2 * dimension[2]) + (ear_size)
    width = (2 * dimension[2]) + (2 * ear_size) + (dimension[1])
    errorx = ceil(length) - length
    errory = ceil(width) - width
    return ((length, width), errorx, errory)

def create_rectangles(dimensions):
    rectangles = []
    for dimension in dimensions:
        box_size = card_board_box_net_lw(dimension)
        rectangles.append(pygame.Rect(0, 0, box_size[0][0] - box_size[1], box_size[0][1] - box_size[2]))
    return rectangles

def find_best_position(rect, rectangles):
    min_waste = float("inf")
    best_x, best_y = None, None
    for y in range(canvas_rect.height - rect.height):
        for x in range(canvas_rect.width - rect.width):
            waste = 0
            for other_rect in rectangles:
                if rect.colliderect(other_rect):
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

def draw_rectangles(rectangles, canvas):
    canvas.fill((255, 255, 255))
    for rect in rectangles:
        pygame.draw.rect(canvas, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), rect)
    pygame.display.update()

def main(dimensions):
    pygame.init()
    clock = pygame.time.Clock()
    canvas = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Rectangles")

    global canvas_rect
    canvas_rect = canvas.get_rect()

    rectangles = create_rectangles(dimensions)
    sorted_rectangles = sorted(rectangles, key=lambda x: (-x.width, -x.height))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        for rect in sorted_rectangles:
            best_x, best_y = find_best_position(rect, rectangles)
            rect.x = best_x
            rect.y = best_y
            draw_rectangles(rectangles, canvas)
            clock.tick(60)


dimensions = [(100, 200, 50), (50, 150, 100), (200, 100, 75), (150, 50, 25)]
main(dimensions)
