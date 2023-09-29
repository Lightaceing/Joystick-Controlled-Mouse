dir = "C:\\Users\\\DOLPHIN\\Downloads\\a.txt"

import mouse
import time

#screens resolution |1366 x 768| is |pixel|

def change_x(x, current_pos_x):
    
    x_change = current_pos_x
    if x < 429:
    #change pos to left
        x_change = current_pos_x - 20
    if x_change < 0:
        pass
    elif x > 434:
    #change pos to right
        x_change = current_pos_x + 20
    if x_change < 0:
        pass
    return x_change
 
def change_y(y, current_pos_y):
        
        y_change = current_pos_y
        if y < 460:
        #change pos to left
            y_change = current_pos_y - 20
        if y_change < 0:
            pass
        elif y > 468:
        #change pos to right
            y_change = current_pos_y + 20
        if y_change < 0:
            pass
        return y_change

#calculates cursor movement and then moves the cursor
def move_cursor(x, y):

    current_pos_x, current_pos_y = mouse.get_position()

    #x pos | 429 - 434 |
    x_change = change_x(x, current_pos_x)
    
    #y pos | 460 - 468 |
    y_change = change_y(y, current_pos_y)
    
    #final mov
    mouse.move(x_change, y_change, absolute=True, duration=0)
    
    #delay
    time.sleep(0.09)#good for now

#reads file
with open(dir, 'r') as file:
    #have to clear the txt file once 
    while True:
        line = file.readline()
        if not line:
            break
        a, b, c = line.split('-')
        move_cursor(int(a), int(b))
