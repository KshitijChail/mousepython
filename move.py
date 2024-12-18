import pyautogui
import time
import random

def move_and_click(interval=5, click=True):
    """
    Moves the mouse to a random position and optionally clicks.

    :param interval: Time in seconds between movements.
    :param click: Whether to perform a mouse click after moving.
    """
    try:
        print("Starting mouse movement. Press Ctrl+C to stop.")
        while True:
            # Get screen size
            screen_width, screen_height = pyautogui.size()

            # Generate random coordinates within the screen bounds
            x = random.randint(0, screen_width - 1)
            y = random.randint(0, screen_height - 1)

            # Move the mouse to the random position
            pyautogui.moveTo(x, y, duration=0.5)  # Smooth movement over 0.5 seconds
            print(f"Moved to ({x}, {y})")

            # Optionally click at the new position
            if click:
                pyautogui.click()
                print("Mouse clicked.")

            # Wait for the specified interval
            time.sleep(interval)

    except KeyboardInterrupt:
        print("Mouse movement stopped.")

if __name__ == "__main__":
    # Customize the interval and click behavior if needed
    move_and_click(interval=5, click=True)
