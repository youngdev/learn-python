import pygame
import pygame.camera
from pygame.locals import *
import time

pygame.init()
pygame.camera.init()

window = pygame.display.set_mode((640,480),0)
cam = pygame.camera.Camera("/dev/video0",(352,288))
cam.start()
time.sleep(5)
image = cam.get_image()
pygame.image.save(image,'abc.jpg')

cam.stop()