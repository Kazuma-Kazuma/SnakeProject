class Perso:
    def __init__(self, x, y, grid):
        self.x = x
        self.y = y
        self.grid = grid
        self.color = "red"
        self.draw()
        self.bind_keys()

    def draw(self):
        self.grid.draw_square(self.x, self.y, self.color)

    def bind_keys(self):
        self.grid.canvas.bind("<Left>", self.move_left)
        self.grid.canvas.bind("<Right>", self.move_right)
        self.grid.canvas.bind("<Up>", self.move_up)
        self.grid.canvas.bind("<Down>", self.move_down)
        self.grid.canvas.focus_set()

    def move_left(self, event):
        if self.x > 0:
            self.grid.draw_square(self.x, self.y, "gray")
            self.x -= 1
            self.draw()

    def move_right(self, event):
        if self.x < self.grid.width - 1:
            self.grid.draw_square(self.x, self.y, "gray")
            self.x += 1
            self.draw()

    def move_up(self, event):
        if self.y > 0:
            self.grid.draw_square(self.x, self.y, "gray")
            self.y -= 1
            self.draw()

    def move_down(self, event):
        if self.y < self.grid.height - 1:
            self.grid.draw_square(self.x, self.y, "gray")
            self.y += 1
            self.draw()

    def deplacer(self, new_x, new_y):
        # Vérifie si la nouvelle position est à l'intérieur de la grille
        if new_x < 0 or new_x >= self.grid.width or new_y < 0 or new_y >= self.grid.height:
            print("Position invalide")
            return
        # Vérifie si la nouvelle position est libre
        if (new_x, new_y) in self.grid.grid:
            print("Position occupée")
            return
        # Met à jour la position du personnage sur la grille et dessine le personnage à sa nouvelle position
        self.grid.draw_square(self.x, self.y, "gray")
        self.grid.draw_square(new_x, new_y, "blue")
        self.x = new_x
        self.y = new_y
