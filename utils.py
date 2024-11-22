import time
from colorama import init, Fore, Style

# init(autoreset=True) why autoreset
init()

def print_animation(text, delay=0.02, color=Fore.GREEN):
    """

    :param text:
    :param delay:
    :param color:
    """
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL)