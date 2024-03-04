#Regner ut alle tallene 10 - 1 - tall1
tall1 = 1
for tall2 in range(10, 1, -1):
    #Bruker f-string så koden for utskrift blir lettere å lese
    print(f'{tall2} - {tall1} = {tall2-tall1}')