import resources.config as config
import time

def partition(bar_chart, low, high):
    arr = bar_chart.bars
    i = (low-1)         # index of smaller element
    pivot = arr[high]
    old_pivot_color = pivot.color
    # pivot.change_color(config.BLACK) # pivot
    
    low_bar, old_low_color = arr[i], arr[i].color
     
    for j in range(low, high):
        if not config.SORTING:
            return 
        # If current element is smaller than or
        # equal to pivot
        compare, old_compare_color = arr[j], arr[j].color
        # compare.change_color(config.YELLOW)
        time.sleep(config.SPEED)
        if compare.value <= pivot.value:
            # compare.change_color(config.RED)
            # increment index of smaller element
            i = i+1
            # low_bar.change_color(old_low_color)
            # low_bar, old_low_color = arr[i], arr[i].color
            # low_bar.change_color(config.RED)
            time.sleep(config.SPEED)
            bar_chart.swap_positions(i, j)
            time.sleep(config.SPEED)
            # compare.change_color(config.YELLOW)
            # low_bar.change_color(old_low_color)
            time.sleep(config.SPEED)
            
        compare.change_color(old_compare_color)
 
    # arr[i+1], arr[high] = arr[high], arr[i+1]
    
    time.sleep(config.SPEED)
    bar_chart.swap_positions(i+1, high)
    time.sleep(config.SPEED)
    # pivot.change_color(old_pivot_color)
    # low_bar.change_color(old_low_color)
    return (i+1)
 
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
 
# Function to do Quick sort
 
 
def quickSort(bar_chart, low, high):
    arr = bar_chart.bars
    if len(arr) == 1:
        return arr
    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(bar_chart, low, high)
        arr[pi].change_color(config.GREEN)
 
        # Separately sort elements before
        # partition and after partition
        quickSort(bar_chart, low, pi-1)
        quickSort(bar_chart, pi+1, high)
    elif low == high:
        arr[low].change_color(config.GREEN)

def quick_sort_vis(bar_chart):
    quickSort(bar_chart, 0, len(bar_chart.bars)-1)