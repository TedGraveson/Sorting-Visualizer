import pygame
from resources.gamestate import GameState
import resources.config as config
from threading import Thread
from numpy import random

from sorting.bubble import bubble_sort_vis
from sorting.heap import heap_sort_vis
from sorting.insertion import insertion_sort_vis
from sorting.merge import merge_sort_vis
from sorting.quick import quick_sort_vis

from pygame.sprite import RenderUpdates
from objects.buttons import *
from objects.bar_chart import *

def game_loop(screen, elements, sorting_algo=[], graphs=[]):
    """Handles all visual updates and events occuring during sorting.

    Args:
        screen: Pygame display instance
        elements: All pygame objects being tracked
        sorting_algo: The algorithm(s) used for sorting
        graphs: BarGraph objects to be sorted

    Returns:
        GameState enum corresponing to a button being clicked
    """
    
    # Default to medium size and speed
    config.SPEED = config.MEDIUM
    config.SIZE = config.SIZE_MEDIUM
    
    # Array to hold threads
    threads = [ 0 ] * len(graphs)
    
    while True:
        if pygame.event.get(pygame.QUIT):
            pygame.quit()
            exit()   
            
        mouse_click = check_click()
        
        # Checking if any buttons were clicked
        for element in elements:
            ui_action = element.update(pygame.mouse.get_pos(), mouse_click)
            
            # Button was clicked, determine action to be taken
            if ui_action is not None:
                
                # Begin sorting on each BarGraph
                if ui_action == GameState.SORT:
                    if not config.SORTING:
                        config.SORTING = True
                        for x in range(len(graphs)):
                            threads[x] = (Thread(target = sorting_algo[x], args = (graphs[x], )))
                            threads[x].start()
    
                # Stop sorting and create new BarGraphs
                elif ui_action == GameState.RANDOMIZE:
                    if config.SORTING:
                        config.SORTING = False
                        for thread in threads:
                            thread.join()
                    
                    graphs = randomize_graphs(graphs)
                    
                # Changing sorting speed and button color
                elif ui_action == GameState.SPEED:
                    for button in elements:
                        if button.text_rgb is not config.WHITE:
                            button.change_color(config.WHITE)
                        element.change_color(config.YELLOW)
                    if not config.SORTING:
                        graphs = randomize_graphs(graphs)
                
                # Returning to main menu
                elif ui_action == GameState.TITLE:
                    if config.SORTING:
                        config.SORTING = False
                        for thread in threads:
                                thread.join()
                    return ui_action
                
                else:
                    return ui_action
                
        # Update all GUI elements
        screen.fill(config.BLUE)
        for graph in graphs:
            graph.draw(screen)
        elements.draw(screen)
        pygame.display.flip()
        
def randomize_graphs(graphs):
    """Randomize all graphs on screen.

    Args:
        graphs: Array of bar graph objects

    Returns:
        Array of new bar graph objects
    """
    new_graphs = [0] * len(graphs)
    values = random.randint(low=1, high=99, size=config.SIZE)
    for x in range(len(graphs)):
        new_graphs[x] = BarChart(values, (graphs[x].width, graphs[x].height), graphs[x].origin)
    
    return new_graphs
        
def check_click():
    """Checks if the user has performed a mouse click.

    Returns:
        Boolean value that is true if click occured, false otherwise.
    """
    for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                return True
    return False
       

def compare_sorts(screen):
    """Initialize elements for merge, bubble, and insertion sort.

    Args:
        screen: Pygame screen instance

    Returns:
        GameState enum once user exits to main menu
    """
    
    buttons = RenderUpdates(sorting_controls())
    
    b1 = random_bar_chart(size=(800, 100), origin=(0, 200))
    b2 = random_bar_chart(size=(800, 100), origin=(0, 300))
    b3 = random_bar_chart(size=(800, 100), origin=(0, 400))
    b4 = random_bar_chart(size=(800, 100), origin=(0, 500))
    b5 = random_bar_chart(size=(800, 100), origin=(0, 600))
    
    graphs = [b1, b2, b3, b4, b5]
        
    sorting_algos = [bubble_sort_vis, insertion_sort_vis, merge_sort_vis, quick_sort_vis, heap_sort_vis,]
    return game_loop(screen, buttons, graphs=graphs, sorting_algo=sorting_algos)

def title_screen(screen):
    """Initialize elements for title screen.

    Args:
        screen: Pygame screen instance

    Returns:
        GameState enum
    """
    buttons = RenderUpdates(title_buttons())
    return game_loop(screen, buttons)