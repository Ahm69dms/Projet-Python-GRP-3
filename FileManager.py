class FileManager: 
    #initialisation de la classe FileManager avec le chemin du fichier
    def __init__(self, file_path):
        self.file_path = file_path # chemin du fichier
        
    def read_file(self):
        "Lire et affiche le contenu du fichier."
        try:
            with open(self.file_path, 'r') as fie:
                contenu = file.read()
            print(contenu)
        except FileNotFoundError:
            print(f"Erreur : Le fichier '{sel.file_path}' n'existe pas, il est crée.
            
    
    def write_to_file(self,data):
         "Ecrire des données dans le fichier."
        try:
            with open(sel.file_path, 'a') as file: # Mode 'a' pour ajouter sans effacer   
                 file.write(data + '\n')
            print(f"Données ajoutées au fichier '{self.file_path}'.")
        except Exception as e:
            print(f'Erreur lors de l'ecriture dans le fichier : {e}")
                
    
    def count_lines(self):
         "Retoune le nombre de lignes dans le fichier."

    def search_keyword(self,keyword):
         "Recherche un mot clé dans le fichier et affiche les lignes correspondantes."   
   
