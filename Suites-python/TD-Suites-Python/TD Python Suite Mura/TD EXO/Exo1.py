print("Calcul d'un prêt immobilier ou d'un crédit à la consommation,")
s=int(input("Entrer le montant du prêt ou du crédit :"))
t=float(input("Entrer le taux annuel en %: "))
n=int(input("Entrez le nombre d'années:"))

#tm=(1+t/100)**(1/12)-1

tm=t/12/100
a=(1+tm)**(12*n)
m=s*tm*a/(a-1)
print("La mensualité avec intérêts est de ",round(m,2),"euros")
print("Le montant des intérêts remboursés sont de",round(m*12*n-s,2),"euros")
print("Le taux mensuel est de ", tm)
print("\nTableau d'amortissement:")
print("Mois - Mensualité - intérêts - Capital remboursé - Capital restant du - intérêts remboursés")
ir=0

for j in range(n*12):
    i=tm*s
    cr=m-i
    crd=s-cr
    ir=i+ir
    print("",j+1,"   -   ",round(m,1),"   -   ",round(i,1),"       -   ",round(cr,1),"             -   ",round(crd,1),"             -   ",round(ir,2))
    s=crd
    
print("Calcul d'un prêt immobilier ou d'un crédit à la consommation,") : Cette ligne affiche un message d'introduction pour indiquer que le programme va calculer les détails d'un prêt immobilier ou d'un crédit à la consommation.
s=int(input("Entrer le montant du prêt ou du crédit :")) : Cette ligne demande à l'utilisateur d'entrer le montant total du prêt ou du crédit en utilisant la fonction input(). La valeur est ensuite convertie en nombre entier avec int() et stockée dans la variable s.
t=float(input("Entrer le taux annuel en %: ")) : Cette ligne demande à l'utilisateur d'entrer le taux d'intérêt annuel en pourcentage. La valeur est ensuite convertie en nombre flottant avec float() et stockée dans la variable t.
n=int(input("Entrez le nombre d'années:")) : Cette ligne demande à l'utilisateur le nombre d'années sur lequel le prêt sera étalé. La valeur est convertie en entier avec int() et stockée dans la variable n.
tm=t/12/100 : Cette ligne calcule le taux d'intérêt mensuel à partir du taux annuel. Pour ce faire, le taux annuel (t) est divisé par 12 (nombre de mois) puis par 100 pour obtenir le taux sous forme décimale. Le résultat est stocké dans tm.
a=(1+tm)**(12*n) : Cette ligne calcule une variable intermédiaire a qui sera utilisée pour déterminer les mensualités. Elle prend en compte le taux mensuel et le nombre total de mois sur lesquels le prêt est réparti (12 mois par année multipliés par le nombre d'années).
m=s*tm*a/(a-1) : Cette ligne calcule la mensualité m en utilisant la formule du prêt amorti. Elle utilise le montant total du prêt, le taux mensuel, et la variable intermédiaire a.
print("La mensualité avec intérêts est de ",round(m,2),"euros") : Cette ligne affiche le montant de la mensualité, arrondi à deux chiffres après la virgule, avec une indication de devise ("euros").
print("Le montant des intérêts remboursés sont de",round(m*12*n-s,2),"euros") : Cette ligne affiche le montant total des intérêts remboursés sur toute la durée du prêt. Elle est calculée comme la différence entre le total des mensualités et le montant du prêt initial.
print("Le taux mensuel est de ", tm) : Cette ligne affiche le taux mensuel calculé précédemment.
print("\nTableau d'amortissement:") : Cette ligne ajoute un saut de ligne (\n) puis affiche le titre pour le tableau d'amortissement qui va suivre.
ir=0 : Cette ligne initialise la variable ir (intérêts remboursés) à zéro. Elle servira à accumuler les intérêts remboursés au fil du temps.
for j in range(n*12): : Cette ligne crée une boucle qui va itérer sur chaque mois du prêt, pour une durée totale de n*12 mois.
i=tm*s : Cette ligne calcule le montant des intérêts pour le mois en cours en multipliant le taux mensuel par le capital restant (s).
cr=m-i : Cette ligne calcule le montant du capital remboursé pour le mois en cours en soustrayant les intérêts de la mensualité.
crd=s-cr : Cette ligne calcule le capital restant dû après le remboursement du mois en cours.
ir=i+ir : Cette ligne met à jour la somme totale des intérêts remboursés en ajoutant les intérêts du mois en cours à ir.
print("",j+1," - ",round(m,1)," - ",round(i,1)," - ",round(cr,1)," - ",round(crd,1)," - ",round(ir,2)) : Cette ligne affiche une ligne du tableau d'amortissement, montrant le numéro du mois, le montant de la mensualité, les intérêts, le capital remboursé, le capital restant dû, et la somme des intérêts remboursés jusqu'à présent.
s=crd : Cette ligne met à jour le capital restant dû (s) avec la valeur calculée dans la variable crd. Ce sera utilisé pour le calcul du mois suivant.
