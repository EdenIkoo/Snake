from fltk import *
from time import sleep
from random import randint
# dimensions du jeu
taille_case = 15
largeur_plateau = 40  # en nombre de cases
hauteur_plateau = 30  # en nombre de cases


def case_vers_pixel(case):
    """Fonction recevant les coordonnées d'une case du plateau sous la\
    forme d'un couple d'entiers (ligne, colonne) et renvoyant les \
    coordonnées du pixel se trouvant au centre de cette case. Ce calcul \
    prend en compte la taille de chaque case, donnée par la variable \
    globale taille_case."""
    i, j = case
    return (i + .5) * taille_case, (j + .5) * taille_case


def affiche_pommes(pommes):
    for pomme in pommes:
        x, y = case_vers_pixel(pomme)
        cercle(x, y, taille_case/2,
               couleur='darkred', remplissage='red')
        rectangle(x-2, y-taille_case*.4, x+2, y-taille_case*.7,
                  couleur='darkgreen', remplissage='darkgreen')


def affiche_serpent(corps):
    for i in range(len(corps)):
        [x, y] = corps[i]
        x, y = case_vers_pixel(corps[i])
        cercle(x, y, taille_case/2 + 1,
        couleur='darkgreen', remplissage='green')


def change_direction(direction, touche):
    """
    >>>change_direction((+1, 0), 'Up')
    >>>(0, +1)
    """
    if touche == 'Up' and direction != (0, +1):
        # flèche haut pressée
        return (0, -1)
    elif touche == 'Down' and direction != (0, -1):
        # flèche bas pressée
        return (0, +1)
    elif touche == 'Left' and direction != (+1, 0):
        # flèche gauche pressée
        return (-1, 0)
    elif touche == 'Right' and direction != (-1, 0):
        # flèche droite pressée
        return (+1, 0)
    else:
        # pas de changement !
        return direction


def deplacement(serpent, direction):
    """Fonction recevant les coordonnées du serpent. Reçoit également
    la direction dans laquelle va aller le serpent (sous forme d'un
    couple d'entiers). Additionne la direction à la position actuelle
    du serpent. Retourne sa nouvelle position après mouvement.
    >>>deplacement((20, 15),(0, +1))
    >>>(20, 16)"""
    [x1, y1] = serpent
    (dx1, dy1) = direction
    serpent = (x1 + dx1, y1 + dy1)
    return serpent


def lapomme(corps):
    """Fonction faisant apparaitre une pomme sur le terrain. vérifie
    que la pomme n'apparait pas SUR le corps du serpent."""
    xpomme = randint(0, 39)
    ypomme = randint(3, 30)
    pomme = (xpomme, ypomme)
    while pomme in corps:
        xpomme = randint(0, 39)
        ypomme = randint(3, 32)
        pomme = (xpomme, ypomme)
    return pomme
# programme principal


