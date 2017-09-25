#!/usr/bin/env python
# title           :pyheader.py
# description     :This will create a header for a python script.
# author          :Gabriel Ionescu
# date            :2017/09/21
# version         :1.1.0
# notes           :pycharm is not starting
# python_version  :3.6
# ==============================================================================

# Import the modules needed to run the script.
from os.path import exists
from time import strftime
import os
import platform


def clear_screen(system):
    """Clear the screen (windows or linux)"""
    
    if system == 'windows':
        os.system('cls')
    elif system == 'linux':
        os.system('clear')


def check_title():
    """Ask for a title name and check if is available"""

    title = input('Enter a title for your script: ')

    # Convert title to a proper filename.
    title = title.lower()
    title = title.replace(' ', '_')
    title = title + '.py'

    # Check to see if the file exists.
    if exists(title):
        print('\nA script with this name already exists.')
        print('1. Try another name')
        print('2. Exit')
        again = input()
        
        if again == '1':
            clear_screen(system)
            title = check_title()
        else:
            raise SystemExit
    return title


def main():
    """"""
    
    # Collect the data.
    descrpt = input('Enter a description for your script: ')
    name = 'Gabriel Ionescu'
    date = strftime('%Y/%m/%d')
    ver = '1.0'
    python_ver = platform.python_version()
    div = '===================================='

    # Create a file
    filename = open(title, 'w')

    # Write the data to the file. 
    filename.write('#!/usr/bin/python')
    filename.write('\n# title          :' + title)
    filename.write('\n# description    :' + descrpt)
    filename.write('\n# author         :' + name)
    filename.write('\n# date           :' + date)
    filename.write('\n# version        :' + ver)
    filename.write('\n# notes          :')
    filename.write('\n# python_version :' + python_ver)
    filename.write('\n# ' + div * 2 + '\n')
    filename.write('\n')
    filename.write('\n')

    # Close the file after writing to it.
    filename.close()


def select_editor():
    """Open the file with either the IDLE (windows) or Vim editor."""

    if system == 'windows':        
        path = os.getcwd()
        clear_screen(system)
        while True:
            print('Please select your prefered editor:\n')
            print('1. IDLE')
            print('2. Notepad++')
            print('3. PyCharm')
            print('4. Atom')
            print('0. exit')
            option = input()
            if option == '1':
                os.system(r'c:\Python36-32\Lib\idlelib\idle '
                          + path + '\\' + title)
                exit()
            elif option == '2':
                os.system('START notepad++ '
                          + path + '\\' + title)
                exit()
            elif option == '3':
                os.system(r'"C:\Program Files\JetBrains\PyCharm Community Edition 2017.2.1\bin\pycharm64.exe" '
                          + path + '\\' + title)
                exit()
            elif option == '4':
                os.system(r'C:\Users\iones\AppData\Local\atom\atom.exe '
                          + path + '\\' + title)
                exit()
            elif option == '0':
                exit()
    elif system ==  'linux':
        clear_screen(system)
        while True:
            print('Please select your prefered editor:\n')
            print('1. vim')
            print('2. gedit')
            print('3. nano')
            print('0. exit')
            option = input()
            if option == '1':
                os.system('vim +12 ' + title)
                exit()
            elif option == '2':
                os.system('gedit +12 ' + title)
                exit()
            elif option == '3':
                os.system('nano +12 ' + title)
                exit()
            elif option == '0':
                exit()
    return select_editor()


if __name__ == "__main__":
    system = platform.system().lower()
    clear_screen(system)
    title = check_title()
    main()
    select_editor()
