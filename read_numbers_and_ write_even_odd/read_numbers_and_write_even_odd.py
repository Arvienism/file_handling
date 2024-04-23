# pseudocode

# start:
#   read the text file that contains 20 integer
with open("number.txt", "r") as f:
    numbers = f.readlines()
#   convert text file to integer
for num in numbers:
    numbers = [int(num.strip())]
#   separate the number to even and odd
#   write the even numbers to even.txt
#   write the odd numbers to odd.txt
# end: