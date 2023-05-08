import tkinter as tk
import random
from tkinter import ttk
from perso import Perso

class Grid:
    def __init__(self, width, height, square_size, window):
        # Initialisation de la grille avec la largeur, la hauteur et la taille des carrés
        self.width = width
        self.height = height
        self.square_size = square_size
        # Ensemble vide pour stocker les carrés remplis
        self.grid = set()
        # Création d'un objet Canvas Tkinter pour dessiner la grille et les carrés
        self.canvas = tk.Canvas(window, width=width*square_size, height=height*square_size)
        self.canvas.pack(side=tk.LEFT)
        # Dessine la grille avec la méthode draw_grid()
        self.draw_grid()
        # Dessine deux carrés pour illustrer leur position sur la grille

    def draw_square(self, x, y, color):
        # Calcule les coordonnées x et y en pixels à partir des coordonnées de la grille et de la taille des carrés
        x_pixel = x * self.square_size
        y_pixel = y * self.square_size
        # Dessine un carré sur le canvas Tkinter à l'aide de la méthode create_rectangle() avec les coordonnées calculées et la couleur spécifiée
        self.canvas.create_rectangle(x_pixel, y_pixel, x_pixel + self.square_size, y_pixel + self.square_size, fill=color)
        # Ajoute le carré à l'ensemble grid si sa couleur est noire, sinon le supprime de l'ensemble
        if color == "black":
            self.grid.add((x, y))
        else:
            self.grid.discard((x, y))

    def draw_grid(self):
        # Parcours chaque ligne et chaque colonne de la grille pour dessiner les carrés
        for y, row in enumerate(range(self.height)):
            for x, col in enumerate(range(self.width)):
                # Détermine la couleur de chaque carré en fonction de sa position et de ses voisins, selon des conditions basées sur des valeurs aléatoires
                if (x, y) in self.grid:
                    # Si le carré est dans l'ensemble grid, sa couleur est noire
                    color = "black"
                else:
                    # Sinon, la couleur du carré est grise
                    color = "gray"
                # Dessine un carré gris
                self.draw_square(x, y, color)

def generate_grid(width, height, square_size, window):
        # Create a canvas with a frame to center the grid
    frame = ttk.Frame(window)
    frame.pack(fill=tk.BOTH, expand=tk.YES)
    canvas = tk.Canvas(frame, width=width*square_size, height=height*square_size)
    canvas.pack(expand=tk.YES)
    
    # Create the grid inside the canvas
    grid = Grid(width, height, square_size, canvas)
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    canvas_width = width * square_size
    canvas_height = height * square_size
    
    # Calculate the x and y offsets to center the grid
    if window_width > canvas_width:
        x_offset = (window_width - canvas_width) // 2
        canvas.place(x=x_offset)
    if window_height > canvas_height:
        # Calculate the y offset to center the grid
        y_offset = (window_height - canvas_height) // 2
        canvas.place(y=y_offset)
        
    return grid

# Example usage with Tkinter
grid_width = 16
grid_height = 16
square_size = 32

root = tk.Tk()
root.title("Agents Game")
grid = generate_grid(grid_width, grid_height, square_size, root)

root.mainloop()
