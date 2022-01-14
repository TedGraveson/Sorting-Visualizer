import resources.config as config
import time
import math
# Calculating next gap
def nextGap(gap):
 
    if gap <= 1:
        return 0
         
    return int(math.ceil(gap / 2))
  
# Merging the subarrays using shell sorting
# Time Complexity: O(nlog n)
# Space Complexity: O(1)
def inPlaceMerge(bar_chart, start, end):
    nums = bar_chart.bars
    gap = end - start + 1
    gap = nextGap(gap)
    final = (start == 0 and end == len(nums)-1)
    while gap > 0:
        i = start
        while (i + gap) <= end:
            
            if not config.SORTING:
                return
            j = i + gap
            nums[i].change_color(config.YELLOW)
            nums[j].change_color(config.YELLOW)
            time.sleep(config.SPEED)
            if nums[i].value > nums[j].value:
                nums[i].change_color(config.RED)
                nums[j].change_color(config.RED)
                time.sleep(config.SPEED)
                bar_chart.swap_positions(i, j)
                time.sleep(config.SPEED)
                nums[i].change_color(config.YELLOW)
                nums[j].change_color(config.YELLOW)
                time.sleep(config.SPEED)
               
            nums[i].change_color(config.WHITE)
            nums[j].change_color(config.WHITE)   
            if final and gap == 1:
                nums[i].change_color(config.GREEN)
                nums[j].change_color(config.GREEN)     
            i += 1
            
         
        gap = nextGap(gap)
             

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

def merge_sort_vis(bar_chart):
    """Merge sort visualization for a bar chart.

    Args:
        bar_chart: Bar chart to be sorted
    """
    bar_chart.mutex.acquire()
    mergeSort(bar_chart, 0, len(bar_chart.bars)-1)
    bar_chart.mutex.release()
    
    
    
