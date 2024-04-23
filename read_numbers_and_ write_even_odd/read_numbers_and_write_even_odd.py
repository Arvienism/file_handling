# pseudocode

# start:
even_numbers = []
odd_numbers = []

#   read the text file that contains 20 integer
with open("number.txt", "r") as f:
    numbers = f.readlines()
#   convert text file to integer
numbers = []
for num in numbers:
    numbers = int(num.strip())
#   separate the number to even and odd
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
#   write the even numbers to even.txt
#   write the odd numbers to odd.txt
# end: