import termcolor
import random
import time, datetime
import sys, os
from colorama import init
from termcolor import colored

def clear():
    if sys.platform == 'win32':
        return os.system('cls')
    else:
        return os.system('clear')

colors = [
        'red',
        'green',
        'yellow',
        'blue',
        'magenta',
        'cyan',
        'white']

name = [
    'H','O','R','N',' ','O','K',' ','P','L','E','A','S','E'
]
init()
while True:
    print('to exit use a keyboard interrupt (ctrl+c)')
    i = 0
    string = ''
    while(i<len(name)):
        string+=termcolor.colored(name[i], colors[random.randint(0,len(colors)-1)])
        i+=1
    print(string)
    time.sleep(0.2)
    clear()