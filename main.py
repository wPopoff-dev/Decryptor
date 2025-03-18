import colorama
import os
from colorama import Fore, Style

os.system('cls' if os.name == 'nt' else 'clear')

colorama.init()

print(Fore.RED + """
                            _____                              _             
                            |  __ \                           | |            
                            | |  | | ___  ___ _ __ _   _ _ __ | |_ ___  _ __ 
                            | |  | |/ _ \/ __| '__| | | | '_ \| __/ _ \| '__|
                            | |__| |  __/ (__| |  | |_| | |_) | || (_) | |   
                            |_____/ \___|\___|_|   \__, | .__/ \__\___/|_|   
                                                    __/ | |                  
                                                    |___|_|                 
""" + Style.RESET_ALL)

# Espacios en blanco
print()
print()

# Enlace en azul
print(Fore.RED + "                                 https://discord.gg/vDJgT2pVfK" + Style.RESET_ALL)

print(      Fore.LIGHTWHITE_EX + "                      Nota " + Fore.CYAN + "Con esta herramienta puedes desifrar hashes. Usarla bajo cuidado")


print(Fore.WHITE + "                                                |-------------------------------|")
print(Fore.YELLOW + "                                                       (1) " + Fore.WHITE + "Decrypt Hashes")
print(Fore.YELLOW + "                                                       (2) " + Fore.WHITE + "Wordlist Load")
print(Fore.YELLOW + "                                                       (3) " + Fore.WHITE + "Close Decrypt")
print(Fore.WHITE + "                                                |-------------------------------|")


print()
print()
print()
print()
print()
opcion = input(Fore.RED + "                 root@CheatingX:-> ")