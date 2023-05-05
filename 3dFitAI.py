import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
import random

# Define the dimensions of the limited 3D space
space_width = 800
space_height = 600
space_depth = 400

# Define the dimensions of the rectangle prism
rect_width = 50
rect_height = 50
rect_depth = 50

# Define the number of possible positions to consider
num_positions = 100

# Generate all possible positions for the rectangle prism
positions = []
for i in range(num_positions):
    x = random.randint(0, space_width - rect_width)
    y = random.randint(0, space_height - rect_height)
    z = random.randint(0, space_depth - rect_depth)
    positions.append((x, y, z))

# Evaluate each position to find the best one
best_position = None
best_score = 0
for position in positions:
    score = 0
    for other_position in positions:
        if other_position != position:
            dx = abs(position[0] - other_position[0])
            dy = abs(position[1] - other_position[1])
            dz = abs(position[2] - other_position[2])
            if dx < rect_width and dy < rect_height and dz < rect_depth:
                score += 1
    if score > best_score:
        best_position = position
        best_score = score

# Initialize Pygame and OpenGL
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)

gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(-space_width/2, -space_height/2, -space_depth/2)

# Draw the rectangle prism in the best position
rect_color = (1.0, 0.0, 0.0)
rect_x, rect_y, rect_z = best_position
glPushMatrix()
glTranslatef(rect_x, rect_y, rect_z)
glBegin(GL_QUADS)
glColor3f(*rect_color)
glVertex3f(0, 0, 0)
glVertex3f(rect_width, 0, 0)
glVertex3f(rect_width, rect_height, 0)
glVertex3f(0, rect_height, 0)
glVertex3f(0, 0, rect_depth)
glVertex3f(rect_width, 0, rect_depth)
glVertex3f(rect_width, rect_height, rect_depth)
glVertex3f(0, rect_height, rect_depth)
glVertex3f(0, 0, 0)
glVertex3f(0, rect_height, 0)
glVertex3f(0, rect_height, rect_depth)
glVertex3f(0, 0, rect_depth)
glVertex3f(rect_width, 0, 0)
glVertex3f(rect_width, rect_height, 0)
glVertex3f(rect_width, rect_height, rect_depth)
glVertex3f(rect_width, 0, rect_depth)
glVertex3f(0, 0, 0)
glVertex3f(0, 0, rect_depth)
glVertex3f(rect_width, 0, rect_depth)
glVertex3f(rect_width, 0, 0)
glEnd()
glPopMatrix() 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Draw the rectangle prism in the best position
    glPushMatrix()
    glTranslatef(rect_x, rect_y, rect_z)
    glBegin(GL_QUADS)
    glColor3f(*rect_color)
    glVertex3f(0, 0, 0)
    glVertex3f(rect_width, 0, 0)
    glVertex3f(rect_width, rect_height, 0)
    glVertex3f(0, rect_height, 0)
    glVertex3f(0, 0, rect_depth)
    glVertex3f(rect_width, 0, rect_depth)
    glVertex3f(rect_width, rect_height, rect_depth)
    glVertex3f(0, rect_height, rect_depth)
    glVertex3f(0, 0, 0)
    glVertex3f(0, rect_height, 0)
    glVertex3f(0, rect_height, rect_depth)
    glVertex3f(0, 0, rect_depth)
    glVertex3f(rect_width, 0, 0)
    glVertex3f(rect_width, rect_height, 0)
    glVertex3f(rect_width, rect_height, rect_depth)
    glVertex3f(rect_width, 0, rect_depth)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, rect_depth)
    glVertex3f(rect_width, 0, rect_depth)
    glVertex3f(rect_width, 0, 0)
    glVertex3f(rect_width, rect_height, 0)
    glVertex3f(0, rect_height, 0)
    glVertex3f(0, rect_height, rect_depth)
    glVertex3f(rect_width, rect_height, rect_depth)
    glVertex3f(rect_width, 0, rect_depth)
    glEnd()
    glPopMatrix()

    pygame.display.flip()
    pygame.time.wait(10)
