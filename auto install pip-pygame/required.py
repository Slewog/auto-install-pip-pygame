#! /usr/bin/python3
import subprocess
import sys
import os


class CheckRequiredModules:
    def __init__(self):
        self.pygame_is_installed = True
        self.tkinter_is_installed = True
        self.python_call_linux = "python3 "
        self.python_call_win32 = "python "

    def modules_update(self):
        pip_update = "-m pip install -U pip"
        modules_update_list = "-m pip list -o > outdated"
        modules_update_linux = "for x in $(sed -n '3,$p' outdated  awk '{print $1}'); do python3 -m pip install -U $x; done"
        try:
            print("[UPDATE] Trying to update your modules")
            if sys.platform == 'linux':
                for command in [self.python_call_linux + pip_update, self.python_call_linux + modules_update_list, modules_update_linux]:
                    subprocess.run(command, shell=True)
                try:
                    os.remove(r"outdated")
                except OSError as e:
                    print('[ERROR] the file "outdated" does not exist.')
            elif sys.platform == 'win32':
                for command in [pip_update, modules_update_list]:
                    subprocess.run(self.python_call_win32 + command, shell=True)
                with open("outdated") as outdated_file:
                    module_list = outdated_file.readlines()
                if len(module_list) >= 3:
                    module_list.pop(0), module_list.pop(0)
                    for module in module_list:
                        module_list = module.replace(" ", ",")
                        module_list = list(module_list.split(","))
                        subprocess.run("python -m pip install " + module_list[0] + " -U", shell=True)
                try:
                    os.remove(r"outdated")
                except OSError:
                    print('[ERROR] The file "outdated" does not exist.')
            print("[UPDATE] Your python modules has been updated")
        except:
            print("[UPDATE ERROR] Your python modules has not been updated")

    def pip_install(self):
        pip_install_linux = "sudo apt-get install python3-pip"
        pip_install_win32 = "python get-pip.py"
        wheel_install = "-m pip install wheel"
        setuptools_install = "-m pip install setuptools"
        print("[INSTALLATION] Trying to install pip")
        if sys.platform == 'linux':
            for command in [pip_install_linux, self.python_call_linux + setuptools_install, self.python_call_linux + wheel_install]:
                subprocess.run(command, shell=True)
        elif sys.platform == 'win32':
            for command in [pip_install_win32, self.python_call_win32 + setuptools_install, self.python_call_win32 + wheel_install]:
                subprocess.run(command, shell=True)
        print("[INSTALLATION] Pip and module has been installed")

    def tkinter_check(self):
        win32_error = "[EXCEPTION] Windows system operating is executing."
        tkinter_install_linux = "sudo apt-get install python3-tk"  # "sudo apt-get remove python3-tk"
        tcl_install_linux = "sudo apt-get install tcl"  # " pip install Tcl"
        try:
            print("[IMPORT] Trying to import tkinter")
            import tkinter as tk
            print("[IMPORT] Tkinter is installed")
        except:
            print("[EXCEPTION] Tkinter not installed")
            try:
                print("[INSTALLATION] Trying to install tkinter")
                if sys.platform == "linux":
                    for command in [tcl_install_linux, tkinter_install_linux]:
                        subprocess.run(command, shell=True)
                    self.tkinter_is_installed = False
                elif sys.platform == "win32":
                    self.tkinter_is_installed = False
                    raise NameError(win32_error)
                import tkinter as tk
                print("[INSTALLATION] Tkinter has been installed")
            except:
                if sys.platform == "win32":
                    print(win32_error)
                    print('[EXCEPTION] Please repair your version of python with module Tcl/Tk and pip!!!')
                elif sys.platform == "linux":
                    try:
                        print("[EXCEPTION] Pip and module not installed on system")
                        self.pip_install()
                        try:
                            print("[INSTALLATION] Trying to install tkinter")
                            for command in [tcl_install_linux, tkinter_install_linux]:
                                subprocess.run(command, shell=True)
                            import tkinter as tk
                            print("[INSTALLATION] Tkinter has been installed")
                            self.tkinter_is_installed = False
                        except:
                            print("[INSTALLATION ERROR] Tkinter could not be installed")
                    except:
                        print("[INSTALLATION ERROR] Pip could not be installed")

    def pygame_check(self):
        pygame_install = "-m pip install pygame"  # pip3 uninstall pygame
        try:
            print("[IMPORT] Trying to import pygame")
            import pygame
            print("[IMPORT] Pygame is installed")
        except:
            print("[EXCEPTION] Pygame not installed")
            try:
                print("[INSTALLATION] Trying to install pygame via pip")
                if sys.platform == "linux":
                    subprocess.run(self.python_call_linux + pygame_install, shell=True)
                elif sys.platform == "win32":
                    subprocess.run(self.python_call_win32 + pygame_install, shell=True)
                import pygame
                print("[INSTALLATION] Pygame has been installed")
                self.pygame_is_installed = False
            except:
                try:
                    print("[EXCEPTION] Pip not installed on system")
                    self.pip_install()
                    try:
                        print("[INSTALLATION] Trying to install pygame")
                        if sys.platform == "linux":
                            subprocess.run(self.python_call_linux + pygame_install, shell=True)
                        elif sys.platform == "win32":
                            subprocess.run(self.python_call_win32 + pygame_install, shell=True)
                        import pygame
                        print("[INSTALLATION] Pygame has been installed")
                        self.pygame_is_installed = False
                    except:
                        print("[INSTALLATION ERROR] Pygame could not be installed")
                except:
                    print("[INSTALLATION ERROR] Pip could not be installed")
