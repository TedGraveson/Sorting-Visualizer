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
import math

def bubble_sort_vis(bar_chart):  
    # Traverse through all array elements
    bar_chart.mutex.acquire()
    for i in range(len(bar_chart.bars)):
    # range(n) also work but outer loop will repeat one time more than needed.
        # current.change_color(constants.RED)
        for j in range(len(bar_chart.bars)-1, i, -1):
            
            if not constants.SORTING:
                bar_chart.mutex.release()
                return 
            
            bar_chart.bars[j].change_color(constants.YELLOW)
            bar_chart.bars[j-1].change_color(constants.YELLOW)
            time.sleep(constants.SPEED)
            if bar_chart.bars[j].value < bar_chart.bars[j - 1].value:
                bar_chart.bars[j].change_color(constants.RED)
                bar_chart.bars[j-1].change_color(constants.RED)
                time.sleep(constants.SPEED)
                bar_chart.swap_positions(j, j-1)
                time.sleep(constants.SPEED)
                bar_chart.bars[j].change_color(constants.YELLOW)
                bar_chart.bars[j-1].change_color(constants.YELLOW)
                time.sleep(constants.SPEED)

            bar_chart.bars[j].change_color((constants.WHITE))
            bar_chart.bars[j-1].change_color((constants.WHITE))
            
        bar_chart.bars[i].change_color(constants.GREEN)
        time.sleep(constants.SPEED)
        
    bar_chart.mutex.release()
    
    
def insertion_sort_vis(bar_chart):  
    bar_chart.mutex.acquire()
    
    bars = bar_chart.bars
    
    # Animate first bar
    current = bar_chart.bars[0]
    current.change_color(constants.RED)
    time.sleep(constants.SPEED)
    current.change_color(constants.GREEN)
    time.sleep(constants.SPEED)
    # Traverse through 1 to len(arr)
    for i in range(1, len(bars)):
  
        key = bars[i].value
  
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        
        current = bar_chart.bars[i]
        while j >= 0:
            
            if not constants.SORTING:
                bar_chart.mutex.release()
                return 
            compare = bar_chart.bars[j]
            old_color = compare.color
            current.change_color(constants.YELLOW)
            compare.change_color(constants.YELLOW)
            time.sleep(constants.SPEED)
            if key < bars[j].value:            
                current.change_color(constants.RED)
                compare.change_color(constants.RED)
                time.sleep(constants.SPEED)
                bar_chart.swap_positions(j+1, j)
                time.sleep(constants.SPEED)
                current.change_color(constants.YELLOW)
                compare.change_color(constants.YELLOW)
                time.sleep(constants.SPEED)
                compare.change_color(old_color)
                j -= 1
            else:
                compare.change_color(old_color)
                break
                      

        current.change_color(constants.GREEN)
        time.sleep(constants.SPEED)
        
    bar_chart.mutex.release()
    
    
    
def merge(bar_chart, start, mid, end):
    print(f"s:{start} end: {end}")
    finalStart = start
    finalEnd = end
    start2 = mid + 1
    arr = bar_chart.bars
    # l.change_color(constants.RED)
    # r.change_color(constants.RED)
    l = arr[mid]
    r = arr[start2]
    c1, c2 = arr[mid].color, arr[start2].color
    l.change_color(constants.YELLOW)
    r.change_color(constants.YELLOW)
    time.sleep(constants.SPEED)
    l.change_color(constants.WHITE)
    r.change_color(constants.WHITE)
    # If the direct merge is already sorted
    if (arr[mid].value <= arr[start2].value ):
        print("p1")
        return
        
    # Two pointers to maintain start
    # of both arrays to merge
    else:
        while (start <= mid and start2 <= end):
            startBar = arr[start]
            if not constants.SORTING:
                return
            # If element 1 is in right place
            if (arr[start].value <= arr[start2].value):
                col1, col2 = arr[start].color, arr[start2].color
                arr[start].change_color(constants.YELLOW)
                arr[start2].change_color(constants.YELLOW)
                time.sleep(constants.SPEED)
                arr[start].change_color(col1)
                arr[start2].change_color(col2)
                if finalStart == 0 and finalEnd == len(arr)-1:
                    arr[start].change_color(constants.GREEN)    
                start += 1
                print("p2")
            else:
                value = arr[start2].value
                index = start2
                # Shift all the elements between element 1
                # element 2, right by 1.
                while (index != start):
                    c1, c2 = arr[index].color, arr[index-1].color
                    arr[index].change_color(constants.RED)
                    arr[index-1].change_color(constants.RED)
                    time.sleep(constants.SPEED)
                    bar_chart.swap_positions(index, index-1)
                    time.sleep(constants.SPEED)
                    arr[index].change_color(c2)
                    arr[index-1].change_color(c1)
                   
                    index -= 1
                    print("p3")
                if finalStart == 0 and finalEnd == len(arr)-1:
                   arr[start].change_color(constants.GREEN) 
                   print("True")           
                # Update all the pointers
                start += 1
                mid += 1
                start2 += 1
    # l.change_color(c1)
    # r.change_color(c2)
 
 
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


# Calculating next gap
def nextGap(gap):
 
    if gap <= 1:
        return 0
         
    return int(math.ceil(gap / 2))
  
# Merging the subarrays using shell sorting
# Time Complexity: O(nlog n)
# Space Complexity: O(1)
def inPlaceMerge(bar_chart, start, end):
    print(f"s:{start} e:{end}")
    nums = bar_chart.bars
    gap = end - start + 1
    gap = nextGap(gap)
    final = (start == 0 and end == len(nums)-1)
    while gap > 0:
        i = start
        while (i + gap) <= end:
            
            if not constants.SORTING:
                return
            j = i + gap
            nums[i].change_color(constants.YELLOW)
            nums[j].change_color(constants.YELLOW)
            time.sleep(constants.SPEED)
            if nums[i].value > nums[j].value:
                nums[i].change_color(constants.RED)
                nums[j].change_color(constants.RED)
                time.sleep(constants.SPEED)
                bar_chart.swap_positions(i, j)
                time.sleep(constants.SPEED)
                nums[i].change_color(constants.YELLOW)
                nums[j].change_color(constants.YELLOW)
                time.sleep(constants.SPEED)
               
            nums[i].change_color(constants.WHITE)
            nums[j].change_color(constants.WHITE)   
            if final and gap == 1:
                nums[i].change_color(constants.GREEN)
                nums[j].change_color(constants.GREEN)     
            i += 1
            
         
        gap = nextGap(gap)
             
# merge sort makes log n recursive calls
# and each time calls merge()
# which takes nlog n steps
# Time Complexity: O(n*log n + 2((n/2)*log(n/2)) +
# 4((n/4)*log(n/4)) +.....+ 1)
# Time Complexity: O(logn*(n*log n))
# i.e. O(n*(logn)^2)
# Space Complexity: O(1)
def mergeSort(bar_chart, s, e):
 
    if s == e:
        return
 
    # Calculating mid to slice the
    # array in two halves
    mid = (s + e) // 2
 
    # Recursive calls to sort left
    # and right subarrays
    mergeSort(bar_chart, s, mid)
    mergeSort(bar_chart, mid + 1, e)
     
    inPlaceMerge(bar_chart, s, e)

def ms(bar_chart):
    mergeSort(bar_chart, 0, len(bar_chart.bars)-1)