import pyautogui as pg
import time
pg.hotkey('ctrl','winleft','d')
pg.hotkey('winleft')
pg.typewrite('chrome\n',0.5)
pg.hotkey('winleft','up')
pg.typewrite('netflix.com\n',0.5)
time.sleep(5)
pg.hotkey('tab')
time.sleep(0.2)
pg.hotkey('tab')
time.sleep(0.2)
pg.hotkey('enter')
time.sleep(5)
pg.hotkey('tab')
time.sleep(0.2)
pg.typewrite('caroline_shen@yahoo.com')
pg.hotkey('tab')
time.sleep(0.2)
pg.password
pw = pg.password('Enter your password','password box','','*')
pg.hotkey('tab')
time.sleep(0.2)
pg.typewrite(pw,0.2)
pw = ""
pg.hotkey('enter')
