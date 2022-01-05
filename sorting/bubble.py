import resources.config as config
import time

def bubble_sort_vis(bar_chart):  
    # Traverse through all array elements
    bar_chart.mutex.acquire()
    for i in range(len(bar_chart.bars)):
    # range(n) also work but outer loop will repeat one time more than needed.
        # current.change_color(constants.RED)
        for j in range(len(bar_chart.bars)-1, i, -1):
            
            if not config.SORTING:
                bar_chart.mutex.release()
                return 
            
            bar_chart.bars[j].change_color(config.YELLOW)
            bar_chart.bars[j-1].change_color(config.YELLOW)
            time.sleep(config.SPEED)
            if bar_chart.bars[j].value < bar_chart.bars[j - 1].value:
                bar_chart.bars[j].change_color(config.RED)
                bar_chart.bars[j-1].change_color(config.RED)
                time.sleep(config.SPEED)
                bar_chart.swap_positions(j, j-1)
                time.sleep(config.SPEED)
                bar_chart.bars[j].change_color(config.YELLOW)
                bar_chart.bars[j-1].change_color(config.YELLOW)
                time.sleep(config.SPEED)

            bar_chart.bars[j].change_color((config.WHITE))
            bar_chart.bars[j-1].change_color((config.WHITE))
            
        bar_chart.bars[i].change_color(config.GREEN)
        time.sleep(config.SPEED)
        
    bar_chart.mutex.release()