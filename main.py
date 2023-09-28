dir = "C:\\Users\\\DOLPHIN\\Downloads\\a.txt"   
import mouse

with open(dir, 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        a, b, c = line.split('-')
        print(a,b,c)
        if(c == 0):
            mouse.click(button='left')

