#Tar en brøk med teller og nevner og omgjør til desimaltall og prosent
teller = 2
nevner = 7

print(f'{teller}/{nevner} = ')
print(f'Desimaltall: {teller/nevner}')
print(f'Prosent: {str((teller/nevner)*100)}%')
#Funksjonen for avrunding er nyttig:
print(f'Rundes av til nærmeste desimaltall med to desimaler: {round(teller/nevner, 2)}')