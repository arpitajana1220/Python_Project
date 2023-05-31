"""
When we want some creative outputs, some fun colorful displays.
Colorama is just the right library to acheive that !
Using this library we can customize our outputs with different colours as demonstarted below 
"""
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print(Fore.BLUE+Back.YELLOW+"Hi My name is Arpita Jana"+ Fore.YELLOW+ Back.BLUE+"I am Senior Data Engineer")
print(Back.CYAN+"I help people to boost their career in Tech")
print(Fore.RED + Back.GREEN+ "Continuously learning and growing")