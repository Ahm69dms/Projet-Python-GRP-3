from FileManager import FileManager
#if __name__ == "__main__":

"""cette commande permet de lier le fichier log.txt à l'instance de la classe FileManager, afin de pouvoir
                  manipuler ce fichier à l'aide des méthodes définies dans la classe."""
file_manager = FileManager("C:\\Users\\BAANA_MEKA\Desktop\\log.txt")  ## chemin vers mon fichier



# Lire le contenu du fichier
file_manager.read_file()

# Écrire des données dans le fichier
file_manager.write_to_file()

# Compter les lignes et afficher le résultat
nombre_de_lignes = file_manager.count_lines()
print(f"Nombre de lignes dans le fichier : {nombre_de_lignes}")

# Rechercher un mot-clé
file_manager.search_keyword(keyword="mot-clé")
print("<--FIN-->")
print()