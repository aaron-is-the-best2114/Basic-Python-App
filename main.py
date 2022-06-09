#aaron-is-the-best2114, all rights to ownership go to aaron-is-the-best2114, Please give credit
#Github - https://github.com/aaron-is-the-best2114
#Youtube - https://www.youtube.com/channel/UCaUj-xomNl5Ia3atXvmIAHg

#Import the pygame index
import pygame
#other imports
import sys
from pygame.locals import *
#Initilizes the use of the pygame index
pygame.init()
#Variable, Difine a color
YELLOW = (255,255,0)
#Give a desired font
myFont = pygame.font.SysFont("monospace", 35)
#Build the GUI for pygame interface, also makes the window resizable
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
screen = pygame.display.set_mode((800, 500), pygame.RESIZABLE)
#sets False value to fullscreen
fullscreen = False
#Update the GUI to display the text or items wanted to be displayed
pygame.display.update()
run = True
while run:
    #screen background color
    screen.fill((0, 0, 255))
    #text to display on the GUI
    text = "testing: "
    #To render the text on the UI
    lable = myFont.render(text, 1, YELLOW)
    #positioning the text and allowing it to render
    screen.blit(lable, (screen.get_width() - 75 - (screen.get_width() / 5), screen.get_height() - 5 - (screen.get_height() /5)))
    #Make action buttons work: Exit, minimize, maximize, etc.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #adjusts background color according to window size
        if event.type == VIDEORESIZE:
            if not fullscreen:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
    pygame.display.update()

pygame.display.update()

pygame.quit()
