import pygame
from resources.gamestate import GameState
from sorting.game_loop import *
from sorting.heap import heap_sort_vis
from objects.bar_chart import random_bar_chart

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Sorting Visualizer')
    game_state = GameState.TITLE
    
    # Main loop
    while True:
        # Title screen
        if game_state == GameState.TITLE:
            pygame.display.set_caption('Sorting Visualizer')
            game_state = title_screen(screen)
            
        # Bubble sort
        elif game_state == GameState.BUBBLE:
            pygame.display.set_caption('Bubble Sort')
            game_state = game_loop(screen, RenderUpdates(sorting_controls()), graphs=[random_bar_chart()], sorting_algo=[bubble_sort_vis])
            
        # Insertion sort
        elif game_state == GameState.INSERTION:
            pygame.display.set_caption('Insertion Sort')
            game_state = game_loop(screen, RenderUpdates(sorting_controls()), graphs=[random_bar_chart()], sorting_algo=[insertion_sort_vis])
            
        # Merge sort
        elif game_state == GameState.MERGE:
            pygame.display.set_caption('Merge Sort')
            game_state = game_loop(screen, RenderUpdates(sorting_controls()), graphs=[random_bar_chart()], sorting_algo=[merge_sort_vis])
            
        elif game_state == GameState.QUICK:
            pygame.display.set_caption('Quick Sort')
            game_state = game_loop(screen, RenderUpdates(sorting_controls()), graphs=[random_bar_chart()], sorting_algo=[quick_sort_vis])
            
        elif game_state == GameState.HEAP:
            pygame.display.set_caption('Heap Sort')
            game_state = game_loop(screen, RenderUpdates(sorting_controls()), graphs=[random_bar_chart()], sorting_algo=[heap_sort_vis])
            
        # Compare sorts
        elif game_state == GameState.COMPARE:
            pygame.display.set_caption('Bubble | Insertion | Merge | Quick | Heap')
            game_state = compare_sorts(screen)
            
        # Quit application
        elif game_state == GameState.QUIT or pygame.event.get(pygame.QUIT):
            pygame.quit()
            exit()