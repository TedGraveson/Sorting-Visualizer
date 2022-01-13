import resources.config as config
import time
import math

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
        if not config.SORTING:
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
    
    
    
