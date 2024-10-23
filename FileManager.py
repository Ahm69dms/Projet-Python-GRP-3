class FileManager: 
    #initialisation de la classe FileManager avec le chemin du fichier
    def __init__(self, file_path):
        self.file_path = file_path # chemin du fichier
        self.file_nombres_de_lignes = self.get_count()
        
    # classe pour retourner le nom du fichier
   