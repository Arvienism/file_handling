# pseudocode
#
# start:
#   prompts user to input a line
line = input("Enter line: ")
#   create a loop to write a line
for lines in line:
#       ask user if they want to create more lines
    try_again = input("Are there more lines (y/n)? ").lower()
#       prompts user to input no to stop the loop 
    if try_again != "y":
        break
#       write the inputted line to the mylife.txt
    else:
        with open("mylife.txt", "w") as my_file:
            my_file.write(line + '\n')
#       create an infinite loop to asks user for new multiple lines
while True:
#           prompts the user to input a  new line
    new_line = input("Enter line: ")
#           write the inputted new line to the mylife.txt
#           asks user if they want to create more lines
#           create a loop to know if the user wants to stop
#               prompts user to input no to stop the loop
#       break the infinite loop
# end: