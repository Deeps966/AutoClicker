import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import KeyCode
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener

# threading.Thread is used
class ClickMouse(threading.Thread):
    def __init__(self, delay):
        super(ClickMouse, self).__init__()
        self.start_stop_key = KeyCode(char='a')
        self.stop_key = KeyCode(char='b')
        self.delay = delay
        self.running = False
        self.program_running = True

        self.keyboard_listener = KeyboardListener(on_press=self.on_press)
        self.mouse_listener = MouseListener(on_click=self.on_click)

        self.keyboard_listener.start()
        self.mouse_listener.start()
        self.mouse = Controller()
        self.mouseClicks = []

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
                    if self.program_running and self.running:
                        self.mouse.position = clickPos['position']
                        self.mouse.click(clickPos['button'])
                        print(clickPos)
                        if clickPos == self.mouseClicks[self.mouseClicks.__len__() - 1]:
                            count = 0
                        else:
                            count = count + 1
                        time.sleep(self.delay)
                        time.sleep(0.1)

    def on_click(self,x, y, button, pressed):
        if pressed:
            self.mouseClicks.append({'position': (x,y), 'button': button})

    def on_press(self,key):
        if key == self.start_stop_key:
            if click_thread.running:
                click_thread.stop_clicking()
            else:
                click_thread.start_clicking()
        elif key == self.stop_key:
            click_thread.exit()

click_thread = ClickMouse(0.5)
click_thread.start()