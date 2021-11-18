import pygame
from pygame.constants import USEREVENT
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum
from UIComponents import UIElement
from pygame.sprite import RenderUpdates
from BarChart import BarChart, Bar
from threading import Thread
import time
BLUE = (106, 159, 181)
WHITE = (255, 255, 255)

ARRAY = [1, 22, 35, 10, 4, 7, 1, 22, 35, 10, 4, 7, 1, 22, 35, 10, 4, 7, 1, 22, 35, 10, 4, 7, 1, 22, 35, 10, 35, 10, 4, 7, 1, 22, 35, 10, 4, 7, 1, 4, 7, 1, 22, 35, 10, 4, 7 ]

class GameState(Enum):
    QUIT = -1
    TITLE = 0
    NEWGAME = 1
    BUBBLE = 2
    SORT = 3
    
sorting = False
def bubble_sort_vis(bar_chart, speed=1000):
    global sorting
    # Traverse through all array elements
    for i in range(len(bar_chart.bars)):
    # range(n) also work but outer loop will repeat one time more than needed.
 
        # Last i elements are already in place
        for j in range(0, len(bar_chart.bars)-1):
            if not sorting:
                return 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if bar_chart.bars[j].value > bar_chart.bars[j + 1].value :
                bar_chart.swap_positions(j, j+1)
                print(f"Swap {j} and {j+1}")
                time.sleep(speed/1000)
   

def bubble_sort(screen):
    global sorting
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
    sorting = False
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
                    sorting = True
                    thread = Thread(target = bubble_sort_vis, args = (values, 10))
                    thread.start()
                else:
                    if thread:
                        sorting=False
                        thread.join()
                    return ui_action

        elements.draw(screen)
        pygame.display.flip()
    
          
def game_loop(screen, elements):
    """ Handles game loop until an action is return by a button in the
    buttons sprite renderer.
    """
    while True:
        if pygame.event.get(pygame.QUIT):
                pygame.quit()
                exit()
        mouse_click = check_click()
        screen.fill(BLUE)
        game_state_change = check_elements(elements, mouse_click)
        if game_state_change:
            return game_state_change

        elements.draw(screen)
        pygame.display.flip()

          
def check_click():
    for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                return True
    return False

def check_elements(elements, mouse_click):
    for element in elements:
            ui_action = element.update(pygame.mouse.get_pos(), mouse_click)
            if ui_action is not None:
                return ui_action
    return None

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

        
def merge_sort_animation(bar_chart, start, speed=1000):
    if len(bar_chart.bars) > 1:
         # Finding the mid of the array
        mid = len(bar_chart.bars)//2
  
        # Dividing the array elements
        L = bar_chart.bars[:mid]
  
        # into 2 halves
        R = bar_chart.bars[mid:]
  
        # Sorting the first half
        merge_sort_animation(L, start)
  
        # Sorting the second half
        merge_sort_animation(R, start+mid)
  
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                bar_chart.bars[k] = L[i]
                i += 1
            else:
                bar_chart.bars[k] = R[j]
                j += 1
            k += 1
  
        # Checking if any element was left
        while i < len(L):
            bar_chart.bars[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            bar_chart.bars[k] = R[j]
            j += 1
            k += 1
     
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
    print("yo")
    pygame.time.set_timer(pygame.USEREVENT, 1000)
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