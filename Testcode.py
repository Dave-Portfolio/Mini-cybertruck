import pygame, sys    #Imports Modules
from pygame.locals import *
from gpiozero import Robot, PWMLED
import RPi.GPIO as GPIO
from picamera import PiCamera
from datetime import datetime
import time

servoPINx = 25
servoPINy = 8
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPINx, GPIO.OUT)
GPIO.setup(servoPINy, GPIO.OUT)
GPIO.setwarnings(False)
time.sleep(1)
p = GPIO.PWM(servoPINx, 50) # GPIO 17 for PWM with 50Hz
q = GPIO.PWM(servoPINy, 50)
x = 7.5
y = 7.5
p.start(x) #start of gpio pwm
q.start(y) #start of gpio pwm

p.ChangeDutyCycle(0)
q.ChangeDutyCycle(0)

camera = PiCamera() #start camera
#camera.start_preview(alpha=200) #show camera view



pygame.init()#Initializes Pygame
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

#Initializes Joystick
#hello
rightside = Robot(left=("BOARD16","BOARD18"), right=("BOARD13","BOARD11")) #initializes robot
leftside = Robot(left=("BOARD38","BOARD37"), right=("BOARD36","BOARD40")) #initializes robot


               
rightpwm = PWMLED("BOARD12")
leftpwm = PWMLED("BOARD33")
right2pwm = PWMLED("BOARD32")
left2pwm = PWMLED("BOARD35")


     
def forward():
    rightside.left()
    leftside.right()
        
    
def backward():
    rightside.right()
    leftside.left()
    
def left():
    rightside.right()
    leftside.right()
    
def right():
    rightside.left()
    leftside.left()
def stop():
    rightside.stop()
    leftside.stop()

while True:
    GPIO.setup(servoPINx, GPIO.IN)
    GPIO.setup(servoPINy, GPIO.IN)
    
    
    
    pygame.event.get()
    axis0 = joystick.get_axis(0) #up and down for left stick
    axis1 = joystick.get_axis(1) #left and right for left stick)
    axis2 = joystick.get_axis(2) #L2
    axis3 = joystick.get_axis(3) #left and right for right stick
    axis4 = joystick.get_axis(4) #up and down for right stick
    axis5 = joystick.get_axis(5) #R2
    r1 = joystick.get_button(5)
    if (0.38<axis0 and 0.38>abs(axis1)):
        left()
        rightpwm.value = abs(axis0)
        leftpwm.value =abs(axis0) 
        right2pwm.value = abs(axis0)
        left2pwm.value = abs(axis0)
    elif(-0.38>axis0 and 0.38>abs(axis1)):
        right()
        rightpwm.value = abs(axis0)
        leftpwm.value =abs(axis0) 
        right2pwm.value = abs(axis0)
        left2pwm.value = abs(axis0)
    elif (0.38<axis1 and 0.38>abs(axis0)):
        backward()
        rightpwm.value = abs(axis1)
        leftpwm.value =abs(axis1) 
        right2pwm.value = abs(axis1)
        left2pwm.value = abs(axis1)
    elif(-0.38>axis1 and 0.38>abs(axis0)):
        forward()
        rightpwm.value = abs(axis1)
        leftpwm.value =abs(axis1) 
        right2pwm.value = abs(axis1)
        left2pwm.value = abs(axis1)
        
    
    
    else:
        stop()
        rightpwm.value = 0
        leftpwm.value = 0
        right2pwm.value = 0
        left2pwm.value = 0
    #print(axis4)
    
    
    
    if(-0.15>axis3 and 0.15>abs(axis4)):
        GPIO.setup(servoPINx, GPIO.OUT)
        p.ChangeDutyCycle(x)
        time.sleep(0.05)
        if (x<12.5):
            x += 0.1
            
        
        
    
    
        
    elif (0.15<axis3 and 0.15>abs(axis4)):
        GPIO.setup(servoPINx, GPIO.OUT)
        p.ChangeDutyCycle(x)
        time.sleep(0.05)
        if (x>2.5):
            x -= 0.1
        
        
    else:
        GPIO.setup(servoPINx, GPIO.IN)
                   
            
    if(-0.15>axis4 and 0.15>abs(axis3)):
        GPIO.setup(servoPINy, GPIO.OUT)
        q.ChangeDutyCycle(y)
        time.sleep(0.05)
        if (y<12.5):
            y += 0.1
        
        
    
    
        
    elif (0.15<axis4 and 0.15>abs(axis3)):
        GPIO.setup(servoPINy, GPIO.OUT)
        q.ChangeDutyCycle(y)
        time.sleep(0.05)
        if (y>2.5):
            y -= 0.1
        
     
    else:
        GPIO.setup(servoPINy, GPIO.IN)
    
    
    if(r1==1):
        timestamp = datetime.now().isoformat()
        camera.capture('/home/pi/Desktop/%s.jpg' % timestamp)


