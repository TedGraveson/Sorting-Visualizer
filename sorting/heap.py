import resources.config as config
import time
def heapify(bar_chart, n, i):
    
    arr =bar_chart.bars
    
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    current, c_old_color = arr[largest], arr[largest].color
    # current.change_color(config.YELLOW)
    # See if left child of root exists and is
    # greater than root
    if not config.SORTING:
        return
    
    if l < n and arr[largest].value < arr[l].value:
        lbar, l_old_color = arr[l], arr[l].color
        lbar.change_color(config.YELLOW)
        time.sleep(config.SPEED)
        largest = l
        lbar.change_color(l_old_color)

    # See if right child of root exists and is
    # greater than root
    
    if r < n and arr[largest].value < arr[r].value:
        rbar, r_old_color = arr[r], arr[r].color
        rbar.change_color(config.YELLOW)
        time.sleep(config.SPEED)
        # current.change_color(config.RED)
        # rbar.change_color(config.RED)
        time.sleep(config.SPEED)
        largest = r
        # current.change_color(old_color)
        
        rbar.change_color(r_old_color)
        
    # Change root, if needed
    if largest != i:
        time.sleep(config.SPEED)
        bar_chart.swap_positions(i, largest)
        time.sleep(config.SPEED)
        current.change_color(c_old_color)
        # Heapify the root.
        heapify(bar_chart, n, largest)
    


def heap_sort_vis(bar_chart):
    arr =bar_chart.bars
    n = len(arr)

    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(bar_chart, n, i)

    # One by one extract elements
    for i in range(n-1, -1, -1):
        time.sleep(config.SPEED)
        bar_chart.swap_positions(i, 0)
        time.sleep(config.SPEED)
        bar_chart.bars[i].change_color(config.GREEN)
        #arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(bar_chart, i, 0)
