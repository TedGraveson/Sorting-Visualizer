from pygame import sprite
from pygame.sprite import Sprite
from UIComponents import UIElement
import pygame


class BarChart():
     """ An bar chart element showing a value """
     
     def __init__(self, values):
         pygame.sprite.AbstractGroup.__init__(self)
         self.width, self.height = pygame.display.get_window_size()
         self.padding = round(10 * (10/len(values)))
         self.values = values
         
         self.bar_width = round((self.width-(self.padding * (len(values) + 1 )))/len(values))
         self.selected = [None, None]
         
         self.bars = []
         for x, value in enumerate(self.values):
            offset = self.padding  + (self.padding  * x)
            topleft = (self.bar_width*x + offset, self.height - (value * 10))
            bar = Bar(value, x, (255, 255, 255), topleft, self.bar_width, value * 10)
            self.bars.append(bar)
       
     def swap_positions(self, x, y):
         bars = self.bars  
         pixel_shift = y-x
         bars[x].move(pixel_shift * (self.bar_width + self.padding), 0)
         bars[y].move((-pixel_shift * (self.bar_width + self.padding)), 0)
         bars[x], bars[y] = bars[y], bars[x]
                  
         return None
        
     def draw(self, surface):
        for bar in self.bars:
            bar.draw(surface)
    #  def draw(self, surface):
    #     """ Draws element onto a surface """
    #     for x, value in enumerate(self.values):
    #         offset = self.padding  + (self.padding  * x)
    #         pygame.draw.rect(surface, (255, 255, 255), (self.bar_width*x + offset, self.height - (value * 10), self.bar_width, value * 10), 0)
            
            
class Bar(pygame.sprite.Sprite):
    """Interactive Bar Element for sorting arrays

    Args:
        Sprite ([type]): [description]
    """
    def __init__(self, value, index, color, topleft, width, height, action=None):
        self.value = value
        self.index = index
        self.height = height
        self.width = self.width
        
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
        super().__init__()
        
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
            
    # def set_value(self, value):
    #     self.value = value
    #     self.height = 10 * value
        
    #     default = pygame.Surface((width, self.height))
    #     default.fill(color)
        
    #     hover = pygame.Surface((width, height))
    #     hover.fill((0, 0, 0))
        
    #     self.images = [default, hover]
    #     self.rects = [
    #         default.get_rect(topleft=topleft),
    #         hover.get_rect(topleft=topleft)
    #     ]