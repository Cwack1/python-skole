#Rock Paper Scissors
import pygame as game
import sys
import random

def addImage(display, image_location, height, width):
    img1 = game.image.load(image_location)
    display.blit(game.transform.scale(img1, (height, width)), (200, 100))
    game.display.flip()
    #game.time.wait(5000)

def ImageRoulette():
    img_arr = ["rock.jpg", "scissor.jpg", "paper.jpg"]
    img_loc = "C:\\Users\\t92\\Documents\\Vscode\\python-skole\\Nivå 2\\Rock_Paper_Scissor\\"
    for i in range(3):
        addImage(display, img_loc + img_arr[i], 400, 400)
        game.time.wait(200)

def run():
    running = True

    while running: 
        for event in game.event.get():
            if event.type == game.QUIT:
                running = False

        game.display.flip()


game.init()
display = game.display.set_mode((800, 600))
game.display.set_caption("Stein, Saks, Papir!")


for i in range(5):
    ImageRoulette() 

#Create the random image
img_arr = ["rock.jpg", "scissor.jpg", "paper.jpg"]
img_loc = "C:\\Users\\t92\\Documents\\Vscode\\python-skole\\Nivå 2\\Rock_Paper_Scissor\\"
addImage(display, img_loc + img_arr[random.randint(0,3)], 400, 400)
#game.display.flip()
run()