#1.2. Modifier le programme précédent pour qu'il calcule les termes de la suite $(u_n)$ définie par l'expression
#$u_n=\dfrac{2n^2-1}{n^2+2}$.

def u(n):
    return (2*n**2-1)/(n**2+2)
n=1
print(u(n))
n=10
print(u(n))
n=100
print(u(n))
n=1000
print(u(n))

#1.3 Avec une boucle for: ajouter les deux lignes suivantes au programme précédent:
for n in range(1,10):
    print(u(n))
#La boucle for ici me permet de créer une boucle qui condense le programme consistant à faire le calcul de U1 à U10.



