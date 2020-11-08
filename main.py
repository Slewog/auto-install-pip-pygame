#! /usr/bin/python3
import subprocess, sys, get_pip, os


#subprocess.call([sys.executable, "-m", "pip", "install", "--upgrade"])

def update_module():
	if sys.platform == 'linux':
		subprocess.run("pip3 install -U pip", shell=True)
		print("update ok")
	#elif sys.platform == 'win32':
		#subprocess.run("python -m pip install -U pip", shell=True)

def check_pygame():
	try:
		print("[GAME] Trying to import pygame")
		import pygame
	except:
		print("[EXCEPTION] Pygame not installed")

		try:
			print("[GAME] Trying to install pygame via pip")
			subprocess.run("pip3 install pygame", shell=True)
			print("[GAME] Pygame has been installed")
		except:
			print("[EXCEPTION] Pip not installed on system")

			print("[GAME] Trying to install pip")

			if sys.platform == 'linux':
				subprocess.run("sudo apt install python3-pip", shell=True)
				subprocess.run("pip3 install -U pip", shell=True)
				subprocess.run("pip3 install setuptools", shell=True)
				subprocess.run("pip3 install wheel", shell=True)
			elif sys.platform == 'win32':
				subprocess.run("python get_pip.py", shell=True)
				subprocess.run("python -m pip install -U pip", shell=True)
				subprocess.run("pip3 install setuptools", shell=True)
				subprocess.run("pip3 install wheel", shell=True)

			print("[GAME] Pip has been installed")

			try:
				print("[GAME] Trying to install pygame")
				subprocess.run("pip3 install pygame", shell=True)
				print("[GAME] Pygame has been installed")
			except:
				print("[ERROR 1] Pygame could not be installed")


check_pygame()
update_module()