#!/usr/bin/python2
# small script to take keyboard inputs to control a remote helicopter.

import pygame
from pygame.locals import *
from sys import exit
import serial
from time import sleep

# define Serial terminal properties here.
_port_name='/dev/ttyUSB0'
_baud_rate=115200

# The code sents data on each key press.
# define data
_up_data='up'
_down_data='down'
_left_data='left'
_right_data='right'
 
# Time between two keypress, in seconds.
_sleep_time=0.2


class helicopter:
    _max_bound=100
    _t_delay=.001
    
    
    _cur_position = 'down'
    def __init__(self, _port_name, _baud_rate):
        #rotor_speed = self._rotor_speed
        self._x_axis = 50
        self._y_axis = 50
        self._rotor_speed = 0

#port = serial.Serial(_port_name, _baud_rate, timeout=0)
    def takeoff(self):
        while self._rotor_speed < self._max_bound:
            self._rotor_speed += 1
            #self.port.write(_up_data)
            sleep(self._t_delay)
            print self._rotor_speed

    def land(self):
        while _rotor_speed < _min_bound:
            _rotot_speed -=1
            #self.port.write(_down_data)
            sleep(_t_delay*2)
            print _rotor_speed

    def adjustx(self,direction):
        if direction == 'up':
            self._x_axis += 1
            
        if direction == 'down':
            self._x_axis -= 1
        print "X axis Change:", self._x_axis
            
            
    def adjusty(self,direction):
        if direction == 'up':
            self._y_axis += 1
           
        if direction == 'down':
            self._y_axis -= 1
        
        print "Y axis change:", self._y_axis

    def adjustrot(self,direction):
        if direction == 'up':
            self._rotor_speed += 1
           
        if direction == 'down':
            self._rotor_speed -= 1
            
        print "Rotor Speed:", self._rotor_speed
            
#program begins

copter = helicopter(_port_name, _baud_rate)
pygame.init()
screen = pygame.display.set_mode((100, 100), 0, 32)
font = pygame.font.SysFont("arial", 10);
font_height = font.get_linesize()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        screen.fill((255, 255, 255))

        pressed_key_text = []
#        sleep(_sleep_time)
        pressed_keys = pygame.key.get_pressed()
        y = font_height
        
        for key_constant, pressed in enumerate(pressed_keys):
            if pressed:
                key_name = pygame.key.name(key_constant)
                text_surface = font.render(key_name, True, (0,0,0))
                screen.blit(text_surface, (8, y))
                
                
                if key_name == 't':
                    copter.takeoff()

                if key_name == 'l':
                    copter.land()
                
                if key_name == 'right':
                    #port.write(_right_data)
                    copter.adjustx('up')
                    
                if key_name == 'left':
                    #port.write(_left_data)
                    copter.adjustx('down')

                if key_name == 'up':
                    #port.write(_left_data)
                    copter.adjusty('up')
                
                if key_name == 'down':
                    #port.write(_left_data)
                    copter.adjusty('down')
                
                if key_name == 'z':
                    #port.write(_left_data)
                    copter.adjustrot('up')

                if key_name == 'x':
                    #port.write(_left_data)
                    copter.adjustrot('down')

                y+= font_height
        pygame.display.update()
