# start:
#   create text file named integers.txt that contains 20 integers
even_numbers = []
odd_numbers = []
#   read the integers.txt
with open("integers.txt", "r") as integers_file:
    numbers = integers_file.readlines()
#   convert the integers.txt to integer
    for number in numbers:
        integers = int(number.strip())
#       separate the integers to even and odd
        if integers % 2 == 0:
            even_numbers.append(integers)
        else:
            odd_numbers.append(integers)
#   square all even integers
squared_of_even_integers = [x ** 2 for x in even_numbers]
#   cube all the odd integers
cubed_of_odd_integers = [x ** 3 for x in odd_numbers]
#   write all squared integers to double.txt
with open("double.txt", "w") as even_integers_file:
    for squared_integers in squared_of_even_integers:
        even_integers_file.write(str(squared_integers) + '\n')
#   write all cubed integers to triple.txt
with open("triple.txt", "w") as odd_integers_file:
    for cubed_integers in cubed_of_odd_integers:
        odd_integers_file.write(str(cubed_integers) + '\n')
# end: