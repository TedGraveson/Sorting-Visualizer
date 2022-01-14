import resources.config as config
import time
def heapify(bar_chart, n, i):
    if not config.SORTING:
        return
    
    arr = bar_chart.bars
    
    lbar, rbar = None, None
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    root = arr[largest]
    current = root
    current.change_color(config.RED)
    
    if l < n:
        lbar = arr[l]
        lbar.change_color(config.YELLOW)
    if r < n:
        rbar = arr[r]
        rbar.change_color(config.YELLOW)
        
    time.sleep(config.SPEED)
    
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest].value < arr[l].value:        
        largest = l
        current = lbar
        

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest].value < arr[r].value:
        largest = r
        current = rbar
        
    # Change root, if needed
    if largest != i:
        current.change_color(config.RED)
        time.sleep(config.SPEED)
        bar_chart.swap_positions(i, largest)
        time.sleep(config.SPEED)
        arr[largest].change_color(config.YELLOW)
        time.sleep(config.SPEED)
        
    if lbar is not None:
        lbar.change_color(config.WHITE)
    if rbar is not None:
        rbar.change_color(config.WHITE)
    root.change_color(config.WHITE)
    
    if largest != i:  
        # Heapify the root.
        heapify(bar_chart, n, largest)


def heap_sort_vis(bar_chart):
    bar_chart.mutex.acquire()
    arr =bar_chart.bars
    n = len(arr)

    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        if not config.SORTING:
            return
        heapify(bar_chart, n, i)

    # One by one extract elements
    for i in range(n-1, -1, -1):
        if not config.SORTING:
            return
        arr[0].change_color(config.YELLOW)
        arr[i].change_color(config.YELLOW)
        time.sleep(config.SPEED)
        arr[0].change_color(config.RED)
        arr[i].change_color(config.RED)
        time.sleep(config.SPEED)
        bar_chart.swap_positions(i, 0)
        time.sleep(config.SPEED)
        arr[i].change_color(config.GREEN)
        if i != 0:
            arr[0].change_color(config.WHITE)
            time.sleep(config.SPEED)
            heapify(bar_chart, i, 0)
    bar_chart.mutex.release()
