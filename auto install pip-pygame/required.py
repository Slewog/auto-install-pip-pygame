#! /usr/bin/python3
import subprocess
import sys

# for /F "delims= " %i in ('pip3 list -o') do pip3 install -U %i
# for /F "delims= " %i in ('pip list --outdated --user') do pip install -U %i


class CheckRequiredModules:
    def __init__(self):
        self.pygame_is_installed = True
        self.tkinter_is_installed = True
        self.win32_error = "[EXCEPTION] Windows system operating is executing."
        self.modules_update_linux_1 = "python3 -m pip list -o > outdated"
        self.modules_update_linux_2= "for x in $(sed -n '3,$p' outdated | awk '{print $1}'); do python3 -m pip install -U $x; done"
        self.tkinter_install_linux = "sudo apt-get install python3-tk"  # "sudo apt-get remove python3-tk"
        self.tcl_install_linux = "sudo apt-get install tcl"  # " pip install Tcl"
        self.pip_update_linux = "python3 -m pip install -U pip"
        self.pip_install_linux = "sudo apt-get install python3-pip"
        self.pip_update_win32 = "python -m pip install -U pip"
        self.pip_install_win32 = "python get-pip.py"
        self.wheel_install_linux = "python3 -m pip install wheel"
        #self.wheel_update_linux = "python3 -m pip install wheel -U"
        self.wheel_install_win32 = "python -m pip install wheel"
        self.wheel_update_win32 = "python -m pip install wheel -U"
        self.setuptools_install_linux = "python3 -m pip install setuptools"
        #self.setuptools_update_linux = "python3 -m pip install setuptools -U"
        self.setuptools_install_win32 = "python -m pip install setuptools"
        self.setuptools_update_win32 = "python -m pip install setuptools -U"
        self.pygame_install_linux = "python3 -m pip install pygame"  # pip3 uninstall pygame
        #self.pygame_update_linux = "python3 -m pip install pygame -U"
        self.pygame_install_win32 = "pip install pygame"
        self.pygame_update_win32 = "python -m pip install pygame -U"

    def modules_update(self):
        try:
            print("[UPDATE] Trying to update pip")
            if sys.platform == 'linux':
                subprocess.run(self.pip_update_linux, shell=True)
                subprocess.run(self.modules_update_linux_1, shell=True)
                subprocess.run(self.modules_update_linux_2, shell=True)
                #subprocess.run(self.setuptools_update_linux, shell=True)
                #subprocess.run(self.wheel_update_linux, shell=True)
            elif sys.platform == 'win32':
                subprocess.run(self.pip_update_win32, shell=True)
                subprocess.run(self.setuptools_install_win32, shell=True)
                subprocess.run(self.wheel_update_win32, shell=True)
            print("[UPDATE] Pip has been updated")
        except:
            print("[UPDATE] Pip has not been updated")

        #try:
            #print("[UPDATE] Trying to update pygame")
            #if sys.platform == 'linux':
                #subprocess.run(self.pygame_update_linux, shell=True)
            #elif sys.platform == 'win32':
                #subprocess.run(self.pygame_update_win32, shell=True)
            #print("[UPDATE] Pygame has been updated")
        #except:
            #print("[UPDATE] Pygame has not been updated")

    def pip_install(self):
        print("[INSTALLATION] Trying to install pip")
        if sys.platform == 'linux':
            subprocess.run(self.pip_install_linux, shell=True)
            subprocess.run(self.setuptools_install_linux, shell=True)
            subprocess.run(self.wheel_install_linux, shell=True)
        elif sys.platform == 'win32':
            subprocess.run(self.pip_install_win32, shell=True)
            subprocess.run(self.setuptools_install_win32, shell=True)
            subprocess.run(self.wheel_install_win32, shell=True)
        print("[INSTALLATION] Pip and module has been installed")

    def tkinter_check(self):
        try:
            print("[IMPORT] Trying to import tkinter")
            import tkinter as tk
            print("[IMPORT] Tkinter is installed")
        except:
            print("[EXCEPTION] Tkinter not installed")
            try:
                print("[INSTALLATION] Trying to install tkinter")
                if sys.platform == "linux":
                    subprocess.run(self.tcl_install_linux, shell=True)
                    subprocess.run(self.tkinter_install_linux, shell=True)
                elif sys.platform == "win32":
                    self.tkinter_is_installed = False
                    raise NameError(self.win32_error)
                self.tkinter_is_installed = False
                import tkinter as tk
                print("[INSTALLATION] Tkinter has been installed")
            except:
                if sys.platform == "win32":
                    print(self.win32_error)
                    print('[EXCEPTION] Please repair your version of python with module Tcl/Tk and pip!!!')
                elif sys.platform == "linux":
                    try:
                        print("[EXCEPTION] Pip and module not installed on system")
                        self.pip_install()
                        try:
                            print("[INSTALLATION] Trying to install tkinter")
                            subprocess.run(self.tcl_install_linux, shell=True)
                            subprocess.run(self.tkinter_install_linux, shell=True)
                            import tkinter as tk
                            print("[INSTALLATION] Tkinter has been installed")
                            self.tkinter_is_installed = False
                        except:
                            print("[INSTALLATION ERROR] Tkinter could not be installed")
                    except:
                        print("[INSTALLATION ERROR] Pip could not be installed")

    def pygame_check(self):
        try:
            print("[IMPORT] Trying to import pygame")
            import pygame
            print("[IMPORT] Pygame is installed")
        except:
            print("[EXCEPTION] Pygame not installed")

            try:
                print("[INSTALLATION] Trying to install pygame via pip")
                if sys.platform == "linux":
                    subprocess.run(self.pygame_install_linux, shell=True)
                elif sys.platform == "win32":
                    subprocess.run(self.pygame_install_win32, shell=True)
                import pygame
                print("[INSTALLATION] Pygame has been installed")
                self.pygame_is_installed = False
            except:
                try:
                    print("[EXCEPTION] pip and module not installed on system")
                    self.pip_install()
                    try:
                        print("[INSTALLATION] Trying to install pygame")
                        if sys.platform == "linux":
                            subprocess.run(self.pygame_install_linux, shell=True)
                        elif sys.platform == "win32":
                            subprocess.run(self.pygame_install_win32, shell=True)
                        import pygame
                        print("[INSTALLATION] pygame has been installed")
                        self.pygame_is_installed = False
                    except:
                        print("[INSTALLATION ERROR] pygame could not be installed")
                except:
                    print("[INSTALLATION ERROR] Pip could not be installed")


#check = CheckRequiredModules()
#check.pygame_check()
#check.tkinter_check()
#if check.pygame_is_installed and check.tkinter_is_installed:
    #check.modules_update()

# input("Update finish, press any key to exit.")
