import pygame
import pyautogui
import sys
import socket
import threading

pygame.init()

ScreenWidth = 640
ScreenHeight = 480
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))

pygame.display.set_caption("Gamma")

clock = pygame.time.Clock() 
 
running = True 

while running:

    DeltaTime = clock.tick(30)

    for event in pygame.event.get(): 
        
        if event.type == pygame.QUIT: 
            running = False

    pygame.display.update()


pygame.quit()