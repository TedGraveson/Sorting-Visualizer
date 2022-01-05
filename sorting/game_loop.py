
import pygame
from resources.gamestate import GameState
import resources.config as config
from threading import Thread
from numpy import random

from sorting.bubble import bubble_sort_vis
from sorting.insertion import insertion_sort_vis
from sorting.merge import merge_sort_vis, ms

from pygame.sprite import RenderUpdates
from objects.buttons import *
from objects.bar_chart import *

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
                    if not config.SORTING:
                        config.SORTING = True
                        for x in range(len(graphs)):
                            threads[x] = (Thread(target = sorting_algo[x], args = (graphs[x], )))
                            threads[x].start()
    
                elif ui_action == GameState.RANDOMIZE:
                    if config.SORTING:
                        config.SORTING = False
                        for thread in threads:
                            thread.join()
                
                    new_graphs = [0] * len(graphs)
                    values = random.randint(low=1, high=99, size=config.SIZE)
                    for x in range(len(graphs)):
                        new_graphs[x] = BarChart(values, (graphs[x].width, graphs[x].height), graphs[x].origin)
                    graphs = new_graphs
                    
                elif ui_action == GameState.SPEED:
                    for button in elements:
                        if button.text_rgb is not config.WHITE:
                            button.change_color(config.WHITE)
                        element.change_color(config.RED)
                
                elif ui_action == GameState.TITLE:
                    if config.SORTING:
                        config.SORTING = False
                        for thread in threads:
                                thread.join()
                    return ui_action
                
                else:
                    return ui_action
                

        screen.fill(config.BLUE)
        for graph in graphs:
            graph.draw(screen)
            
        elements.draw(screen)
        pygame.display.flip()
        
def check_click():
    """Checks if the user has performed a mouse click.

    Returns:
        Boolean value that is true if click occured, false otherwise.
    """
    for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                return True
    return False
       
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