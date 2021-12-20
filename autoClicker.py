import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import KeyCode
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener

# threading.Thread is used
class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.start_self.stop_key = KeyCode(char='a')
        self.stop_key = KeyCode(char='b')
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

        self.keyboard_listener = KeyboardListener(on_press=self.on_press)
        self.mouse_listener = MouseListener(on_click=self.on_click)

        self.keyboard_listener.start()
        self.mouse_listener.start()
        self.mouse = Controller()
        self.mouseClicks = []
        # self.keyboard_listener.join()
        # self.mouse_listener.join()

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        count = 0
        while self.program_running:
            while self.running:
                for clickPos in self.mouseClicks:
                    self.mouse.position = clickPos
                    self.mouse.click(self.button)
                    print(clickPos)
                    if clickPos == self.mouseClicks[self.mouseClicks.__len__() - 1]:
                        count = 0
                    else:
                        count = count + 1
                    time.sleep(self.delay)
                    time.sleep(1)

    def on_click(self,x, y, button, pressed):
        if pressed:
            self.mouseClicks.append((x,y))

    def on_press(self,key):
        if key == self.start_self.stop_key:
            if click_thread.running:
                click_thread.stop_clicking()
            else:
                click_thread.start_clicking()
        elif key == self.stop_key:
            click_thread.exit()

click_thread = ClickMouse(1, Button.left)
click_thread.start()