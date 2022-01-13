import pygame
from resources.gamestate import GameState
from sorting.game_loop import *
from sorting.heap import heap_sort_vis
from objects.bar_chart import random_bar_chart

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    game_state = GameState.TITLE
    
    # Main loop
    while True:
        # Title screen
        print(game_state)
        if game_state == GameState.TITLE:
            game_state = title_screen(screen)
            
        # Bubble sort
        elif game_state == GameState.BUBBLE:
            game_state = game_loop(screen, RenderUpdates(sorting_controls()), graphs=[random_bar_chart()], sorting_algo=[bubble_sort_vis])
            
        # Insertion sort
        elif game_state == GameState.INSERTION:
            game_state = game_loop(screen, RenderUpdates(sorting_controls()), graphs=[random_bar_chart()], sorting_algo=[insertion_sort_vis])
            
        # Merge sort
        elif game_state == GameState.MERGE:
            game_state = game_loop(screen, RenderUpdates(sorting_controls()), graphs=[random_bar_chart()], sorting_algo=[ms])
            
        elif game_state == GameState.QUICK:
            game_state = game_loop(screen, RenderUpdates(sorting_controls()), graphs=[random_bar_chart()], sorting_algo=[quick_sort_vis])
            
        elif game_state == GameState.HEAP:
            game_state = game_loop(screen, RenderUpdates(sorting_controls()), graphs=[random_bar_chart()], sorting_algo=[heap_sort_vis])
            
        # Compare sorts
        elif game_state == GameState.COMPARE:
            game_state = compare_sorts(screen)
            
        # Quit application
        elif game_state == GameState.QUIT or pygame.event.get(pygame.QUIT):
            pygame.quit()
            exit()