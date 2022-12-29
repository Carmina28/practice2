# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

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