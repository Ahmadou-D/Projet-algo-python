Fox and Hounds est un petit jeu de réflexion à deux joueurs développé en Python orienté objet (POO).
Il s’agit d’une adaptation d’un jeu traditionnel scandinave, conçu pour mettre en pratique les concepts fondamentaux de la programmation orientée objet : encapsulation, héritage et modularité.

Objectif du jeu
Deux joueurs s’affrontent sur un plateau carré de taille n×n, où n est un multiple de 4.
Le Fox (renard) doit atteindre la première ligne pour gagner.
Les Hounds (chiens de chasse) doivent bloquer totalement le Fox pour remporter la partie.

Règles du jeu
Le Fox (symbole F) commence au centre de la dernière ligne.
Il peut se déplacer en diagonale dans toutes les directions.
Les Hounds (symboles 1, 2, etc.) commencent sur la première ligne, une colonne sur deux.
Ils peuvent se déplacer en diagonale uniquement vers le bas.
Si le Fox atteint la première ligne, il gagne.
Si les Hounds l’empêchent de bouger, ils gagnent.

Structure du code
Le projet est organisé en plusieurs fichiers pour une meilleure clarté :
gameBoard.py → Gère la création et l’affichage du plateau, avec encapsulation (get/set)
hound.py → Définit la classe des chiens et leurs mouvements
fox.py → Classe héritée de Hound, adaptée pour les déplacements du renard
foxAndHounds.py → Contient la logique principale du jeu et la boucle de déroulement
main.py → Point d’entrée du programme, lance la partie avec la taille du plateau choisie

Points techniques
Encapsulation → Les accès au plateau sont contrôlés par des getters et setters.
Héritage → La classe Fox hérite de Hound et redéfinit certaines méthodes (polymorphisme).
Vérifications automatiques → Contrôle des déplacements possibles, des bords du plateau et des conditions de victoire.
Boucle de jeu interactive → Alternance automatique des tours entre Fox et Hounds.

Lancement du jeu
Exécuter main.py
Choisir la taille du plateau (par défaut : 8×8)
Le programme affiche le plateau initial et invite les joueurs à jouer à tour de rôle.
