""" Importation de la bibliothèque standard tkinter qui nous permettra de  
créer notre interface graphique (GUI)"""

import tkinter as tk
from tkinter import messagebox, simpledialog
from FileManager import FileManager

# Création de la classe LogManagerApp qui contient toutes les fonctionnalités de l'API
class LogManagerApp:
    
    # Constructeur de la classe
    def __init__(self, root):
        # Initialisation de la Fenêtre Principale
        self.root = root
        self.root.title("Gestionnaire de fichiers log")
        
        # la taille initiale de la fenêtre
        self.root.geometry("800x600")  # Largeur x Hauteur

        # instance de FileManager avec le fichier log.txt
        self.file_manager = FileManager("C:\\Users\\BAANA_MEKA\\Desktop\\log.txt")
        
        # Boutons pour ajouter, lire, modifier, rechercher et compter les lignes de notre fichier
        self.read_button = tk.Button(root, text="Lire le fichier", command=self.display_logs)
        self.read_button.pack(pady=10)
        
        self.write_button = tk.Button(root, text="Modifier le fichier", command=self.write_to_file)
        self.write_button.pack(pady=10)
        
        self.search_button = tk.Button(root, text="Rechercher un mot-clé", command=self.search_keyword)
        self.search_button.pack(pady=10)
        
        self.count_button = tk.Button(root, text="Compter les lignes", command=self.count_lines)
        self.count_button.pack(pady=10)
        
        self.quit_button = tk.Button(root, text="Quitter", command=root.quit)
        self.quit_button.pack(pady=10)
        
        # Zone de texte pour afficher les résultats
        self.text_area = tk.Text(root, height=25, width=100)
        self.text_area.pack(pady=10)

    """
        La fonction display_logs a pour rôle de lire le contenu du fichier 
        et de l'afficher dans la zone de texte de l'interface graphique.
    """
    def display_logs(self):
        try:
            self.text_area.delete(1.0, tk.END)  # Efface l'ancien contenu de la zone de texte
            with open(self.file_manager.file_path, 'r') as file:
                contenu = file.read()  
            self.text_area.insert(tk.END, contenu)  # Affiche le contenu dans la zone de texte
        except FileNotFoundError:
            messagebox.showerror("Erreur", "Le fichier est introuvable.") 
            
    """pour demander à l'utilisateur d'ajouter une nouvelle ligne au fichier."""
    def write_to_file(self):
        # fenêtre pour modifier le fichier.
        self.dialog = tk.Toplevel(self.root)
        self.dialog.title("Modifier le fichier")
        self.dialog.geometry("400x200") 
        self.entry = tk.Text(self.dialog, height=20, width=80)
        self.entry.pack(pady=20)

        # Bouton pour ajouter le texte
        add_button = tk.Button(self.dialog, text="Ajouter", command=self.add_text)
        add_button.pack(pady=10)

        # Bouton pour fermer la fenêtre
        close_button = tk.Button(self.dialog, text="Annuler", command=self.dialog.destroy)
        close_button.pack(pady=5)
        
        # fonction pour Obtenir le texte et l'insérer dans le fichier
    def add_text(self):
        data = self.entry.get("1.0", tk.END).strip()  
        if data:
            self.file_manager.write_to_file(data)
            self.text_area.insert(tk.END, f"{data}\n")
            messagebox.showinfo("Succès", "La ligne a été ajoutée au fichier.")
            self.dialog.destroy()  # Ferme la fenêtre après ajout
        else:
            messagebox.showwarning("Avertissement", "Aucune donnée n'a été ajoutée.")

    """Recherche un mot-clé dans le fichier log."""
    def search_keyword(self):
        keyword = simpledialog.askstring("Rechercher un mot-clé", "Entrez le mot-clé à rechercher :")
        if keyword:
            self.text_area.delete(1.0, tk.END)  # Efface la zone de texte
            with open(self.file_manager.file_path, 'r') as file:
                lines = file.readlines()
                found = False
                for i, line in enumerate(lines):
                    if keyword.lower() in line.lower():
                        self.text_area.insert(tk.END, f"Ligne {i+1}: {line}")
                        found = True
                if not found:
                    self.text_area.insert(tk.END, "Aucun résultat trouvé.")
                    
    """Compte et affiche le nombre de lignes dans le fichier"""
    def count_lines(self):
        nombre_de_lignes = self.file_manager.count_lines()
        messagebox.showinfo("Nombre de lignes", f"Le fichier contient {nombre_de_lignes} lignes.")

# Crée la fenêtre Tkinter
root = tk.Tk()
app = LogManagerApp(root)
root.mainloop()
