# import the pygame module, so you can use it
import pygame
from time import sleep
import random
import os
import math
from multiprocessing import Process

os.system('clear')


display_width = 1280
display_height = 720
global island
island = 0
global mx
global my
mx = 0
my = 0
buttonsDict = {}





# initialize the pygame module
pygame.init()

running = True

# load and set the logo
logo = pygame.image.load("logo.png")
pygame.display.set_icon(logo)
pygame.display.set_caption("RPG - Sam McKid")


### SREEN AND CLOCK ###
screen = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()

    #VARIABLE RESET
    ButtonLocationPrintHolder = "holder"
    Bank_account += Bank_account*(0.0001388888889) #Equals 5% per 0.6 seconds or something like that
    Bank_account = round(Bank_account, 2)  #round it so it looks nice
    #print(pygame.mixer.music.get_pos())
    if pygame.mixer.music.get_pos() >= 6000:
        pygame.mixer.music.play()
    # updates the display
    pygame.display.update()
    # clock.tick(framespersecond)
    clock.tick(60)



pygame.quit()
