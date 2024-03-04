#Regner ut alle tallene 0 - 9 + tall1
tall1 = 1
for tall2 in range(10):
    #Bruker f-string så koden for utskrift blir lettere å lese
    print(f'{tall1} + {tall2} = {tall1+tall2}')