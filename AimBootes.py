import pyautogui as pa
import time 
import keyboard
import win32api
import win32con

"""
Não esquece de baixar os pacotes, use um ambiente virtual.

Você pode mudar as posições "region" usando o codigo "displayMousePosition()"
abaixo, pode variar de acordo com a resolução de seu monitor.
Só clicar no play e ver a evolução do código, por favor melhore ele para brincar.
Essa é o minha primeira vez usando o pyautogui então por isso há no que melhorar :) .
"""

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


while keyboard.is_pressed('c')== False:
    print("Comoçou a correr")
    sc = pa.screenshot(region=(275,470,800,560))
    width,height = sc.size


    for x in range(0, width,12):
        achou = 0
        for y in range(0, height,12):
            r,g,b = sc.getpixel((x,y))
            #print(r,g,b)

            if r == 255 and b == 195:
                achou = 1
                click(275+x,470+y)
                time.sleep(0.05)
                break
        if achou ==1:
            break





"""
while True:
    pa.displayMousePosition()

"""
sc = pa.screenshot(region=(275,470,800,560))

sc.save('AimBooster.png')
