from pygame import constants
import time
import constants
from types import FunctionType
import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum
from threading import Lock

def bubble_sort_vis(bar_chart):  
    # Traverse through all array elements
    bar_chart.mutex.acquire()
    for i in range(len(bar_chart.bars)):
    # range(n) also work but outer loop will repeat one time more than needed.
 
        
        # current.change_color((0, 0, 0))
        for j in range(len(bar_chart.bars)-1, i, -1):
            
            if not constants.SORTING:
                bar_chart.mutex.release()
                return 
            
            bar_chart.bars[j].change_color((0, 0, 0))
            bar_chart.bars[j-1].change_color((0, 0, 0))
            time.sleep(constants.SPEED)
            if bar_chart.bars[j].value < bar_chart.bars[j - 1].value:
                bar_chart.swap_positions(j, j-1)
            time.sleep(constants.SPEED)
            bar_chart.bars[j].change_color((constants.WHITE))
            bar_chart.bars[j-1].change_color((constants.WHITE))
            
        bar_chart.bars[i].change_color((0, 255, 0))
        
    bar_chart.mutex.release()
    
    
def insertion_sort_vis(bar_chart):  
    bar_chart.mutex.acquire()
    
    bars = bar_chart.bars
    
    # Animate first bar
    current = bar_chart.bars[0]
    current.change_color((0, 0, 0))
    time.sleep(constants.SPEED)
    current.change_color((0, 255, 0))
    time.sleep(constants.SPEED)
    # Traverse through 1 to len(arr)
    for i in range(1, len(bars)):
  
        key = bars[i].value
  
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        
        current = bar_chart.bars[i]
        current.change_color((0, 0, 0))
        while j >= 0 and key < bars[j].value:
            compare = bar_chart.bars[j]
            old_color = compare.color
            compare.change_color((0, 0, 0))
            time.sleep(constants.SPEED)
            if not constants.SORTING:
                bar_chart.mutex.release()
                return 
            else:
                bar_chart.swap_positions(j+1, j)
                j -= 1
            time.sleep(constants.SPEED)
            compare.change_color(old_color)
        current.change_color((0, 255, 0))
        
    bar_chart.mutex.release()
    
    
    
def merge(bar_chart, start, mid, end):
    start2 = mid + 1
    arr = bar_chart.bars
    
        
    # If the direct merge is already sorted
    if (arr[mid].value <= arr[start2].value ):
        return
 
    # Two pointers to maintain start
    # of both arrays to merge
    while (start <= mid and start2 <= end):
        if not constants.SORTING:
            return
        time.sleep(constants.SPEED)
        # If element 1 is in right place
        if (arr[start].value <= arr[start2].value):
            start += 1
            arr[start].change_color((0, 255, 0))
        else:
            value = arr[start2].value
            index = start2
            sorted = arr[start2]
            sorted.change_color((0, 255, 0))
            # Shift all the elements between element 1
            # element 2, right by 1.
            while (index != start):
                bar_chart.swap_positions(index, index-1)
                # arr[index] = arr[index - 1]
                index -= 1
            
            arr[start].value = value
            
            # Update all the pointers
            start += 1
            mid += 1
            start2 += 1
 
 
'''
* l is for left index and r is right index of
the sub-array of arr to be sorted
'''
 
def merge_sort_vis(bar_chart):
    _merge_sort_vis(bar_chart, 0, len(bar_chart.bars)-1)
    
def _merge_sort_vis(bar_chart, l, r):
    if (l < r):
 
        # Same as (l + r) / 2, but avoids overflow
        # for large l and r
        m = l + (r - l) // 2
 
        # Sort first and second halves
        _merge_sort_vis(bar_chart, l, m)
        _merge_sort_vis(bar_chart, m + 1, r)
        if not constants.SORTING:
            return

        merge(bar_chart, l, m, r) 