import time
from colorama import init, Fore, Style

init(autoreset=True)

def print_animation(text, delay=0.02, color=Fore.GREEN):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL)