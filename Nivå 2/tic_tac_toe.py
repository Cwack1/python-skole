#Tic Tac Toe
import pygame as game
game.init()

game.display.set_mode((800, 600))

running = True

while running: 
    for event in game.event.get():
        if event.type == game.QUIT:
            running = False