#Note that you will have to download and install pynput for this to work
from pynput.mouse import Listener
import logging

logging.basicConfig(filename="Mouse_log.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

def on_move(x, y):
    logging.info ("Mouse moved to ({1}, {0})".format(x, y))

def on_click(x, y, button, pressed):
    if pressed:
    logging.info ("Mouse clicked at ({1}, {0}) with {2}".format(x, y, button))

def on_scroll(x, y, dx, dy):
    logging.info ("Mouse scrolled at ({0}, {1})({2}, {3})".format(x, y, dx, dy))
    
with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    Listener.join()
