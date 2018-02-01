#! /usr/bin/python

import serial
import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,400),0,32)
pygame.display.set_caption('Lab1 Color Wheel')

s = serial.Serial("/dev/ttyACM0")
WHITE = (255,255,255)
DISPLAYSURF.fill(WHITE) 
pygame.display.update()
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  l = s.readline()
  colors = l.rstrip().split(",")

  try:
    try:
      Color_G = int(colors[0])
      Color_B = int(colors[1])
      Color_R = int(colors[2])
      DISPLAYSURF.fill((Color_R,Color_G, Color_B))
      pygame.display.update()
    except IndexError:
	print('IndexPass')

  except ValueError:
    print("ValuePass")
  
   
    
 



  
  

