# import sys this is useless
from colorama import init, Fore, Style
from functions import function1, function2, api_function, data_handler, logger
from utils import print_animation

# init(autoreset=True) # why autoreset
init()

def display_image():
    image = """
    ██████╗ ██╗   ██╗██████╗ ███████╗███████╗███████╗
    ██╔══██╗██║   ██║██╔══██╗██╔════╝██╔════╝██╔════╝
    ██████╔╝██║   ██║██████╔╝█████╗  █████╗  ███████╗
    ██╔═══╝ ██║   ██║██╔═══╝ ██╔══╝  ██╔══╝  ╚════██║
    ██║     ╚██████╔╝██║     ███████╗███████╗███████║
    ╚═╝      ╚═════╝ ╚═╝     ╚══════╝╚══════╝╚══════╝
    """
    print(image)

def display_menu():
    print_animation("==============================", color=Fore.CYAN + Style.BRIGHT)
    print_animation("      PYTHON PROJECT MENU      ", color=Fore.CYAN + Style.BRIGHT)
    print_animation("==============================\n", color=Fore.CYAN + Style.BRIGHT)
    print_animation("1. Function 1 Description", color=Fore.YELLOW)
    print_animation("2. Function 2 Description", color=Fore.YELLOW)
    print_animation("3. API Function", color=Fore.YELLOW)
    print_animation("4. Display Data", color=Fore.YELLOW)
    print_animation("5. Exit\n", color=Fore.YELLOW)

def main():
    while True:
        display_image()
        display_menu()
        choice = input(Fore.GREEN + "Enter your choice: ").strip()

        if choice.lower() == 'exit' or choice == '5':
            print_animation("Exiting the program. Goodbye!", color=Fore.MAGENTA)
            # sys.exit() # using sys here is not necessary you could have just used return which will automtically exit the code so importing sys would be avoidede
            return
        elif choice == '1':
            result = function1.perform_action()
            logger.log_action("Function1 executed", result)
        elif choice == '2':
            result = function2.perform_action()
            logger.log_action("Function2 executed", result)
        elif choice == '3':
            result = api_function.call_external_api()
            logger.log_action("API Function executed", result)
        elif choice == '4':
            data_handler.display_data()
        else:
            print_animation("Invalid choice. Please try again.", color=Fore.RED)
        input(Fore.BLUE + "Press Enter to return to the menu...")

if __name__ == "__main__":
    main()