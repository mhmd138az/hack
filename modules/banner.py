from colorama import Fore, Style
import platform, os

OsName = platform.uname()[0]

def banner():
    if OsName == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    
    print(Fore.LIGHTCYAN_EX + "  __  __    _      _    __  __   _____  ")
    print(Fore.LIGHTCYAN_EX + " |  \/  |  | |    | |  |  \/  | ||    ||   ")
    print(Fore.LIGHTCYAN_EX + " | \  / |  | |____| |  | \  / | || ___ ||  ")
    print(Fore.LIGHTCYAN_EX + " | |\/| |  | |____| |  | |\/| | |||___|||  ")
    print(Fore.LIGHTCYAN_EX + " | |  | |  | |    | |  | |  | | ||     ||  ")
    print(Fore.LIGHTCYAN_EX + " |_|  |_|  |_|    |_|  |_|  |_| ||____||   ")
    print(Fore.LIGHTCYAN_EX + "                            ")
    print(Fore.LIGHTCYAN_EX + "         ERROR              ")
    
    print(Style.RESET_ALL)

banner()
