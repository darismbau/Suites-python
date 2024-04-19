print("Calcul du capital acquis et de ses intérêts versés lorsque les intérêts sont calculées une fois par an.")
cO=int(input("Entrer le placement de départ: "))
m=int(input("Entrer le montant du versement mensuel: "))
t=float(input("Entrer le taux annuel en %: "))
n=int(input("Entrer le nombre d'années: "))

def c(n):
    if n==0:
        return cO
    else:
        return ((c(n-1)+12*m)*(1+t/100))

print("Le capital acquis avec intérêts est de",round(c(n),2),"euros au bout de",n,"ans avec des versements mensuels de",m,"euros.")
print("Les intérêts gagnés au taux annuel de ",t,"% sont de",round(c(n)-n*m*12-cO,2),"euros.")
print("Sans placement avec intérêts le capital acqui serait de",round(n*m*12+cO,2),"euros.")

#Dans ce programme, la rélation de récurrence = Cn+1=(Cn+12xm)x(1+t/100).

#Ensuite, la question 2 :
print("Calcul du capital acquis et de ses intérêts versés lorsque les intérêts sont calculées une fois par an.")
cO=int(input("Entrer le placement de départ: "))
m=int(input("Entrer le montant du versement mensuel: "))
t=float(input("Entrer le taux annuel en %: "))
n=int(input("Entrer le nombre d'années: "))

def c(n):
    if n==0:
        return cO
    else:
        #return ((c(n-1)+12*m)*(1+t/100))
        return ((c(n-1)+m)*(1+t/100/12))

print("Le capital acquis avec intérêts est de",round(c(n*12),2),"euros au bout de",n,"ans avec des versements mensuels de",m,"euros.")
print("Les intérêts gagnés au taux annuel de ",t,"% sont de",round(c(n*12)-n*m*12-cO,2),"euros.")
print("Sans placement avec intérêts le capital acqui serait de",round(n*m*12+cO,2),"euros.")