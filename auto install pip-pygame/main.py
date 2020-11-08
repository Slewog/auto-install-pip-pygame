#! /usr/bin/python3
import subprocess, sys, os



def check_pygame_install():
	pygame_installed = True
	PYGAME_INSTALL_LINUX = "python3 -m pip install pygame" # pip3 uninstall pygame
	PYGAME_INSTALL_WIN32 = "pip install pygame"
	#TKINTER_INSTALL_LINUX = "sudo apt-get install python3-tk" # "sudo apt-get remove python3-tk"

	def update_module():
		try:
			if sys.platform == 'linux':
				subprocess.run("python3 -m pip install -U pip", shell=True)
			elif sys.platform == 'win32':
				subprocess.run("python -m pip install -U pip", shell=True)
			print("[UPDATE] Pip has been updated")
		except:
			print("[UPDATE] Pip has not been updated")

	def secondary_module():
		subprocess.run("pip3 install setuptools", shell=True)
		subprocess.run("pip3 install wheel", shell=True)

	def pip_install():
		print("[EXCEPTION] Pip and module not installed on system")
		print("[INSTALLATION] Trying to install pip")
		if sys.platform == 'linux':
			subprocess.run("sudo apt install python3-pip", shell=True)
		elif sys.platform == 'win32':
			subprocess.run("python get-pip.py", shell=True)
		update_module()
		secondary_module()
		print("[INSTALLATION] Pip and module has been installed")

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