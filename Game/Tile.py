# /* Tile.py
import pygame

class Tile:
    def __init__(self, x, y, tile_width, tile_height):
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.abs_x = x * tile_width
        self.abs_y = y * tile_height
        self.abs_pos = (self.abs_x, self.abs_y)
        self.color = 'light' if (x + y) % 2 == 0 else 'dark'
        self.draw_color = (220, 189, 194) if self.color == 'light' else (53, 53, 53)
        self.highlight_color = (100, 249, 83) if self.color == 'light' else (0, 228, 10)
        self.occupying_piece = None
        self.coord = self.get_coord()
        self.highlight = False
        self.rect = pygame.Rect(
            self.abs_x,
            self.abs_y,
            self.tile_width,
            self.tile_height
        )