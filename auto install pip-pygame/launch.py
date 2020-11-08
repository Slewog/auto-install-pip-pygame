#! /usr/bin/python3
from required import CheckRequiredModules
run = True
update = CheckRequiredModules()

while run:
    answer = input("Pour vérifier si pygame est à jour faite 1, pour tkinter faite 2, pour mettre à jour les modules "
                   "faites 3 et 4 pour quitter.")
    try:
        val = int(answer)
        if answer == '1':
            update.pygame_check()
        elif answer == '2':
            update.tkinter_check()
        elif answer == '3':
            update.modules_update()
        elif answer == '4':
            run = False
    except ValueError:
        print("entrez seulement nombre et pas des lettres")