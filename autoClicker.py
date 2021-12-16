# importing time and threading
import time
import threading
from pynput.mouse import Button, Controller 

# pynput.keyboard is used to watch events of
# keyboard for start and stop of auto-clicker
from pynput.keyboard import KeyCode
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener

# four variables are created to
# control the auto-clicker
delay = 1
button = Button.left
start_stop_key = KeyCode(char='a')
stop_key = KeyCode(char='b')

# threading.Thread is used
# to control clicks
class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

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
                for clickPos in mouseClicks:
                    mouse.position = clickPos
                    mouse.click(self.button)
                    if mouseClicks == mouseClicks.__len__:
                        count = 0
                    else:
                        count = count + 1
                        print(count)
                # if count == 0:
                #     mouse.position = mouseClicks[0]
                #     mouse.click(self.button)
                #     count = count + 1
                # elif count == 1:
                #     mouse.position = mouseClicks[1]
                #     mouse.click(self.button)
                #     count = count + 1
                # elif count == 2:
                #     mouse.position = mouseClicks[2]
                #     mouse.click(self.button)
                #     count = count + 1
                #     time.sleep(1)
                # elif count == 3:
                #     mouse.position = mouseClicks[3]
                #     mouse.click(self.button)
                #     count = 0
                time.sleep(self.delay)
                time.sleep(0.1)

def on_click(x, y, button, pressed):
    if pressed:
        # print(x,y)
        mouseClicks.append((x,y))

# on_press method takes
# key as argument
def on_press(key):
	
# start_stop_key will stop clicking
# if running flag is set to true
	if key == start_stop_key:
		if click_thread.running:
			click_thread.stop_clicking()
		else:
			click_thread.start_clicking()
			
	# here exit method is called and when
	# key is pressed it terminates auto clicker
	elif key == stop_key:
		click_thread.exit()
		keyboard_listener.stop()
		mouse_listener.stop()

# with KeyCodeListener(on_press=on_press) as listener:
# 	listener.join()

# with MouseListener(on_click=on_click) as ls:
#     ls.join()

keyboard_listener = KeyboardListener(on_press=on_press)
mouse_listener = MouseListener(on_click=on_click)

keyboard_listener.start()
mouse_listener.start()
# keyboard_listener.join()
# mouse_listener.join()

# instance of mouse controller is created
mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()
mouseClicks = []
