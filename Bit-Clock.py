from microbit import *

BIT_BRIGHT = 9

display.clear()
start_time = running_time()
base_hrs = 23
base_mins = 44
last = 0

def display_binary(col, value):
    
    if value in [1, 3, 5, 7, 9]:
        display.set_pixel(col, 3, BIT_BRIGHT)
        
    if value in [2, 3, 6, 7]:
        display.set_pixel(col, 2, BIT_BRIGHT)

    if value in [4, 5, 6, 7]:
        display.set_pixel(col, 1, BIT_BRIGHT)
        
    if value in [8, 9]:
        display.set_pixel(col, 0, BIT_BRIGHT)

while True:
    run_secs = int((running_time() - start_time) / 1000)

    run_hrs = run_secs / 3600 + base_hrs + base_mins / 60

    run_mins = int((run_hrs - int(run_hrs)) * 60)
    run_hrs = int(run_hrs) % 24
  
    hrs_tens_value = int(run_hrs / 10)
    hrs_unit_value = run_hrs - 10 * hrs_tens_value
    min_tens_value = int(run_mins / 10)
    min_unit_value = run_mins - 10 * min_tens_value

    if last != min_unit_value:  
        display.clear()
        display_binary(0, hrs_tens_value)
        display_binary(1, hrs_unit_value)
        display_binary(3, min_tens_value)
        display_binary(4, min_unit_value)
        last = min_unit_value
