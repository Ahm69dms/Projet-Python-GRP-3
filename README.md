ProjetGroupe3
Objectif:
    Ce projet vise à développer une application en Python qui simplifie la gestion et l'analyse des fichiers texte, offrant une interface utilisateur avec Tkinter pour effectuer des actions variées sur les fichiers. 

L'application permettra d'effectuer les opérations suivantes sur des fichiers texte :

    Lecture : Ouvrir un fichier et en afficher le contenu.

    Écriture : Créer un nouveau fichier ou écraser un fichier existant avec un nouveau contenu.

    Analyse : Compter le nombre de lignes dans le fichier ou rchercher un mot-clé et afficher toutes les occurrences avec leur position dans le fichier.

    Modification : Modifier le contenu d'un fichier.

Structure du Projet

    main : Interface utilisateur principale créée avec Tkinter, permettant aux utilisateurs de sélectionner des fichiers, de déclencher les actions d'analyse, d'ajout de texte, de recherche de mots-clés et de comptage des lignes.
    FileManager : Classe dédiée à la gestion des opérations sur le fichier, incluant la lecture, l’écriture, le comptage de lignes et la recherche de mots-clés.

Nous utiliserons PIP, le gestionnaire de paquets Python, pour :

    Installer des modules externes qui pourraient être utiles pour certaines fonctionnalités (par exemple, un module pour la manipulation de dates, un module pour générer des rapports, etc.).
    Gérer les dépendances du projet, c'est-à-dire la liste des modules externes nécessaires au fonctionnement de l'application.

Utilité du fichier requierements.txt
    Le fichier requierement.txt liste les dependances nécessaires au bon fonctionnement du projet. Cela permet aux autres utilisateurs de facilement installer ces bibliotheques via pip,
    garantissant ainsi qu'ils disposent des bonnes versions des packages pour exécuter.
    
    
    
