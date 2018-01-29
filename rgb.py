#! /usr/bin/python

import serial
import pygame

pygame.init()
DISPLAYSURF = pygame.display.set_mode((500,400),0,32)
pygame.display.set_caption('Lab1 Color Wheel')

s= serial.Serial("/dev/ttyACM0")
WHITE = (255,255,255)
DISPLAYSURF.fill(WHITE)
while(True):
  l = s.readline()
  colors = l.rstrip().split(",")
  try:
    rgb = [ int(val) for val in colors]
    DISPLAYSURF.fill(rgb[0],rgb[1],rgb[2])
    pygame.display.update()
  except ValueError:
    print("Pass")
  print rgb
 



  
  

