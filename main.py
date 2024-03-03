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
def generate_path (case, x_max, y_max):
    good_path = []
    good_path.append(case)

    def neighbor(case, x_max, y_max):
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
    path = [case]
    print ("first path : ", path[0].x, path[0].y)

    # tant que j'ai des voisin à visiter
    while path: 
        # je récupère la case où je suis
        actual_case = path[-1]
        print ("actual case : ", actual_case.x, actual_case.y)
        # je récupère ses voisins
        neighbors = neighbor(actual_case, x_max, y_max)
        for i in neighbors:
            print("neighbor : ", i.x, i.y)
        # je crée une liste pour les voisins que j'ai pas visité
        unvisited_neighbors = []  
        print("good_path avant l'itération sur les voisins :", [(case.x, case.y) for case in good_path])
        # pour chaque voisin de ma case actuelle
        for i in neighbors:
            # si je n'ai pas encore visité ce voisin
            if (i.x, i.y) not in [(case.x, case.y) for case in good_path]:
                # je l'ajoute à ma liste de voisin non visité
                unvisited_neighbors.append(i)
                print ("unvisited neighbor : ", i.x, i.y)

        # si j'ai des voisins non visité
        if unvisited_neighbors:
            # je choisi un voisin au hasard
            next_case = random.choice(unvisited_neighbors)
            # je l'ajoute à mon chemin (path)
            path.append(next_case)
            # et je l'ajoute aussi à la liste du bon chemin
            good_path.append(next_case)
            for i in good_path:
                print("good path : ", i.x, i.y)
        else:
            # sinon je retourne en arrière et je supprime la case actuelle de mon chemin
            path.pop()

    return good_path


# on génère la grille
labyrinthe = generate_list(5, 5)
# on parcourt la grille
go_through_list(labyrinthe)
# on choisi une case de départ
first_case = Case(0, 0)
# on génère le chemin
path = generate_path(first_case, 5, 5)

# on affiche le chemin
print ("Chemin : ")
for case in path:
    print(case.x, case.y)
    