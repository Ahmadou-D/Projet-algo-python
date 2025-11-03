# Ahmadou Diallo et Aleksandar Lakic

from foxAndHounds import FoxAndHounds

def main():
    print("Jeu du Fox and Hounds")
    taille = int(input("Entrez la taille du plateau (multiple de 4) : "))
    jeu = FoxAndHounds(taille)
    jeu.play()

if __name__ == "__main__":
    main()
