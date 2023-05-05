import pygame
import tkinter as tk

# function to open Pygame window
def open_window():
    pygame.init()
    clock = pygame.time.Clock()
    canvas = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Pygame Window")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        canvas.fill((255, 255, 255))
        pygame.draw.circle(canvas, (255, 0, 0), (400, 300), 50)
        pygame.display.update()

        clock.tick(60)

    pygame.quit()

# create Tkinter window and button
root = tk.Tk()
root.title("Main Window")
button = tk.Button(root, text="Open Pygame Window", command=open_window)
button.pack()

root.mainloop()
