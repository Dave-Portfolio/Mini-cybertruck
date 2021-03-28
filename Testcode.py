import pygame, sys, time    #Imports Modules
from pygame.locals import *
from gpiozero import Robot, PWMLED



pygame.init()#Initializes Pygame
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

#Initializes Joystick
#hello
robot = Robot(left=("BOARD18","BOARD16"), right=("BOARD11","BOARD13")) #initializes robot

axis0 = joystick.get_axis(0)
axis1 = joystick.get_axis(1)
               
rightpwm = PWMLED("BOARD12")
leftpwm = PWMLED("BOARD33")
     


while True:
    pygame.event.get()
    axis0 = joystick.get_axis(0)
    axis1 = joystick.get_axis(1)
    axis2 = joystick.get_axis(2)
    axis3 = joystick.get_axis(3)
    if (0.65<axis0):
        robot.backward()
        rightpwm.value = 1
        leftpwm.value = 1
    elif(-0.65>axis0):
        robot.forward()
        rightpwm.value = 1
        leftpwm.value = 1
    elif (0.65<axis1):
        robot.right()
        rightpwm.value = 1
        leftpwm.value = 1
    elif(-0.65>axis1):
        robot.left()
        rightpwm.value = 1
        leftpwm.value = 1
    else:
        robot.stop()
        rightpwm.value = 0
        leftpwm.value = 0
    print(axis1)
    
    
    
        
    


