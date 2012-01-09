#!/usr/bin/python2
# small script to take keyboard inputs to control a remote helicopter.

import pygame
from pygame.locals import *
from sys import exit
import serial

# define Serial terminal properties here.
_port_name='/dev/ttyS'
_baud_rate=115200

# The code sents data on each key press.
# define data
_up_data='up'
_down_data='down'
_left_data='left'
_right_data='right'
 
# Time between two keypress, in seconds.
_sleep_time=0.2

#program begins
port = serial.Serial(_port_name, _baud_rate, timeout=0)

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
font = pygame.font.SysFont("arial", 32);
font_height = font.get_linesize()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        screen.fill((255, 255, 255))

        pressed_key_text = []
        sleep(_sleep_time)
        pressed_keys = pygame.key.get_pressed()
        y = font_height
        
        for key_constant, pressed in enumerate(pressed_keys):
            if pressed:
                key_name = pygame.key.name(key_constant)
                text_surface = font.render(key_name+" pressed", True, (0,0,0))
                screen.blit(text_surface, (8, y))
                
                
                if key_name == 'up':
                    port.write(_up_data)

                if key_name == 'down':
                    port.write(_down_data)
                
                if key_name == 'right':
                    port.write(_right_data)
                    
                if key_name == 'left':
                    port.write(_left_data)
                    
                
                
                y+= font_height
        pygame.display.update()
