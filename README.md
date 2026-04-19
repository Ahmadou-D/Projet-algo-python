# 🦊 Fox and Hounds - Programmation Orientée Objet

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## 📝 Présentation
Adaptation d'un jeu traditionnel scandinave développée en **Python**. Ce projet a pour but de mettre en pratique les concepts fondamentaux de la **POO** (Programmation Orientée Objet).

## 🧠 Concepts techniques appliqués
* **Encapsulation** : Contrôle des accès au plateau via des getters et setters.
* **Héritage et Polymorphisme** : Utilisation d'une classe mère `Hound` dont hérite la classe `Fox`, avec redéfinition des méthodes de mouvement.
* **Modularité** : Découpage du code en modules distincts (`gameBoard`, `hound`, `fox`, `main`) pour une maintenance facilitée.

## 🎮 Règles du jeu
* **Le Fox (F)** doit atteindre la première ligne du plateau.
* **Les Hounds (1, 2...)** doivent bloquer totalement le Fox.
* Le Fox se déplace en diagonale dans toutes les directions, tandis que les Hounds ne peuvent descendre que vers le bas.

## 🚀 Lancement
```bash
python main.py
