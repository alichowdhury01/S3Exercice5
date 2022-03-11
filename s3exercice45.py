#Créez une fonction demandant à un utilisateur un nombre pair et un nombre impair, 
# une fonction permettant de vérifier que les nombres ne sont pas les deux pairs ou impairs, 
# et affichez la phrase suivante: Votre nombre impair est le x, votre nombre pair est le y 
# et le résultat de leur division est égal à z. Vous ne devez qu'afficher 3 chiffres après le point.

#Fonction demandant à un utilisateur un nombre pair et un nombre impair:

def nb_input():
    return nb_input(nb_pair, nb_impair)

nb_pair = int(input("Veillez entrez un nombre pair: "))
nb_impair = int(input('Veuillez entrer un nombre impair: '))

nb_input()

#Fonction permettant de vérifier que les nombres ne sont pas les deux pairs ou impairs:

