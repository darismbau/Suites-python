#1.1
#Définition d'une suite explicite, à partir d'une fonction - Boucles et détermination d'un seuil
#L'instruction def permet de définir une fonction en python. (voir éventuellement, en complément, les fonctions en python)
#Qu'affiche le programme suivant ? (en python, * désigne la multiplication: 3*2 vaut 6, et ** désigne la puissance: 3**2 vaut 9)
#L'equation algebrique est (0.2Xn^2)-2
def u(n):
    return 0.2*n**2-2
print(u(2))

n=10
print(u(n))
n=25
print(u(n))
n=1
print(u(n))

#1.4 Détermination d'un seuil: boucle while. Pour quelle valeur de n, les valeurs un de la suite de la question 1. dépassent-elles 1000 ?
#Déterminer la valeur algébriquement, par le calcul.
#Ajouter ensuite dans le programme précédent les quelques lignes suivantes:

n=1000
while u(n)<1000:
   print(u(n))
   n=n+1
print(n)