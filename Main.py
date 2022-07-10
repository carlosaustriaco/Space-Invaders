import pygame
import os
import time
import random

RED_SPACE_SHIP = pygame.image.load(os.path.join("Images", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("Images", "pixel_ship_green_small.png"))
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("Images", "pixel_ship_yellow.png")) 
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("Images", "pixel_ship_blue_small.png"))
RED_LASER = pygame.image.load(os.path.join("Images", "pixel_laser_red.png"))    
GREEN_LASER = pygame.image.load(os.path.join("Images", "pixel_laser_green.png"))   
BLUE_LASER = pygame.image.load(os.path.join("Images", "pixel_laser_blue.png"))   
YELLOW_LASER = pygame.image.load(os.path.join("Images", "pixel_laser_yellow.png"))
BG = pygame.image.load(os.path.join("Images", "background-black.png"))    