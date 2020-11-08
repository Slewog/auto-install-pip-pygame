#! /usr/bin/python3
from required import CheckRequiredModules
run = True
update = CheckRequiredModules()

while run:
    answer = input("Pour installez pip faites 1, vérifier si pygame est installer faite 2, pour tkinter faite 3, pour mettre à jour les modules "
                   "faites 4 et 5 pour quitter.")
    try:
        val = int(answer)
        if answer == '1':
            update.pip_install()
        elif answer == '2':
            update.pygame_check()
        elif answer == '3':
            update.tkinter_check()
        elif answer == '4':
            update.modules_update()
        elif answer == '5':
            run = False
    except ValueError:
        print("entrez seulement nombre et pas des lettres")
