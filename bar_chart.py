from pygame import color, sprite
from pygame.sprite import Sprite
import pygame
from threading import Lock
from numpy import random
import constants
from constants import SIZE_SMALL, SIZE_MEDIUM, SIZE_LARGE


class Bar(pygame.sprite.Sprite):
    """Interactive Bar Element for sorting arrays

    Args:
        Sprite ([type]): [description]
    """
    def __init__(self, value, index, color, topleft, width, height, action=None):
        super().__init__()
        self.value = value
        self.index = index
        self.height = height
        self.width = width
        self.color = color
        self.topleft = topleft
        
        default = pygame.Surface((width, height))
        default.fill(color)
        
        hover = pygame.Surface((width, height))
        hover.fill((0, 0, 0))
        
        self.images = [default, hover]
        self.rects = [
            default.get_rect(topleft=topleft),
            hover.get_rect(topleft=topleft)
        ]
        self.mouse_over = False
        self.action = action
        
    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]
        
    def update(self, mouse_pos, mouse_up):
        """ Updates the mouse_over variable and returns the button's
            action value when clicked.
        """
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False

    def draw(self, surface):
        """ Draws element onto a surface """
        surface.blit(self.image, self.rect)
        
    def move(self, x, y):
        for rect in self.rects:
            pygame.Rect.move_ip(rect, x, y)
            
    def change_color(self, new_color):
        self.color = new_color
        for image in self.images:
            image.fill(new_color)


class BarChart(pygame.sprite.AbstractGroup):
     """ An bar chart element showing a value """
     
     def __init__(self, values, size=None, origin=None):
         pygame.sprite.AbstractGroup.__init__(self)
         
         if size is not None:
            self.width, self.height = size
         else:             
            self.width, self.height = pygame.display.get_window_size()
         
         self.padding = round(10 * (10/len(values)))
         self.values = values
         self.origin= origin
         self.bar_width = round((self.width-(self.padding * (len(values) + 1 )))/len(values))
         self.selected = [None, None]
         
         self.mutex = Lock()
         
         self.bars = []
         
         value_to_height = self.height/100
         
         for x, value in enumerate(self.values):
            offset = self.padding  + (self.padding  * x)
            if self.origin is not None:
                topLeft  = (self.bar_width*x + offset, self.origin[1] - (value * value_to_height))
            else:
                topLeft = (self.bar_width*x + offset, self.height - (value * value_to_height))
            bar = Bar(value, x, (255, 255, 255), topLeft, self.bar_width, value * value_to_height)
            self.bars.append(bar)
       
     def swap_positions(self, x, y):
         bars = self.bars  
         pixel_shift = y-x
         bars[x].move(pixel_shift * (self.bar_width + self.padding), 0)
         bars[y].move((-pixel_shift * (self.bar_width + self.padding)), 0)
         bars[x], bars[y] = bars[y], bars[x]
        
     def draw(self, surface):
        for bar in self.bars:
            bar.draw(surface)

def random_bar_chart(low=1, high=99, size=(800, 500), origin=(0, 600)):
    return BarChart(random.randint(low=1, high=99, size=(constants.SIZE)), size=size, origin=origin)