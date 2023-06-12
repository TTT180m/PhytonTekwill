"""
Un utilizator va introduce un sir de numere, separate prin virgula de la consola.
Din sirul introdus creaza o lista de numere.
Afla suma elementelor pare si a celor impare din lista si afiseazo.
"""

sir=list()
numere=input("Introdu sirul de numere prin virgula: ")
numere=numere.split(',')
sir.extend(numere)
suma_par=0
suma_impar=0

for numar in sir:
    numar=int(numar)
    if numar % 2 == 0:
        suma_par += numar
    else:
        suma_impar += numar

print(sir)
print("suma nr pare: ",suma_par)
print("suma nr impare: ",suma_impar)