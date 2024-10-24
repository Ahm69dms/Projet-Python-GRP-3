from FileManager import FileManager

if __name__ == "__main__":

    #demande à l'utilisateur d'entrer le chemin vers le fichier
    print(f"entrer le chemin vers le fichier :")
    chemin_fichier = input("")

    # Crée une instance de FileManager avec le chemin vers le fichier
    file_manager = FileManager( chemin_fichier )  ## chemin vers mon fichier
    choice = 0
    
    # le while nous permet de gérer le cas de d'erreur si l'utilisateur entre un choix invalide
    while choice==0:
        print("\nChoisissez une action:")
        print("1. Lire le fichier")
        print("2. Modifier le fichier")
        print("3. Rechercher un mot-clé")
        print("4. Compter le nombre de lignes")
        print("5. Quitter")

        try:
            choice = int(input("Entrez le numéro de votre choix: "))
        except ValueError:
            print("--------------erreur, Veuillez entrer un numéro valide.---------------")
            continue

        if choice == 1:
            # Lire le contenu du fichier
            file_manager.read_file()
            
        elif choice == 2:
            # Écrire des données dans le fichier

            file_manager.write_to_file(data='')
            
        elif choice == 3:
            # Rechercher un mot-clé
            file_manager.search_keyword(keyword="")
            
        elif choice == 4:
            # Compter le nombre de lignes et afficher le résultat
            nombre_de_lignes = file_manager.count_lines()
            print(f"Nombre de lignes dans le fichier : {nombre_de_lignes}")
            
        elif choice == 5:
            # Quitter le programme
            print("Au revoir!")
            break
            
        else:
            print("Choix invalide. Veuillez réessayer.")
