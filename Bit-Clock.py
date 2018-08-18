from microbit import *

display.clear()
start_time = running_time()
base_hrs = 23
base_mins = 44
last = 0

def binary(col, value):
    if value in [1, 3, 5, 7, 9]:
        display.set_pixel(col, 3, 9)
        
    if value in [2, 3, 6, 7]:
        display.set_pixel(col, 2, 9)

    if value in [4, 5, 6, 7]:
        display.set_pixel(col, 1, 9)
        
    if value in [6, 7]:
        display.set_pixel(col, 2, 9)
        
    if value in [8, 9]:
        display.set_pixel(col, 0, 9)

while True:
    run_secs = int((running_time() - start_time) / 1000)

    run_hrs = run_secs / 3600 + base_hrs + base_mins / 60

    run_mins = int((run_hrs - int(run_hrs)) * 60)
    run_hrs = int(run_hrs) % 24
  
    col1 = int(run_hrs / 10)
    col2 = run_hrs - 10 * col1
    col4 = int(run_mins / 10)
    col5 = run_mins - 10 * col4

    if last != col5:  
        display.clear()
        binary(0, col1)
        binary(1, col2)
        binary(3, col4)
        binary(4, col5)
        last = col5
