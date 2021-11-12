import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum
from UIComponents import UIElement
from pygame.sprite import RenderUpdates
from BarChart import BarChart, Bar
BLUE = (106, 159, 181)
WHITE = (255, 255, 255)

ARRAY = [1, 22, 35, 10, 4, 7, 2, 6, 8, 2, 1]


class GameState(Enum):
    QUIT = -1
    TITLE = 0
    NEWGAME = 1
    BUBBLE = 2

def title_screen(screen):
    start_btn = UIElement(
        center_position=(400, 400),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Start",
        action=GameState.NEWGAME,
    )
    quit_btn = UIElement(
        center_position=(400, 500),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Quit",
        action=GameState.QUIT,
    )
    bubble_btn = UIElement(
        center_position=(400, 300),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Bubble",
        action=GameState.BUBBLE,
    )

    buttons = RenderUpdates(start_btn, quit_btn, bubble_btn)

    return game_loop(screen, buttons)    

def bubble_sort_graph(screen, graph):
    for
def bubble_sort(screen):
    values = BarChart(ARRAY)
    return_btn = UIElement(
        center_position=(140, 20),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Return to main menu",
        action=GameState.TITLE,
    )
    swap = UIElement(
        center_position=(340, 20),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Swap",
        action= GameState.NEWGAME,
    )
    
    elements = RenderUpdates( return_btn, swap)
    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BLUE)
        values.draw(screen)
        for element in elements:
            ui_action = element.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                if ui_action == GameState.NEWGAME:
                     values.swap_positions(0, 5)
                else:
                    return ui_action

        elements.draw(screen)
        pygame.display.flip()
    
          
def game_loop(screen, elements):
    """ Handles game loop until an action is return by a button in the
    buttons sprite renderer.
    """
    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BLUE)

        for element in elements:
            ui_action = element.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action

        elements.draw(screen)
        pygame.display.flip()

          
  
def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    game_state = GameState.TITLE
    quit_btn = UIElement(
        center_position=(400, 500),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Quit",
        action=GameState.QUIT,
    )

    # main loop
    while True:
        while True:
            if game_state == GameState.TITLE:
                game_state = title_screen(screen)
                
            if game_state == GameState.BUBBLE:
                game_state = bubble_sort(screen)
                
            if game_state == GameState.QUIT:
                pygame.quit()
                return
        
        
if __name__ == "__main__":
    main()
















# visualizer = thorpy.Application(size=(300, 300), caption="Hello Word")

# merge_sort_button = thorpy.make_button("Merge Sort")
# quit_button = thorpy.make_button("Quit", func=thorpy.functions.quit_menu_func)

# background = thorpy.Background(color=(200, 200, 255),
#                                elements = [merge_sort_button, quit_button])

# #automatic centering / storage of elements
# thorpy.store(background)

# #Creat menu on top of background
# menu = thorpy.Menu(background)
# menu.play()

# visualizer.quit()