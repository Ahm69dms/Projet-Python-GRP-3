class FileManager: 
    #initialisation de la classe FileManager avec le chemin du fichier
    def __init__(self, file_path):
        self.file_path = file_path # chemin du fichier
        
    """la fonction read_file() Lit et affiche le contenu du fichier. si il est absent le code renvoi un message"""    
    def read_file(self):
        try:
            with open(self.file_path, 'r') as mon_fichier:
                contenu_fichier = mon_fichier.read()
                print(contenu_fichier)
        except FileNotFoundError: 
            print("----ERROR, FILE NOT FOUND----")
        
    """la fonction pour écrire les données dans le fichier."""  
    def write_to_file(self, data):
        data = input("Entrez les données à ajouter au fichier: ")
        try:
            with open(self.file_path, 'a') as file: # ouvrir le fichier en mode append, sans supprimer le contenu précedent
                file.write(data + '\n')  # Écrire les données dans le fichier
                print(f"Les données ont été écrites avec succès dans {self.file_path}.")
        except Exception as erreur:  # Capture toute erreur
            print(f"Erreur lors de l'écriture dans le fichier : {erreur}")  # Affiche le message d'erreur
        
    """la fonction qui retourne le nombre de lignes dans le fichier."""
    def count_lines(self):
        try:
            with open(self.file_path, 'r') as mon_fichier:
                nombres_lignes = mon_fichier.readlines()
                return len(nombres_lignes)
        except FileNotFoundError:
            return 0

    """Recherche un mot-clé dans le fichier et affiche les lignes correspondantes."""
    def search_keyword(self, keyword):
        
    #"""Recherche un mot-clé dans le fichier et affiche les lignes correspondantes, tout en comptant le nombre d'occurrences."""
    
        keyword = input("Entrez le mot-clé : ").lower()  # Gestion de la casse

        total = 0
        try:
            with open(self.file_path, 'r') as mon_fichier:  # Ouvre en mode lecture seule
                trouver = False
            
                for numero_ligne, line in enumerate(mon_fichier, start=1):
                    if keyword in line.lower():  # Comparer la ligne et le mot-clé en minuscules
                        print(f"Mot-clé trouvé à la ligne {numero_ligne}: {line.strip()}")
                        trouver = True
                        total += line.lower().count(keyword)  # Compter les occurrences du mot-clé dans la ligne
            
            print(f"Le mot '{keyword}' apparaît {total} fois dans le fichier.")
            
            if not trouver:
                    print(f"Le mot-clé '{keyword}' n'a pas été trouvé dans le fichier.")
        except FileNotFoundError:
                print("---ERROR, FILE NOT FOUND--")

            
        
# Test de la classe
print("<--DEBUT-->")

   