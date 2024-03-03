import random

class Case:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Première fonction pure !
def generate_list (x_max, y_max):
    labyrinthe = []
    for i in range (x_max):
        for j in range (y_max):
            case = Case(i, j)
            labyrinthe.append(case)
    
    return labyrinthe

labyrinthe = generate_list(5, 5)

def go_through_list (labyrinthe):
    for case in labyrinthe:
        print(case.x, case.y)


# Fonction Closure !
def generate_path (case):
    good_path = []
    good_path.append(case)

    def neighbor (case):
        neighbors = []
        # on ajoute les voisins (haut, bas, droite, gauche)
        neighbors.append(Case(case.x, case.y + 1))
        neighbors.append(Case(case.x, case.y - 1))
        neighbors.append(Case(case.x + 1, case.y))
        neighbors.append(Case(case.x - 1, case.y))
        return neighbors
    

    # on met la case de départ dans le chemin
    path = [case]

    # tant que j'ai des voisin à visiter
    while path: 
        # je récupère la case où je suis
        actual_case = path[-1]
        # je récupère ses voisins
        neighbors = neighbor(actual_case)
        # je crée une liste pour les voisins que j'ai pas visité
        unvisited_neighbors = []  
        # pour chaque voisin de ma case actuelle
        for n in neighbors:
            # si je n'ai pas encore visité ce voisin
            if n not in good_path:
                # je l'ajoute à ma liste de voisin non visité
                unvisited_neighbors.append(n)

        # si j'ai des voisins non visité
        if unvisited_neighbors:
            # je choisi un voisin au hasard
            next_case = random.choice(unvisited_neighbors)
            # je l'ajoute à mon chemin (path)
            path.append(next_case)
            # et je l'ajoute aussi à la liste du bon chemin
            good_path.append(next_case)
        else:
            # sinon je retourne en arrière et je supprime la case actuelle de mon chemin
            path.pop()

    return good_path


# on génère la grille
labyrinthe = generate_list(5, 5)
# on choisi une case de départ
first_case = Case(0, 0)
# on génère le chemin
path = generate_path(first_case)

# on affiche le chemin
for case in path:
    print(case.x, case.y)
    