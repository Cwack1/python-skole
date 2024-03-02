#Basic math 

#Addisjon
def add_two_numbers(num1, num2):
    return num1 + num2

#print(add_two_numbers(2, 4))

#Subtraksjon
def sub_two_numbers(num1, num2):
    return num1 - num2

#print(sub_two_numbers(8, 5))

#Oddetall eller partall
def check_even_odd(number):
    #Hvis tallet "number" kan deles på 2 helt frem til 0 uten å bli desimaltall
    if number % 2 == 2:
        return "Even"
    else:
        return "Odd"
    