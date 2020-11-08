#! /usr/bin/python3
import subprocess, sys, os
#TKINTER_INSTALL_LINUX = "sudo apt-get install python3-tk" # "sudo apt-get remove python3-tk"
#TCL_INSTALL = " pip install Tcl"
#TCL_INSTALL_LINUX = "sudo apt-get install tcl"
PIP_UPDATE_LINUX = "python3 -m pip install -U pip"
PIP_INSTALL_LINUX = "sudo apt install python3-pip"

PIP_UPDATE_WIN32 = "python -m pip install -U pip"
PIP_INSTALL_WIN32 = "python get-pip.py"

WHEEL_INSTALL_LINUX = "python3 -m pip install wheel"
WHEELS_UPDATE_LINUX = "python3 -m pip install wheel -U"

WHEEL_INSTALL_WIN32 = "python -m pip install wheel"
WHEEL_UPDATE_WIN32 = "python -m pip install wheel -U"

SETUPTOOLS_INSTALL_LINUX ="python3 -m pip install setuptools"
SETUPTOOLS_UPDATE_LINUX = "python3 -m pip install setuptools -U"

SETUPTOOLS_INSTALL_WIN32 = "python -m pip install setuptools"
SETUPTOOLS_UPDATE_WIN32= "python -m pip install setuptools -U"

PYGAME_INSTALL_LINUX = "python3 -m pip install pygame" # pip3 uninstall pygame
PYGAME_UPDATE_LINUX = "python3 -m pip install pygame -U"

PYGAME_INSTALL_WIN32 = "pip install pygame"
PYGAME_UPDATE_WIN32= "python -m pip install pygame -U"


def update_module():
	try:
		print("[UPDATE] Trying to update pip")
		if sys.platform == 'linux':
			subprocess.run(PIP_UPDATE_LINUX, shell=True)
			subprocess.run(SETUPTOOLS_UPDATE_LINUX, shell=True)
			subprocess.run(WHEELS_UPDATE_LINUX, shell=True)
		elif sys.platform == 'win32':
			subprocess.run(PIP_UPDATE_WIN32, shell=True)
			subprocess.run(SETUPTOOLS_INSTALL_WIN3232, shell=True)
			subprocess.run(WHEEL_UPDATE_WIN32, shell=True)
		print("[UPDATE] Pip has been updated")
	except:
		print("[UPDATE] Pip has not been updated")

	try:
		print("[UPDATE] Trying to update pygame")
		if sys.platform == 'linux':
			subprocess.run(PYGAME_UPDATE_LINUX, shell=True)
		elif sys.platform == 'win32':
			subprocess.run(PYGAME_UPDATE_WIN32, shell=True)
		print("[UPDATE] Pygame has been updated")
	except:
		print("[UPDATE] Pygame has not been updated")

def pip_install():
	print("[EXCEPTION] Pip and module not installed on system")
	print("[INSTALLATION] Trying to install pip")
	if sys.platform == 'linux':
		subprocess.run(PIP_INSTALL_LINUX, shell=True)
		subprocess.run(SETUPTOOLS_INSTALL_LINUX, shell=True)
		subprocess.run(WHEEL_INSTALL_LINUX, shell=True)
	elif sys.platform == 'win32':
		subprocess.run(PIP_INSTALL_WIN32, shell=True)
		subprocess.run(SETUPTOOLS_INSTALL_WIN32, shell=True)
		subprocess.run(WHEEL_INSTALL_WIN32, shell=True)
	update_module()
	print("[INSTALLATION] Pip and module has been installed")


def check_pygame_install():
	pygame_installed = True

	def check_pygame():
		try:
			print("[IMPORT] Trying to import pygame")
			import pygame
			print("[IMPORT] Pygame is installed")
		except:
			print("[EXCEPTION] Pygame not installed")

			try:
				print("[INSTALLATION] Trying to install pygame via pip")
				if sys.platform == "linux":
					subprocess.run(PYGAME_INSTALL_LINUX, shell=True)
				elif sys.platform == "win32":
					subprocess.run(PYGAME_INSTALL_WIN32, shell=True)
				import pygame
				print("[INSTALLATION] Pygame has been installed")
				pygame_installed = False
			except:
				try:
					pip_install()
					try:
						print("[INSTALLATION] Trying to install pygame")
						if sys.platform == "linux":
							subprocess.run(PYGAME_INSTALL_LINUX, shell=True)
						elif sys.platform == "win32":
							subprocess.run(PYGAME_INSTALL_WIN32, shell=True)
						import pygame
						print("[INSTALLATION] Pygame has been installed")
						pygame_installed = False
					except:
						print("[INSTALLATION ERROR] Pygame could not be installed")
				except:
					print("[INSTALLATION ERROR] PIP could not be installed")

	check_pygame()
	if pygame_installed:
		update_module()


check_pygame_install()
input("break loop")
