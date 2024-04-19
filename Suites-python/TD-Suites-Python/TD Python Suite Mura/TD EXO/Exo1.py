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