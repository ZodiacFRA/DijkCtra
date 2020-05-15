import sys
import time

import pygame
from pygame.locals import *

from config import *


class pyGameHandler(object):
    def __init__(s, window_dimensions, grid_width, grid_height, max_fps):
        s.grid_width = grid_width
        s.grid_height = grid_height
        s.icons = {}
        # FPS handling
        s.last_frame_time = time.time()
        FPS = MAX_FPS
        s.min_frame_time = 1 / FPS

        pygame.init()
        s.width, s.height = window_dimensions[0], window_dimensions[1]
        s.display = pygame.display.set_mode(window_dimensions)
        s.init_from_map()

    def prepare_display(s, bg_color):
        # Update window size if needed
        w, h = pygame.display.get_surface().get_size()
        if w != s.width or h != s.height:
            s.width = w
            s.height = h
            init_from_map()
        # Update display
        s.display.fill(bg_color)

    def update_display(s):
        pygame.display.update()
        # Wait if needed to respect fps capping
        wait_time = s.min_frame_time - (s.last_frame_time - time.time())
        if wait_time > 0:
            time.sleep(wait_time)
        s.last_frame_time = time.time()

        # Handle inputs for next turn
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return s.handle_input()

    def handle_input(s):
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            return 0
        elif keys[K_RIGHT]:
            return 1
        elif keys[K_DOWN]:
            return 2
        elif keys[K_LEFT]:
            return 3

    # Drawing functions
    def draw(s, icon_name, pos):
        s.display.blit(s.icons[icon_name], s.get_pixel_pos(pos))

    def draw_grid(s, fg_color):
        for y in range(s.base_y, s.height - s.base_y + 1, s.grid_y_inc):
            pygame.draw.line(s.display, fg_color, (s.base_y, y), ((s.width - s.base_x), y), 2)
        for x in range(s.base_x, s.width - s.base_x + 1, s.grid_x_inc):
            pygame.draw.line(s.display, fg_color, (x, s.base_x), (x, (s.height - s.base_y)), 2)

    # Init functions
    def init_from_map(s):
        """Requires the s.map ref to be up-to-date with Core's one!"""
        s.base_y = int(s.height - 0.9 * s.height)
        s.base_x = int(s.width - 0.9 * s.width)
        s.grid_y_inc = int((s.height - 2 * s.base_y) // (s.grid_height))
        s.grid_x_inc = int((s.width - 2 * s.base_x) // (s.grid_width))
        s.init_icons()

    def init_icons(s):
        """Load icons to the correct square size"""
        s.icons["Player"] = pygame.transform.scale(pygame.image.load("./rsc/icons/pacman.png"), (s.grid_x_inc, s.grid_y_inc))
        s.icons["Enemy"] = pygame.transform.scale(pygame.image.load("./rsc/icons/ghostV2.png"), (s.grid_x_inc, s.grid_y_inc))
        s.icons["Wall"] = pygame.transform.scale(pygame.image.load("./rsc/icons/wall.png"), (s.grid_x_inc, s.grid_y_inc))
        s.icons["Bonus"] = pygame.transform.scale(pygame.image.load("./rsc/icons/bonus.png"), (s.grid_x_inc, s.grid_y_inc))
        # Create color icons
        for i in range(0, 10):
            tmp = "Icon" + str(i)
            s.icons[tmp] = pygame.transform.scale(pygame.image.load("./rsc/icons/" + tmp + ".png"), (s.grid_x_inc, s.grid_y_inc))
        for i in range(0, 5):
            tmp = "color" + str(i)
            s.icons[tmp] = pygame.transform.scale(pygame.image.load("./rsc/icons/" + tmp + ".png"), (s.grid_x_inc, s.grid_y_inc))

    # Utils functions
    def get_pixel_pos(s, pos):
        y = s.base_y + pos.y * s.grid_y_inc
        x = s.base_x + pos.x * s.grid_x_inc
        #INVERTED FOR PYGAME !!!!
        return (x, y)

    def set_window_title(s, title):
        pygame.display.set_caption(title)
