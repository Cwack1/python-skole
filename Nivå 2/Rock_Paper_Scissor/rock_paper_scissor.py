#Rock Paper Scissors
import pygame as game
import sys

game.init()

display = game.display.set_mode((800, 600))

img1 = game.image.load("C:\\Users\\t92\\Documents\\Vscode\\python-skole\\Nivå 2\\Rock_Paper_Scissor\\rock2.jpg")

display.blit(game.transform.scale(img1, (400, 400)), (10, 10))

game.display.flip()
game.time.wait(5000)

game.display.set_caption("Stein, Saks, Papir!")

running = True

while running: 
    for event in game.event.get():
        if event.type == game.QUIT:
            running = False

    game.display.flip()