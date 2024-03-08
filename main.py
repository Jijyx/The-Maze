import random


class Case:
    def __init__(self, x, y, parent = None):
        self.x = x
        self.y = y
        self.parent = parent


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
            neighbors.append(Case(case.x + 1, case.y, case))  # bas
        if case.x - 1 >= 0:
            neighbors.append(Case(case.x - 1, case.y, case))  # haut
        if case.y + 1 < y_max:
            neighbors.append(Case(case.x, case.y + 1, case))  # droite
        if case.y - 1 >= 0:
            neighbors.append(Case(case.x, case.y - 1, case))  # gauche
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




# on génère la grille
labyrinthe = generate_list(5, 5)
print ("Labyrinthe : ", [(case.x, case.y) for case in labyrinthe])
# on choisi une case de départ
first_case = Case(0, 0)
# on choisi un case d'arrivée
escape_case = Case(4,4)
# on génère le chemin
path, good_path = generate_path(first_case, 5, 5, escape_case, labyrinthe)

# on affiche le constructeur (path)
print ("Constructeur : ", [(case.x, case.y) for case in path])
# on affiche le chemin (good_path)
print ("Chemin : ", [(case.x, case.y) for case in good_path])
