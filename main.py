import pygame
from resources.gamestate import GameState
from sorting.game_loop import *

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    game_state = GameState.TITLE
    
    # Main loop
    while True:
        # Title screen
        if game_state == GameState.TITLE:
            game_state = title_screen(screen)
            
        # Bubble sort
        elif game_state == GameState.BUBBLE:
            game_state = bubble_sort(screen)
            
        # Insertion sort
        elif game_state == GameState.INSERTION:
            game_state = insertion_sort(screen)
            
        # Merge sort
        elif game_state == GameState.MERGE:
            game_state = merge_sort(screen)
            
        # Compare sorts
        elif game_state == GameState.COMPARE:
            game_state = compare_sorts(screen)
            
        # Quit application
        elif game_state == GameState.QUIT or pygame.event.get(pygame.QUIT):
            pygame.quit()
            exit()