# start:
#   create text file named integers.txt that contains 20 integers
even_numbers = []
odd_numbers = []
#   read the integers.txt
with open("integers.txt", "r") as integers_file:
    number = integers_file.readlines()
#   convert the integers.txt to integer
for integers in number:
    integers = int(integers.strip())
#   separate the integers to even and odd
    if integers % 2 == 0:
        even_numbers.append(integers)
    else:
        odd_numbers.append(integers)
#   square all even integers
squared_of_even_integers = even_numbers ** 2
#   cube all the odd integers
cubed_of_odd_integers = odd_numbers ** 3
#   write all squared integers to double.txt
with open("double.txt", "w") as even_integers_file:
    for integers in even_numbers:
        even_integers_file.write(str(integers) + '\n')
#   write all cubed integers to triple.txt
# end: