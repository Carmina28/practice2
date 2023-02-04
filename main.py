
"""
Multiples lineas de comentarios
Comentario1
Comentario2
"""

#variables
age = 15
name = "Maria"
mayorEdad = "Es mayor de edad"
menorEdad = "Es menor de edad"
#Concatenar
print(f"{name} {mayorEdad}")

#Concatenar un entero
print(f"{name} tiene {str(age)}, {mayorEdad}")

#Concatenar con el +
print(name+", " + mayorEdad)

#Indentar/Tabular

#Conditionales


if (age>18):
    print(mayorEdad)
else:
    print(menorEdad)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#For loop
numbers = [1, 2, 3, 4, 5]
for item in numbers:
    print(item)

# While loop
i = 0
while i <= 10:
    print(i * '*`')
    i = i + 1
#Common to see range function with for loop
#number = range(5,10,2)
#for numb in number:
#    print(numb)

#is common to see range function with for loop
#we  can call the range function directly
for numb in range(5):
    print(numb)


#() to define a tuple, parentesis, they are used to store sequence of objects, but they are inmutable
#only have count and index method
#count return the number of ocurrences of a element
#index returns the index of the first ocurrence of the given element
#NOTE: magic methods _add_