import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
from FileManager import FileManager

class LogManagerApp:
    def __init__(self, root):
        # Initialisation de la Fenêtre Principale
        self.root = root
        self.root.title("Gestionnaire de fichiers log")
        self.root.geometry("800x600")
        self.root.configure(bg="#e8f4f8")  # Fond clair et doux, bleu pâle

        # Initialise la variable du gestionnaire de fichiers
        self.file_manager = None

        # Bouton pour ajouter le fichier log
        add_file_button = tk.Button(root, text="Ajouter le fichier", command=self.add_file, bg="#b3e5fc", fg="black", font=('Arial', 10))
        add_file_button.pack(pady=20)
        
        # Boutons pour les autres fonctionnalités
        self.read_button = tk.Button(root, text="Lire le fichier", command=self.display_logs, state=tk.DISABLED, bg="#b2dfdb", fg="black", font=('Arial', 10))
        self.read_button.pack(pady=10)
        
        self.write_button = tk.Button(root, text="Modifier le fichier", command=self.write_to_file, state=tk.DISABLED, bg="#ffccbc", fg="black", font=('Arial', 10))
        self.write_button.pack(pady=10)
        
        self.search_button = tk.Button(root, text="Rechercher un mot-clé", command=self.search_keyword, state=tk.DISABLED, bg="#d1c4e9", fg="black", font=('Arial', 10))
        self.search_button.pack(pady=10)
        
        self.count_button = tk.Button(root, text="Compter les lignes", command=self.count_lines, state=tk.DISABLED, bg="#c5cae9", fg="black", font=('Arial', 10))
        self.count_button.pack(pady=10)
        
        self.quit_button = tk.Button(root, text="Quitter", command=root.quit, bg="#ffcdd2", fg="black", font=('Arial', 10))
        self.quit_button.pack(pady=10)
        
        # Zone de texte pour afficher les résultats
        self.text_area = tk.Text(root, height=25, width=100, bg="#f1f8e9", fg="#424242", font=('Courier', 10))  # Fond très léger et texte gris foncé
        self.text_area.pack(pady=10)

    def add_file(self):
        # Ouvre le dialogue de sélection de fichier
        file_path = filedialog.askopenfilename(title="Sélectionner un fichier")
        if file_path:
            print(f"Fichier sélectionné : {file_path}")
            self.file_manager = FileManager(file_path=file_path)
            
            # Active les boutons une fois que le fichier est sélectionné
            self.read_button.config(state=tk.NORMAL)
            self.write_button.config(state=tk.NORMAL)
            self.search_button.config(state=tk.NORMAL)
            self.count_button.config(state=tk.NORMAL)
        else:
            print("Aucun fichier.")

#   fonction pour lire et afficher le contenu du fichier spécifié
    def display_logs(self):
        try:
            self.text_area.delete(1.0, tk.END)
            with open(self.file_manager.file_path, 'r') as file:
                contenu = file.read()
            self.text_area.insert(tk.END, contenu)
        except FileNotFoundError:
            messagebox.showerror("Erreur", "Le fichier est introuvable.")
#   pour écrire les données dans le fichier
    def write_to_file(self):
        self.dialog = tk.Toplevel(self.root)
        self.dialog.title("Modifier le fichier")
        self.dialog.geometry("400x200")
        self.dialog.configure(bg="#e0f2f1")  # Couleur douce pour la fenêtre de dialogue

        self.entry = tk.Text(self.dialog, height=10, width=50, bg="#ffffff", fg="#000000", font=('Courier', 10))
        self.entry.pack(pady=20)

        add_button = tk.Button(self.dialog, text="Ajouter", command=self.add_text, bg="#c8e6c9", fg="black", font=('Arial', 10))
        add_button.pack(pady=10)

        close_button = tk.Button(self.dialog, text="Annuler", command=self.dialog.destroy, bg="#ffe0b2", fg="black", font=('Arial', 10))
        close_button.pack(pady=5)
# permet à l'utilisateur d'entrer du texte via une zone de saisie et d'ajouter ce texte au fichier
    def add_text(self):
        data = self.entry.get("1.0", tk.END).strip()
        if data:
            self.file_manager.write_to_file(data)
            self.text_area.insert(tk.END, f"{data}\n")
            messagebox.showinfo("Succès", "La ligne a été ajoutée au fichier.")
            self.dialog.destroy()
        else:
            messagebox.showwarning("Avertissement", "Aucune donnée n'a été ajoutée.")
#pour rechercher un mot-clé dans le fichier et afficher les lignes correspondantes
    def search_keyword(self):
        keyword = simpledialog.askstring("Rechercher un mot-clé", "Entrez le mot-clé à rechercher :")
        if keyword:
            self.text_area.delete(1.0, tk.END)
            with open(self.file_manager.file_path, 'r') as file:
                lines = file.readlines()
                found = False
                for i, line in enumerate(lines, 0):
                    if keyword.lower() in line.lower():
                        self.text_area.insert(tk.END, f"Ligne {i + 1}: {line}")
                        found = True
                if not found:
                    self.text_area.insert(tk.END, "Aucun résultat trouvé.")

#pour retourner le nombre de lignes dans le fichier
    def count_lines(self):
        nombre_de_lignes = self.file_manager.count_lines()
        messagebox.showinfo("Nombre de lignes", f"Le fichier contient {nombre_de_lignes} lignes.")

# Crée la fenêtre Tkinter
root = tk.Tk()
app = LogManagerApp(root)
root.mainloop()