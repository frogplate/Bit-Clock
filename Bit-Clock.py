from microbit import *

BIT_BRIGHT = 9
BACK_BRIGHT = 3
SECS_BRIGHT = 6

display.clear()
start_time = running_time()
base_hrs = 12
base_mins = 34
last_min = -1
last_sec = -1

def display_binary(col, value):
    
    if value in [1, 3, 5, 7, 9]:
        display.set_pixel(col, 3, BIT_BRIGHT)
        
    if value in [2, 3, 6, 7]:
        display.set_pixel(col, 2, BIT_BRIGHT)

    if value in [4, 5, 6, 7]:
        display.set_pixel(col, 1, BIT_BRIGHT)
        
    if value in [8, 9]:
        display.set_pixel(col, 0, BIT_BRIGHT)

def draw_background():
    display.clear()
    for x in range(5):
        display.set_pixel(x, 4, BACK_BRIGHT)

def refresh_display(hrs_tens, hrs_units, min_tens, min_units):
    draw_background()
    display_binary(0, hrs_tens)
    display_binary(1, hrs_units)
    display_binary(3, min_tens)
    display_binary(4, min_units)

def invert_secs():
    if display.get_pixel(2, 2) > 0:
        display.set_pixel(2, 2, 0)
    else:
        display.set_pixel(2, 2, SECS_BRIGHT)
        
while True:
    
    # Button A increments the hours
    if button_a.was_pressed():
        base_hrs = base_hrs + 1
        if base_hrs > 23:
            base_hrs = 0
        # Force display update
        last_min = -1

    # Button B increments the minutes
    if button_b.was_pressed():
        base_mins = base_mins + 1
        if base_mins > 59:
            base_mins = 0
        # Force display update
        last_min = -1
        
    run_secs = int((running_time() - start_time) / 1000)

    run_hrs = run_secs / 3600 + base_hrs + base_mins / 60

    run_mins = int((run_hrs - int(run_hrs)) * 60)
    run_hrs = int(run_hrs) % 24
  
    hrs_tens  = int(run_hrs / 10)
    hrs_units = run_hrs - 10 * hrs_tens
    min_tens  = int(run_mins / 10)
    min_units = run_mins - 10 * min_tens

    if last_min != min_units:  
        refresh_display(hrs_tens, hrs_units, min_tens, min_units)
        last_min = min_units

    if last_sec != run_secs:
        invert_secs()
        last_sec = run_secs
