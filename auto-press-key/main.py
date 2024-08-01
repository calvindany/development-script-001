import pyautogui
import time
import random

# Function to press either "P" or "Q" followed by Space
def press_key_sequence():
    # Choose randomly between "P" and "Q"
    key = random.choice(['p', 'q'])
    
    # Press the chosen key
    pyautogui.press(key)
    # Press the Space key
    pyautogui.press('space')

# Give a delay to switch to the window where you want to press the keys
time.sleep(3)

# Define how many times you want to repeat the sequence
repetitions = 2000

for _ in range(repetitions):
    press_key_sequence()
    time.sleep(0.01)  # Adjust the sleep time as needed

print("Key press sequence completed.")
