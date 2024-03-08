# The-Maze
Projet programmation fonctionnelle : générateur de labyrinthes 
Réalisé par Adrien Calais et Eva Trapani

Notre projet consiste en un générateur de labyrinthes parfaits (possédants une seule sortie). La taille du labyrinthe est modulable et nous avons ajouté une interface graphique afin d'afficher le labyrinthe.

## Composition fonctionnelle 
- Fonction pure : "generate_list" - la génération de la liste formant une grille (taille variable)
- Fonction closure : "generate_path" - la génération du labyrinthe, liste de tuples possédant les coordonnées de chaque cases et nous retrouvons dans cette fonction la fonction "neighbor" qui nous permet de vérifier que nous avons parcouru tout le labyrinthe
- Fonction de premier ordre + anonyme : nous retrouvons ces fonctions sur la variable "unvisited_neighbors" où nous utilisons la fonction de premier ordre filter et une lambda à l'intérieur (anonyme)

## Conseil d'exécution
N'ayant pas tester d'autres IDE, nous développons sous VS Code, nous préconisons donc l'utilisation de ce même IDE pour la suite des explications (si vous voulez utiliser autre chose, on suppose qu'il faudra faire plus ou moins les mêmes manipulations).

## Pour exécuter notre projet
- Cliquez sur la flèche d'exécution de votre VS Code
- Un fenêtre Tkinter va s'ouvrir
- Cliquez sur le bouton "Generate Maze"
- Tadaaa le labyrinthe apparaît, saurez-vous le résoudre ?

## TIPS 
Vous pouvez modifier la taille de votre labyrinthe, pour se faire : 
- Rendez-vous d'abord à la ligne : 105
- Changez la valeur de "size" afin de modifier la taille des cases
- Puis rendez-vous dans le code à la ligne : 130
- Modifiez la valeur de "size_maze" 
- Nous vous conseillons de ne pas aller au delà de 50 (ça devient long)

