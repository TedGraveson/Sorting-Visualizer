import resources.config as config
import time

def insertion_sort_vis(bar_chart):
    """Insertion sort visualiztion for a bar chart.

    Args:
        bar_chart: Bar chart to be sorted
    """
    bar_chart.mutex.acquire()
    
    bars = bar_chart.bars
    
    # Animate first bar
    current = bar_chart.bars[0]
    current.change_color(config.RED)
    time.sleep(config.SPEED)
    current.change_color(config.GREEN)
    time.sleep(config.SPEED)
    # Traverse through 1 to len(arr)
    for i in range(1, len(bars)):
  
        key = bars[i].value
  
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        
        current = bar_chart.bars[i]
        while j >= 0:
            
            if not config.SORTING:
                bar_chart.mutex.release()
                return 
            compare = bar_chart.bars[j]
            old_color = compare.color
            current.change_color(config.YELLOW)
            compare.change_color(config.YELLOW)
            time.sleep(config.SPEED)
            if key < bars[j].value:            
                current.change_color(config.RED)
                compare.change_color(config.RED)
                time.sleep(config.SPEED)
                bar_chart.swap_positions(j+1, j)
                time.sleep(config.SPEED)
                current.change_color(config.YELLOW)
                compare.change_color(config.YELLOW)
                time.sleep(config.SPEED)
                compare.change_color(old_color)
                j -= 1
            else:
                compare.change_color(old_color)
                break
                      

        current.change_color(config.GREEN)
        time.sleep(config.SPEED)
        
    bar_chart.mutex.release()