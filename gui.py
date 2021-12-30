import pygame
from pygame.constants import USEREVENT
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum
from pygame.sprite import RenderUpdates
from bar_chart import BarChart, Bar, random_bar_chart
from threading import Thread
import time
from numpy import random

import constants
from constants import FAST, GameState, BLUE, WHITE, SORTING
from buttons import sorting_controls, title_buttons

from sorting_algorithms import bubble_sort_vis, insertion_sort_vis, merge_sort_vis, ms

def check_click():
    """Checks if the user has performed a mouse click.

    Returns:
        Boolean value that is true if click occured, false otherwise.
    """
    for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                return True
    return False

def game_loop(screen, elements, sorting_algo=[], graphs=[], *args):
    """Draws all visual updates to the screen.

    Args:
        screen: Pygame display instance
        elements: All pygame objects being tracked

    Returns:
        GameState enum corresponing to action requsted by a user click.
    """
    
    threads = [ 0 ] * len(graphs)
    
    while True:
        if pygame.event.get(pygame.QUIT):
            pygame.quit()
            exit()   
            
        mouse_click = check_click()
        
        for element in elements:
            ui_action = element.update(pygame.mouse.get_pos(), mouse_click)
            if ui_action is not None:
                if ui_action == GameState.SORT:
                    if not constants.SORTING:
                        constants.SORTING = True
                        for x in range(len(graphs)):
                            threads[x] = (Thread(target = sorting_algo[x], args = (graphs[x], )))
                            threads[x].start()
    
                elif ui_action == GameState.RANDOMIZE:
                    if constants.SORTING:
                        constants.SORTING = False
                        for thread in threads:
                            thread.join()
                
                    new_graphs = [0] * len(graphs)
                    values = random.randint(low=1, high=99, size=constants.SIZE)
                    for x in range(len(graphs)):
                        new_graphs[x] = BarChart(values, (graphs[x].width, graphs[x].height), graphs[x].origin)
                    graphs = new_graphs
                    
                elif ui_action == GameState.SPEED:
                    for button in elements:
                        if button.text_rgb is not constants.WHITE:
                            button.change_color(constants.WHITE)
                        element.change_color(constants.RED)
                
                elif ui_action == GameState.TITLE:
                    if constants.SORTING:
                        constants.SORTING = False
                        for thread in threads:
                                thread.join()
                    return ui_action
                
                else:
                    return ui_action
                

        screen.fill(BLUE)
        for graph in graphs:
            graph.draw(screen)
            
        elements.draw(screen)
        pygame.display.flip()
        
        
def bubble_sort(screen):
    buttons = RenderUpdates(sorting_controls())
    graphs = [random_bar_chart()]
    sorting_algos = [bubble_sort_vis]
    return game_loop(screen, buttons, graphs=graphs, sorting_algo=sorting_algos)
    
    
def insertion_sort(screen):
    buttons = RenderUpdates(sorting_controls())
    graphs = [random_bar_chart()]
    sorting_algos = [insertion_sort_vis]
    return game_loop(screen, buttons, graphs=graphs, sorting_algo=sorting_algos)

def merge_sort(screen):
    buttons = RenderUpdates(sorting_controls())
    graphs = [random_bar_chart()]
    sorting_algos = [ms]
    return game_loop(screen, buttons, graphs=graphs, sorting_algo=sorting_algos)

def compare_sorts(screen):
    buttons = RenderUpdates(sorting_controls())
    
    b1 = random_bar_chart(size=(800, 100), origin=(0, 600))
    b2 = random_bar_chart(size=(800, 100), origin=(0, 400))
    b3 = random_bar_chart(size=(800, 100), origin=(0, 200))
    
    graphs = [b1, b2, b3]
        
    sorting_algos = [bubble_sort_vis, insertion_sort_vis, ms]
    return game_loop(screen, buttons, graphs=graphs, sorting_algo=sorting_algos)
    

def title_screen(screen):
    buttons = RenderUpdates(title_buttons())
    return game_loop(screen, buttons)    

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    game_state = GameState.TITLE
    
    # main loop
    while True:
        # Title Screen
        if game_state == GameState.TITLE:
            game_state = title_screen(screen)
            
        # Bubble Sort
        elif game_state == GameState.BUBBLE:
            game_state = bubble_sort(screen)
            
        # Insertion Sort
        elif game_state == GameState.INSERTION:
            game_state = insertion_sort(screen)
            
        # Merge Sort
        elif game_state == GameState.MERGE:
            game_state = merge_sort(screen)
            
        # Compare Sorts
        elif game_state == GameState.COMPARE:
            game_state = compare_sorts(screen)
            
        # Quit Application
        elif game_state == pygame.QUIT or pygame.event.get(pygame.QUIT):
            pygame.quit()
            exit()