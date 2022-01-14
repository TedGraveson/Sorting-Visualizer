import resources.config as config
import time

def partition(bar_chart, low, high):
    arr = bar_chart.bars
    i = (low-1)         # index of smaller element
    pivot = arr[high]
    pivot.change_color(config.PURPLE)
    
    for j in range(low, high):
        # If current element is smaller than or
        # equal to pivot
        compare, old_compare_color = arr[j], arr[j].color
        compare.change_color(config.YELLOW)
        time.sleep(config.SPEED)
        if not config.SORTING:
                return -1
        if compare.value <= pivot.value:
            i = i+1
            # compare.change_color(config.RED)
            # increment index of smaller element
            compare.change_color(config.RED)
            pivot.change_color(config.RED)
            time.sleep(config.SPEED)
            pivot.change_color(config.PURPLE)
            compare.change_color(config.YELLOW)
            if i != j:
                arr[i].change_color(config.YELLOW)
                time.sleep(config.SPEED)
                arr[i].change_color(config.RED)
                compare.change_color(config.RED)
                time.sleep(config.SPEED)
                bar_chart.swap_positions(i, j)
                time.sleep(config.SPEED)
                arr[j].change_color(config.YELLOW)
                arr[i].change_color(config.YELLOW)
                time.sleep(config.SPEED)
                arr[j].change_color(config.WHITE)
                arr[i].change_color(config.WHITE)
            else:
                time.sleep(config.SPEED)
            
        compare.change_color(old_compare_color)
 
    pivot.change_color(config.YELLOW)
    time.sleep(config.SPEED)
    if i+1 != high:
        arr[i+1].change_color(config.YELLOW)
        time.sleep(config.SPEED)
        pivot.change_color(config.RED)
        arr[i+1].change_color(config.RED)
        time.sleep(config.SPEED)
        bar_chart.swap_positions(i+1, high)
        time.sleep(config.SPEED)
        arr[high].change_color(config.WHITE)
        pivot.change_color(config.PURPLE)
        time.sleep(config.SPEED)
        

    return (i+1)
  
def quickSort(bar_chart, low, high):
    arr = bar_chart.bars
    if len(arr) == 1:
        return arr
    if low < high:
        if not config.SORTING:
            return
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(bar_chart, low, high)
        if pi == -1:
            return
        arr[pi].change_color(config.GREEN)
        time.sleep(config.SPEED)
 
        # Separately sort elements before
        # partition and after partition
        quickSort(bar_chart, low, pi-1)
        quickSort(bar_chart, pi+1, high)
    elif low == high:
        arr[low].change_color(config.PURPLE)
        time.sleep(config.SPEED)
        arr[low].change_color(config.GREEN)
        time.sleep(config.SPEED)

def quick_sort_vis(bar_chart):
    """Quick sort visualization for a bar chart.

    Args:
        bar_chart: Bar chart to be sorted
    """
    bar_chart.mutex.acquire()
    quickSort(bar_chart, 0, len(bar_chart.bars)-1)
    bar_chart.mutex.release()