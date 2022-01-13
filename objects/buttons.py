import resources.config as config
import pygame
import pygame.freetype
from pygame.sprite import Sprite
from resources.gamestate import GameState

def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
    """ Creates the text label for buttons.
    
    Args:
        text
    
    """
    font = pygame.freetype.SysFont("Courier", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()


class Button(Sprite):
    """ An user interface element that can be added to a surface """

    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb, action=None, selected=None):
        """
        Args:
            center_position - tuple (x, y)
            text - string of text to write
            font_size - int
            bg_rgb (background colour) - tuple (r, g, b)
            text_rgb (text colour) - tuple (r, g, b)
            action - the gamestate change associated with this button
        """
        self.mouse_over = False
        self.center_position = center_position
        self.text = text
        self.font_size = font_size
        self.bg_rgb = bg_rgb
        self.text_rgb = text_rgb
        self.action = action

        default_image = create_surface_with_text(
            text=text, font_size=font_size, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        highlighted_image = create_surface_with_text(
            text=text, font_size=font_size * 1.2, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        self.images = [default_image, highlighted_image]
        
        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position),
        ]

        # assign button action
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
                if (callable(self.action)):
                    return self.action(self)
                else:
                    return self.action
        else:
            self.mouse_over = False

    def draw(self, surface):
        """ Draws element onto a surface """
        surface.blit(self.image, self.rect)
        
    def change_color(self, color):
        self.images[0] = create_surface_with_text(text=self.text, font_size=self.font_size, text_rgb=color, bg_rgb=self.bg_rgb)
        self.images[1] = create_surface_with_text(text=self.text, font_size=self.font_size * 1.2, text_rgb=color, bg_rgb=self.bg_rgb)
        self.text_rgb = color

            

def title_buttons():
    bubble_btn = Button(
        center_position=(400, 100),
        font_size=30,
        bg_rgb=config.BLUE,
        text_rgb=config.WHITE,
        text="Bubble Sort",
        action=GameState.BUBBLE,
    )
    quick_btn = Button(
        center_position=(400, 250),
        font_size=30,
        bg_rgb=config.BLUE,
        text_rgb=config.WHITE,
        text="Quick Sort",
        action=GameState.QUICK,
    )
    heap_btn = Button(
        center_position=(400, 300),
        font_size=30,
        bg_rgb=config.BLUE,
        text_rgb=config.WHITE,
        text="Heap Sort",
        action=GameState.HEAP,
    )
    insertion_btn = Button(
        center_position=(400, 148), # weird spacing bug
        font_size=30,
        bg_rgb=config.BLUE,
        text_rgb=config.WHITE,
        text="Insertion Sort",
        action=GameState.INSERTION,
    ),
    merge_btn = Button(
        center_position=(400, 200),
        font_size=30,
        bg_rgb=config.BLUE,
        text_rgb=config.WHITE,
        text="Merge Sort",
        action=GameState.MERGE,
    )
    compare_btn = Button(
        center_position=(400, 400),
        font_size=30,
        bg_rgb=config.BLUE,
        text_rgb=config.WHITE,
        text="Compare Sorts",
        action=GameState.COMPARE,
    )
    quit_btn = Button(
        center_position=(400, 500),
        font_size=30,
        bg_rgb=config.BLUE,
        text_rgb=config.WHITE,
        text="Quit",
        action=GameState.QUIT,
    )

    return [bubble_btn, quick_btn, insertion_btn, merge_btn, compare_btn, heap_btn, quit_btn]
    
def sorting_controls(sort_title="Sort"):
    return_btn = Button(
        center_position=(200, 20),
        font_size=20,
        bg_rgb=config.BLUE,
        text_rgb=config.WHITE,
        text="Main menu",
        action=GameState.TITLE,
    )
    randomize = Button(
        center_position=(400, 20),
        font_size=20,
        bg_rgb=config.BLUE,
        text_rgb=config.WHITE,
        text="Randomize",
        action= GameState.RANDOMIZE,
    )
    sort = Button(
        center_position=(600, 20),
        font_size=20,
        bg_rgb=config.BLUE,
        text_rgb=config.WHITE,
        text=sort_title,
        action= GameState.SORT,
    )
    slow = Button(
        center_position=(200, 50),
        font_size=20,
        bg_rgb=config.BLUE,
        text_rgb=config.WHITE,
        text="Slow",
        action= set_slow,
    )
    medium = Button(
        center_position=(400, 50),
        font_size=20,
        bg_rgb=config.BLUE,
        text_rgb=config.YELLOW,
        text="Medium",
        action=set_med,
    )
    fast = Button(
        center_position=(600, 50),
        font_size=20,
        bg_rgb=config.BLUE,
        text_rgb=config.WHITE,
        text="Fast",
        action= set_fast,
    )
    
    return [return_btn, randomize, sort, slow, medium, fast]


def set_slow(self):
    config.SPEED = config.SLOW
    config.SIZE = config.SIZE_SMALL
    return GameState.SPEED

def set_med(self):
    config.SPEED = config.MEDIUM
    config.SIZE = config.SIZE_MEDIUM
    return GameState.SPEED

def set_fast(self):
    config.SPEED = config.FAST
    config.SIZE = config.SIZE_LARGE
    return GameState.SPEED