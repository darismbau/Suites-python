#2.1 Qu'affiche le programme suivant ?

def u(n):
    if n==0:
        return 2
    else:
        return 3*u(n-1)-2

print(u(0))
print(u(1))
print(u(2))

n=10
print(u(n))

#La fonction définie et utilisée ici s'appelle une fonction récursive: c'est une fonction qui s'appelle elle-même…
#La formule algébrique definissant la suite Un de ce programme est : U0 = 2 & Un+1 = 3xU(n-1)-2