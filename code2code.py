#!/usr/bin/python
import subprocess
from gpiozero import Button

bpres = Button("BOARD31")

check = 1 
while (check == 1):
    if(bpres.is_pressed):
      try:
        subprocess.call(["python,"Testcode.py])
        raise SystemExit()
      
      except KeyboardInterrupt:
        print("Quit")
      check = 0
