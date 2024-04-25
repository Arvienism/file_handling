# start:
#   create text file named integers.txt that contains 20 integers
#   read the integers.txt
with open("integers.txt", "r") as integers_file:
    number = integers_file.readlines()
#   convert the integers.txt to integer
for integers in number:
    integers = int(integers.strip())
#   separate the integers to even and odd
#   square all even integers
#   cube all the odd integers
#   write all squared integers to double.txt
#   write all cubed integers to triple.txt
# end: