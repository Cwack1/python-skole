#Ganger "tall" med alle tallene fra 0 til 10
tall = 2
for ganger in range(0, 11):
    #Bruker f-string så koden for utskrift blir lettere å lese
    print(f'{tall} * {ganger} = {tall*ganger}')