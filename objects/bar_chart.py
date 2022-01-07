import pygame
from threading import Lock
from numpy import random
import resources.config as config


class Bar(pygame.sprite.Sprite):
    """Bar element representing a number in a BarChart.

    Args:
        value: integer value
        index: index in representitive array
        color: color of bar when drawn
        topleft: pixel coordinates of the top left corner of the bar
        width: width of bar in pixels
        height: height of bar in pixels
        action: event executed when bar is clicked
    """
    def __init__(self, value, index, color, topleft, width, height, action=None):
        super().__init__()
        self.value = value
        self.index = index
        self.height = height
        self.width = width
        self.color = color
        self.topleft = topleft
        
        # Currently bars have no additioal behaviour when hovered over
        default = pygame.Surface((width, height))
        default.fill(color)
        hover = pygame.Surface((width, height))
        hover.fill(color)
        
        self.images = [default, hover]
        self.rects = [
            default.get_rect(topleft=topleft),
            hover.get_rect(topleft=topleft)
        ]
        self.mouse_over = False
        self.action = action
    @property    
    def image(self):
        """Gets visual components for a bar.

        Returns:
            Mouse over visual or default visual.
        """
        return self.images[1] if self.mouse_over else self.images[0]
    @property
    def rect(self):
        """Gets geometric components for a bar

        Returns:
            Mouse over rectangle or default rectangle.
        """
        return self.rects[1] if self.mouse_over else self.rects[0]
        
    def update(self, mouse_pos, mouse_up):
        """ Updates the mouse_over variable.
        
        Returns:
            Button's action value when clicked.
        """
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False

    def draw(self, surface):
        """Draws the bar onto the screen

        Args:
            surface: Pygame screen instance
        """
        surface.blit(self.image, self.rect)
        
    def move(self, x, y):
        """Moves a bar's position on the screen.

        Args:
            x: pixel offset in the x dimension
            y: pixel offset in the y dimension
        """
        for rect in self.rects:
            pygame.Rect.move_ip(rect, x, y)
            
    def change_color(self, new_color):
        """Changes the color of a bar.

        Args:
            new_color: color to change the bar to
        """
        self.color = new_color
        for image in self.images:
            image.fill(new_color)


class BarChart(pygame.sprite.AbstractGroup):
    """A visual representation of an array presented as a bar chart.

    Args:
        values: integer array
        size: pixel dimensions of chart, defaults to window size
        origin: bottom left corner of chart, defaults to (0, max_y)
    """
     
    def __init__(self, values, size=None, origin=None):
        pygame.sprite.AbstractGroup.__init__(self)
        
        if size is not None:
            self.width, self.height = size
        else:             
            self.width, self.height = pygame.display.get_window_size()
            
            
        if origin is not None:
            self.origin = origin
        else:
            self.origin = (0, self.height)
               
        self.padding = round(10 * (10/len(values)))
        self.values = values
        self.origin= origin
        self.bar_width = round((self.width-(self.padding * (len(values) + 1 )))/len(values))
        self.selected = [None, None]
        
        self.mutex = Lock()
        
        self.bars = []
        
        value_to_height = self.height/100
        
        for x, value in enumerate(self.values):
            offset = self.padding  + (self.padding  * x) + self.origin[0]
            
            topLeft  = (self.bar_width*x + offset, self.origin[1] - (value * value_to_height))
    
            bar = Bar(value, x, (255, 255, 255), topLeft, self.bar_width, value * value_to_height)
            self.bars.append(bar)
    
    def swap_positions(self, x, y):
        """Swap positions of two values in an array (two bars in graph).

        Args:
            x: index of first value (bar)
            y: index of second value (bar)
        """
        bars = self.bars  
        pixel_shift = y-x
        bars[x].move(pixel_shift * (self.bar_width + self.padding), 0)
        bars[y].move((-pixel_shift * (self.bar_width + self.padding)), 0)
        bars[x], bars[y] = bars[y], bars[x]
    
    def draw(self, surface):
        """Draws bar graph to screen

        Args:
            surface: Pygame screen instance
        """
        for bar in self.bars:
            bar.draw(surface)

def random_bar_chart(low=1, high=99, size=(800, 500), origin=(0, 600)):
    """Generates a random bar chart.

    Args:
        low: lower bound for value range, defaults to 1.
        high: upper bound for value range, defaults to 99.
        size: tuple for pixel size (width, height), defaults to (800, 500).
        origin: lower left corner coordinates of graph, defaults to (0, 600).

    Returns:
        Random bar graph with values in range [low, high].
    """
    return BarChart(random.randint(low=1, high=99, size=(config.SIZE)), size=size, origin=origin)