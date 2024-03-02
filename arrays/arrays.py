#n^2 -> potenser i et array fra num1 til num2
def potenser(num1, num2):
    return [i**2 for i in range(num1, num2+1)]

#print(potenser(2,20))

#Sorter array fra lavest til høyest
def sort_numbers(numbers):
    return sorted(numbers)

#Sorter array fra høyest til lavest
def sort_numbers_rev(numbers):
    return sorted(numbers)[::-1]

#Importere bibliotek så vi kan bruke funksjonen "random"
import random
def create_random_array(size, lower, upper):
    #Lager en tom liste
    array = []
    for i in range(size):
        #Lager et tilfeldig nummber mellom "lower" og "upper"
        number = random.randint(lower, upper)
        #Legger til det tilfeldige tallet i listen
        array.append(number)
    return array

random_array = create_random_array(10, 1, 100)

print(random_array)
print(sort_numbers(random_array))
print(sort_numbers_rev(random_array))