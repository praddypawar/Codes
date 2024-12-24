#sudo apt-get install python3-tk python3-dev
#Python 3.8.10

import pyautogui
import random
import time
import string

def random_mouse_movement():
    screen_width, screen_height = pyautogui.size()
    x = random.randint(0, screen_width - 1)
    y = random.randint(0, screen_height - 1)
    pyautogui.moveTo(x, y, duration=random.uniform(0.1, 1))

def random_click():
    if random.choice([True, False]):
        pyautogui.click()
    else:
        pyautogui.click(button='right')

def random_keyboard_typing():
    random_text = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(3, 10)))
    pyautogui.write(random_text, interval=random.uniform(0.1, 0.3))

def random_tab_change():
    # Simulate an Alt+Tab event to switch between applications
    pyautogui.hotkey('alt', 'tab')

def random_event():
    event = random.choice([random_mouse_movement])
    event()

def main():
    while True:
        random_event()
        # Sleep for a random time between 5 to 15 seconds
        time.sleep(random.randint(10, 25))

if __name__ == '__main__':
    main()
