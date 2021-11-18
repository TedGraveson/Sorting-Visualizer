import threading
import time
import pygame
# Python program for implementation of Bubble Sort
def bubble_sort_vis(bar_chart, speed=1000):
    global sorting
    arr = bar_chart.bars
    # Traverse through all array elements
    for i in range(len(arr)):
    # range(n) also work but outer loop will repeat one time more than needed.
 
        # Last i elements are already in place
        for j in range(0, len(arr)-1):
            if not sorting:
                return 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j].value > arr[j + 1].value :
                bar_chart.swap_positions(j, j+1)
                print(f"Swap {j} and {j+1}")
                time.sleep(1)
                pygame.display.flip()
                
                