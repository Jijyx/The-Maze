import random

class Case:
    def __init__(self, x, y):
        self.x = x
        self.y = y


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

    def neighbor(case, x_max, y_max, escape, labyrinthe):
        neighbors = []
        # on ajoute les voisins (haut, bas, droite, gauche)
        if case.x + 1 < x_max:
            neighbors.append(Case(case.x + 1, case.y))  # bas
        if case.x - 1 >= 0:
            neighbors.append(Case(case.x - 1, case.y))  # haut
        if case.y + 1 < y_max:
            neighbors.append(Case(case.x, case.y + 1))  # droite
        if case.y - 1 >= 0:
            neighbors.append(Case(case.x, case.y - 1))  # gauche
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
        neighbors = neighbor(actual_case, x_max, y_max, escape, labyrinthe)
        for i in neighbors:
            print("neighbor : ", i.x, i.y)
        # je crée une liste pour les voisins que j'ai pas visité
        unvisited_neighbors = []  
        
        
        # pour chaque voisin de ma case actuelle
        for i in neighbors:
            # si je n'ai pas encore visité ce voisin
            if (i.x, i.y) not in [(case.x, case.y) for case in path]:
                # je l'ajoute à ma liste de voisin non visité
                unvisited_neighbors.append(i)
                print ("unvisited neighbor : ", i.x, i.y)

        # si j'ai des voisins non visité
        if unvisited_neighbors:
            # je choisi un voisin au hasard sauf si c'est la sortie
            if escape in unvisited_neighbors:
                next_case = escape
            else:
                next_case = random.choice(unvisited_neighbors)
            print ("choix parmi :", [(case.x, case.y) for case in unvisited_neighbors])
            print ("next case : ", next_case.x, next_case.y)
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


# def generate_labyrinth_grid(nb_rows, nb_columns):
#     labyrinth_grid = []

#     # on commence par faire la première ligne de murs du haut
#     # donc on répète +--- autant de fois qu'il y a de colonnes et on ajoute un + pour fermer
#     row_content = ['+---'] * nb_columns + ['+']
#     labyrinth_grid.append(row_content)

#     # on fait les lignes de cases et de murs
#     # donc on répète |   autant de fois qu'il y a de colonnes et on ajoute un | pour fermer
#     # puis on répète +--- autant de fois qu'il y a de colonnes et on ajoute un + pour fermer
#     for i in range(nb_rows):
#         row_content = ['|   '] * nb_columns + ['|']
#         labyrinth_grid.append(row_content)
#         row_content = ['+---'] * nb_columns + ['+']
#         labyrinth_grid.append(row_content)

#     # on affiche la grille ligne par ligne
#     for row in labyrinth_grid:
#         print(''.join(row))
    
#     return labyrinth_grid

def generate_labyrinth_grid(nb_rows, nb_columns, path, good_path):
    labyrinth_grid = []

    row_content = ['+']
    # on regarde la liste de path, si la coordonnée x a +1 alors on enlève le mur de droite
    # si la coordonnée x a -1 alors on enlève le mur de gauche
    for i in range(nb_rows):
        # si la coordonnée y = 0 alors on met un mur en haut
        if path[i].y == 0:
            row_content = ['+---'] * nb_columns + ['+']
        else:
            row_content = ['+   '] * nb_columns + ['+']
        labyrinth_grid.append(''.join(row_content))
        # si la coordonnée x = 0 alors on met un mur à gauche
        if path[i].x == 0:
            row_content = ['|'] 
        else:
            row_content = [' ']
        labyrinth_grid.append(''.join(row_content))
        if path[i].x != 0 and path[i].y != 0:
            # si la coordonnée x de la case suivante est +1 alors on enlève le mur de droite
            if good_path[i].x + 1 == good_path[i + 1].x:
                row_content.append('    ')
            else:
                row_content.append('   |')
            labyrinth_grid.append(''.join(row_content))
            # si la coordonnée y de la case suivante est +1 alors on enlève le mur du bas
            if good_path[i].y + 1 == good_path[i + 1].y:
                row_content = ['   +']
            else:
                row_content = ['---+']
            labyrinth_grid.append(''.join(row_content))


    # on affiche la grille ligne par ligne
    for row in labyrinth_grid:
        print(''.join(row))
    
    return labyrinth_grid





# on génère la grille
labyrinthe = generate_list(5, 5)
print ("Labyrinthe : ", [(case.x, case.y) for case in labyrinthe])
# on parcourt la grille
go_through_list(labyrinthe)
# on choisi une case de départ
first_case = Case(0, 0)
# on choisi un case d'arrivée
escape_case = Case(4,4)
# on génère le chemin
path, good_path = generate_path(first_case, 5, 5, escape_case, labyrinthe)

# on affiche le constructeur
print ("Constructeur : ", [(case.x, case.y) for case in path])
# on affiche le chemin
print ("Chemin : ", [(case.x, case.y) for case in good_path])

# on affiche le labyrinthe
print("\nLabyrinthe : ")
labyrinth_grid = generate_labyrinth_grid(5, 5, path, good_path)
