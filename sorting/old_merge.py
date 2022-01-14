import time
import resources.config as config

# This file contains a version of in-place merge
# sort where sub-arrays were merged with insertion sort
def merge(bar_chart, start, mid, end):
    finalStart = start
    finalEnd = end
    start2 = mid + 1
    arr = bar_chart.bars

    l = arr[mid]
    r = arr[start2]
    c1, c2 = arr[mid].color, arr[start2].color
    l.change_color(config.YELLOW)
    r.change_color(config.YELLOW)
    time.sleep(config.SPEED)
    l.change_color(config.WHITE)
    r.change_color(config.WHITE)
    
    # If the direct merge is already sorted
    if (arr[mid].value <= arr[start2].value ):
        print("p1")
        return
        
    # Two pointers to maintain start
    # of both arrays to merge
    else:
        while (start <= mid and start2 <= end):
            startBar = arr[start]
            if not config.SORTING:
                return
            # If element 1 is in right place
            if (arr[start].value <= arr[start2].value):
                col1, col2 = arr[start].color, arr[start2].color
                arr[start].change_color(config.YELLOW)
                arr[start2].change_color(config.YELLOW)
                time.sleep(config.SPEED)
                arr[start].change_color(col1)
                arr[start2].change_color(col2)
                if finalStart == 0 and finalEnd == len(arr)-1:
                    arr[start].change_color(config.GREEN)    
                start += 1
                print("p2")
            else:
                value = arr[start2].value
                index = start2
                # Shift all the elements between element 1
                # element 2, right by 1.
                while (index != start):
                    c1, c2 = arr[index].color, arr[index-1].color
                    arr[index].change_color(config.RED)
                    arr[index-1].change_color(config.RED)
                    time.sleep(config.SPEED)
                    bar_chart.swap_positions(index, index-1)
                    time.sleep(config.SPEED)
                    arr[index].change_color(c2)
                    arr[index-1].change_color(c1)
                   
                    index -= 1
                    print("p3")
                if finalStart == 0 and finalEnd == len(arr)-1:
                   arr[start].change_color(config.GREEN) 
                   print("True")           
                # Update all the pointers
                start += 1
                mid += 1
                start2 += 1
 
    
def _merge_sort_vis(bar_chart, l, r):
    if (l < r):
 
        # Same as (l + r) / 2, but avoids overflow
        # for large l and r
        m = l + (r - l) // 2
 
        # Sort first and second halves
        _merge_sort_vis(bar_chart, l, m)
        _merge_sort_vis(bar_chart, m + 1, r)
        if not config.SORTING:
            return

        merge(bar_chart, l, m, r) 
        
def merge_sort_vis_old(bar_chart):
    _merge_sort_vis(bar_chart, 0, len(bar_chart.bars)-1)