if __name__ == "__main__":

    # initialisation du jeu
    framerate = 10    # taux de rafraîchissement du jeu en images/s
    direction = (0, -1)  # direction initiale du serpent
    cree_fenetre(taille_case * 40, taille_case * 33)
    serpent = (20, 15)  # Tete du serpent
    corps = [serpent, (20, 16), (20, 17)]  # Liste des coor du corps du serpent
    pommes = []  # liste des coordonnées des cases contenant des pommes
    timerpomme = 0
    pommes.append(lapomme(serpent))
    score = 0
    jouer = False
    # boucle principale
    """INTERFACE D'ACCUEIL"""
    while jouer is False:
        rectangle(0, 600, 600, 0, remplissage='black')
        texte(taille_case * 20, taille_case * 4, "SNAKE", ancrage='center',
                   taille=75, police='Fixedsys', couleur='Green')
        rectangle(taille_case * 2, taille_case * 10,
                  taille_case * 12, taille_case * 14, couleur='white')
        texte(taille_case * 7, taille_case * 12, "PLAY", ancrage='center',
                    taille=30, police='Fixedsys', couleur='white')
        rectangle(taille_case * 2, taille_case * 16, taille_case * 12,
                   taille_case * 20, couleur='white')
        texte(taille_case * 7, taille_case * 18, "HELP", ancrage='center',
                    taille=30, police='Fixedsys', couleur='white')
        rectangle(taille_case * 2, taille_case * 22, taille_case * 12,
                   taille_case * 26, couleur='white')
        texte(taille_case * 7, taille_case * 24, "EXIT", ancrage='center',
                    taille=30, police='Fixedsys', couleur='white')
        image(taille_case * 29.5, taille_case * 21.15,
              'snake1.gif', ancrage='center')
        ev1 = attend_clic_gauche()
        x, y = ev1
        """BOUTON "QUIT" """
        if x >= taille_case * 2 and x <= taille_case * 12 and \
           y >= taille_case * 22 and y <= taille_case * 26:
            ferme_fenetre()
        """BOUTON "HELP" """
        if x >= taille_case * 2 and x <= taille_case * 12 and \
           y >= taille_case * 16 and y <= taille_case * 20:
            jouer = False
            efface_tout()
            rectangle(0, 600, 600, 0, remplissage='black')
            rectangle(taille_case * 2, taille_case * 1.5,
                      taille_case * 38, taille_case * 6.5, couleur='white')
            texte(taille_case * 20, taille_case * 4,
                   "REGLES DU JEU", ancrage='center',
                   taille=60, police='Fixedsys', couleur='white')
            texte(taille_case * 20, taille_case * 9,
                   "Vous contrôlez un serpent", ancrage='center',
                   taille=18, police='Fixedsys', couleur='white')
            texte(taille_case * 20, taille_case * 11,
                   "à l'aide des touches directionnelles.", ancrage='center',
                   taille=18, police='Fixedsys', couleur='white')
            texte(taille_case * 20, taille_case * 21,
                   "Le but   du jeu est de manger", ancrage='center',
                   taille=18, police='Fixedsys', couleur='white')
            texte(taille_case * 20, taille_case * 23,
                   "le plus de pommes sur le terrain,", ancrage='center',
                   taille=18, police='Fixedsys', couleur='white')
            texte(taille_case * 20, taille_case * 25,
                   "sans se mordre la queue,", ancrage='center',
                   taille=18, police='Fixedsys', couleur='white')
            texte(taille_case * 20, taille_case * 27,
                   "et sans sortir de la fenêtre de jeu.", ancrage='center',
                   taille=18, police='Fixedsys', couleur='white')
            image(taille_case * 10.25, taille_case * 17.5,
                  'serpent2.gif', ancrage='center')
            image(taille_case * 31, taille_case * 16.5,
                  'touche.gif', ancrage='center')
            rectangle(taille_case * 16, taille_case * 29, taille_case * 24,
                      taille_case * 32, couleur='white')
            texte(taille_case * 20, taille_case * 30.5, "Back",
                   ancrage='center', taille=19, police='Fixedsys',
                  couleur='white')
            ev2 = attend_clic_gauche()
            x, y = ev2
            if x >= taille_case * 16 and x <= taille_case * 24 and \
               y >= taille_case * 29 and y <= taille_case * 32:
                jouer = False
        """BOUTON "JOUER" """
        if x >= taille_case * 2 and x <= taille_case * 12 and \
           y >= taille_case * 10 and y <= taille_case * 14:
            efface_tout()
            rectangle(0, 600, 600, 0, remplissage='black')
            jouer = True
    """DECOMPTE AVANT DE JOUER"""
    if jouer == True:
        texte(taille_case * 20, taille_case * 16.5, "Prêt ?", ancrage='center',
                           taille=25, couleur="white", police='Fixedsys')
        attente(1)
        efface_tout()
        rectangle(0, 600, 600, 0, remplissage='black')
        texte(taille_case * 20, taille_case * 16.5, "3.", ancrage='center',
                        taille=25, couleur="white", police='Fixedsys')
        attente(0.1)
        efface_tout()
        rectangle(0, 600, 600, 0, remplissage='black')
        texte(taille_case * 20, taille_case * 16.5, "3..", ancrage='center',
                          taille=25, couleur="white", police='Fixedsys')
        attente(0.1)
        efface_tout()
        rectangle(0, 600, 600, 0, remplissage='black')
        texte(taille_case * 20, taille_case * 16.5, "3...", ancrage='center',
                           taille=25, couleur="white", police='Fixedsys')
        attente(0.5)
        efface_tout()
        rectangle(0, 600, 600, 0, remplissage='black')
        texte(taille_case * 20, taille_case * 16.5, "2.", ancrage='center',
                             taille=25, couleur="white", police='Fixedsys')
        attente(0.1)
        efface_tout()
        rectangle(0, 600, 600, 0, remplissage='black')
        texte(taille_case * 20, taille_case * 16.5, "2..", ancrage='center',
                        taille=25, couleur="white", police='Fixedsys')
        attente(0.1)
        efface_tout()
        rectangle(0, 600, 600, 0, remplissage='black')
        texte(taille_case * 20, taille_case * 16.5, "2...", ancrage='center',
                        taille=25, couleur="white", police='Fixedsys')
        attente(0.5)
        efface_tout()
        rectangle(0, 600, 600, 0, remplissage='black')
        texte(taille_case * 20, taille_case * 16.5, "1.", ancrage='center',
                taille=25, couleur="white", police='Fixedsys')
        attente(0.1)
        efface_tout()
        rectangle(0, 600, 600, 0, remplissage='black')
        texte(taille_case * 20, taille_case * 16.5, "1..", ancrage='center',
                        taille=25, couleur="white", police='Fixedsys')
        attente(0.1)
        efface_tout()
        rectangle(0, 600, 600, 0, remplissage='black')
        texte(taille_case * 20, taille_case * 16.5, "1 ...", ancrage='center',
                            taille=25, couleur="white", police='Fixedsys')
        attente(0.5)
        efface_tout()
        rectangle(0, 600, 600, 0, remplissage='black')
        texte(taille_case * 20, taille_case * 16.5, "GO !", ancrage='center',
                          taille=25, couleur="white", police='Fixedsys')
        attente(1)
    while jouer:
        # affichage des objets
        efface_tout()
        rectangle(0, 600, 600, 0, remplissage='black')
        affiche_pommes(pommes)
        affiche_serpent(corps)
        """Affichage de la fenêtre"""
        ligne(0, (taille_case * 3), (taille_case * 40), (taille_case * 3),
              epaisseur=3, couleur='white')
        texte(taille_case * 1, taille_case * (5/2), "Score:", ancrage='sw',
               taille=20, police='Fixedsys', couleur='white')
        texte(taille_case * (15/2), taille_case * (5/2), score, ancrage='sw',
               taille=20, police='Fixedsys', couleur='white')
        mise_a_jour()
        # gestion des événements
        ev = donne_ev()
        ty = type_ev(ev)
        if ty == 'Quitte':
            jouer = False
        elif ty == 'Touche':
            touche(ev)
            direction = change_direction(direction, touche(ev))
        serpent = deplacement(serpent, direction)
        """Si les serpent touche les bords"""
        x1, y1 = serpent
        if x1 < 0 or x1 > 39 or y1 < 3 or y1 > 32:
            texte(taille_case * 20, taille_case * 15,
                   "Perdu!", ancrage='center',
                   taille=35, couleur="red", police='Fixedsys')
            jouer = False
        """Actualise la position du corps du serpent"""
        corps[0:0] = [serpent]
        # Ajoute 1 segment
        corps.pop()
        # Retire le dernier segment
        """Si le serpent se mord lui-même"""
        for i in range(1, len(corps)):
            if corps[0] == corps[i]:
                texte(taille_case * 20, taille_case * 18,
                      "Perdu !", ancrage='center',
                      taille=25, couleur="red", police='Fixedsys')
                jouer = False
        """Fais apparaitre une pomme à chaque fois que le timer = 100
        ou s'il n'y a plus de pommes sur le terrain"""
        if timerpomme == 100 or len(pommes) == 0:
            pomme = lapomme(corps)
            pommes.append(pomme)
            timerpomme = 0
        timerpomme += 1
        """Si la tête du serpent passe sur une pomme"""
        if serpent in pommes:
            score += 1
            a_supp = serpent
            pommes.remove(a_supp)
            """Grandis le serpent si une pomme est mangée"""
            corps[0:0] = [serpent]
            # Ajoute 1 segment
        # attente avant rafraîchissement
        sleep(1/framerate)
    # fermeture et sortie
    attend_ev()
    ferme_fenetre()
