import RPi.GPIO as GPIO
import pygame

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP) # X axis
GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Y axis
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button 1

# Initialize pygame
pygame.init()

# Set up the joystick
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Main loop
while True:
  # Read the joystick's X and Y axis values
  x_axis = GPIO.input(10)
  y_axis = GPIO.input(9)

  # Read the joystick's button 1 value
  button_1 = GPIO.input(11)

  # Perform actions based on the joystick's input
  if x_axis == False:
    print("X axis moved left")
  elif x_axis == True:
    print("X axis moved right")

  if y_axis == False:
    print("Y axis moved up")
  elif y_axis == True:
    print("Y axis moved down")

  if button_1 == False:
    print("Button 1 pressed")
  elif button_1 == True:
    print("Button 1 released")

# Clean up
pygame.joystick.quit()
GPIO.cleanup()
