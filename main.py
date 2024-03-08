import random

from tkinter import *

class Case:
    def __init__(self, x, y, parent = None, from_direction = None):
        self.x = x
        self.y = y
        self.parent = parent
        self.from_direction = from_direction


# Première fonction pure !
def generate_list (nb_lines, nb_columns):
    labyrinthe = []
    for y in range (nb_lines):
        for x in range (nb_columns):
            case = Case(x, y)
            labyrinthe.append(case)
    
    return labyrinthe


def go_through_list (labyrinthe):
    for case in labyrinthe:
        print(case.x, case.y)


# Fonction Closure !
def generate_path (case, x_max, y_max, escape, labyrinthe):
    path = []
    path.append(case)
    end = False

    def neighbor(case, x_max, y_max):
        neighbors = []
        # on ajoute les voisins (haut, bas, droite, gauche)
        if case.x + 1 < x_max:
            neighbors.append(Case(case.x + 1, case.y, case,"O"))  # droite
        if case.x - 1 >= 0:
            neighbors.append(Case(case.x - 1, case.y, case,"E"))  # gauche
        if case.y + 1 < y_max:
            neighbors.append(Case(case.x, case.y + 1, case,"N"))  # haut
        if case.y - 1 >= 0:
            neighbors.append(Case(case.x, case.y - 1, case,"S"))  # bas
        return neighbors

    # on met la case de départ dans le chemin
    good_path = [case]
    print ("first path : ", good_path[0].x, good_path[0].y)

    # tant que j'ai des voisin à visiter
    # je récupère la case où je suis
    actual_case = path[-1]
    actual_case_index = len(path) - 1
    while len(path) <= len(labyrinthe): 
        
        print ("index de la case actuelle : ", actual_case_index)
        print ("Je suis à la case : ", actual_case.x, actual_case.y)
        # je récupère ses voisins
        neighbors = neighbor(actual_case, x_max, y_max)

        # Je crée une liste filtré pour les voisins que j'ai pas visité 
        # Fonction anonyme lambda + premier ordre avec filter
        unvisited_neighbors = list(filter(lambda f : (f.x,f.y) not in [(case.x, case.y) for case in path], neighbors))
        for i in unvisited_neighbors:
            print ("unvisited neighbor : ", i.x, i.y)

        # si j'ai des voisins non visité
        if unvisited_neighbors:
            # je choisi un voisin au hasard sauf si c'est la sortie
            if escape in unvisited_neighbors:
                next_case = escape
            else:
                next_case = random.choice(unvisited_neighbors)
            print ("choix parmi :", [(case.x, case.y) for case in unvisited_neighbors])
            print ("next case : ", next_case.x, next_case.y, next_case.parent.x, next_case.parent.y)
            # je l'ajoute à mon chemin (path)
            if end != True:
                good_path.append(next_case)
            # et je l'ajoute aussi à la liste du bon chemin
            path.append(next_case)
            actual_case = next_case
            actual_case_index += 1
            print ("j'avance à la case : ", actual_case.x, actual_case.y)
            if next_case.x == escape.x and next_case.y == escape.y:
                print ("SORTIE WESH")
                end = True

        # sinon je retourne en arrière et je supprime la case actuelle de mon chemin
        else :
            actual_case_index -= 1
            if actual_case_index < 0:
                break
            actual_case = path[actual_case_index]
            print("Je retourne à la case précédente :", actual_case.x, actual_case.y)

            if end != True:
                good_path.pop()
        print("path :", [(case.x, case.y) for case in path])
        print ("good path : ", [(case.x, case.y) for case in good_path])
            
    return path, good_path

size = 50
def display_maze(labyrinthe, path):
    for i in labyrinthe:
        
        canevas.create_line(size*i.x,size*i.y,size*(i.x+1),size*(i.y), fill = "red")
        canevas.create_line(size*i.x,size*i.y,size*(i.x),size*(i.y+1), fill = "red")
    #Triche graphique pour fermer le labyrinthe et faire les ouvertures :)
    canevas.create_line(0,500,450,500, fill = "red")
    canevas.create_line(500,0,500,500, fill = "red")
    canevas.create_line(0,0,0,50, fill = "Ivory")

    for i in path:
        print(i.x,i.y,i.from_direction)
        if i.from_direction == "N":
            print("NOOOORTH")
            canevas.create_line (size*i.x,size*i.y,size*(i.x+1),size*i.y, fill="Ivory")
        if i.from_direction == "S":
            canevas.create_line (size*i.x,size*(i.y+1),size*(i.x+1),size*(i.y+1), fill="Ivory")
        if i.from_direction == "E":
            canevas.create_line (size*(i.x+1),size*i.y,size*(i.x+1),size*(i.y+1), fill="Ivory")
        if i.from_direction == "O":
            canevas.create_line (size*i.x,size*i.y,size*i.x,size*(i.y+1), fill="Ivory")
        


size_maze = 10
# on génère la grille
labyrinthe = generate_list(size_maze, size_maze)
print ("Labyrinthe : ", [(case.x, case.y) for case in labyrinthe])
# on parcourt la grille
#go_through_list(labyrinthe)
# on choisi une case de départ
first_case = Case(0, 0)
# on choisi un case d'arrivée
escape_case = Case(4,4)
# on génère le chemin
path, good_path = generate_path(first_case, size_maze, size_maze, escape_case, labyrinthe)

# on affiche le constructeur
#print ("Constructeur : ", [(case.x, case.y) for case in path])
# on affiche le chemin
#print ("Chemin : ", [(case.x, case.y) for case in good_path])

root = Tk()

root.title("Welcome to the Maze")
root.geometry('800x800')
button = Button(root, text = "Generate Maze", fg = "red", command = lambda : display_maze(labyrinthe, path) )
button.pack()

canevas = Canvas(root, width=501, height=501,bg = "ivory", borderwidth= -2)
canevas.pack()



root.mainloop()

