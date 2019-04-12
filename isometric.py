# This will only work on PC's having screen size 1920 X 1080.


import pyautogui
from time import sleep
#Open ms paint,maximise the window and extend the drawing space to full area. 
#Open the terminal in front but not in full screen.
#Place the cursor anywhere in paint but not on terminal.
#Run the file in terminal.
pyautogui.click() #click to put paint in focus
pyautogui.click(442,76)#to select the straight line tool
delta_x=298
delta_y=136
x=537
y=466
pyautogui.doubleClick(x,y)
pyautogui.dragRel(delta_x,delta_y,duration=0.25)
centre_x=825
centre_y=451 # centre_x and centre_y are for random clicks in order to remove cursor from previous line and draw a new one
pyautogui.click(centre_x,centre_y)
pyautogui.doubleClick(x+delta_x,y+delta_y)
pyautogui.dragRel(delta_x,-delta_y,duration=0.25)
pyautogui.click(centre_x,centre_y)
pyautogui.doubleClick(x+ 2*delta_x, y)
pyautogui.dragRel(-delta_x,-delta_y, duration=0.25)
pyautogui.click(centre_x,centre_y)
pyautogui.doubleClick(x+delta_x,y-delta_y)
pyautogui.dragRel(-delta_x,delta_y)
# this concludes the top view,now we will draw the bottom portion
pyautogui.click(centre_x,centre_y)
a=340
pyautogui.doubleClick(x,y)
pyautogui.dragRel(0,a,duration=0.25)
pyautogui.click(centre_x,centre_y)
pyautogui.doubleClick(x,y+a)
pyautogui.dragRel(delta_x,delta_y,duration=0.25)
pyautogui.click(centre_x,centre_y)
pyautogui.doubleClick(x+delta_x,y+delta_y)
pyautogui.dragRel(0,a,duration=0.25)
pyautogui.click(centre_x,centre_y)
pyautogui.doubleClick(x+2*delta_x,y)
pyautogui.dragRel(0,a,duration=0.25)
pyautogui.click(centre_x,centre_y)
pyautogui.doubleClick(x+delta_x,y+delta_y+a)
pyautogui.dragRel(delta_x,-delta_y,duration=0.25)

