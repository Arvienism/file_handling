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
            my_file.write("Enter line: " + line + '\n')
            my_file.write("Are there more lines (y/n)? " + try_again + '\n')
#       create an infinite loop to asks user for new multiple lines
    while True:
#           prompts the user to input a  new line
        new_line = input("Enter line: ")
#           asks user if they want to create more lines
        try_again_new = input("Are there more lines (y/n)? ").lower()
#           write the inputted new line to the mylife.txt
        with open ("mylife.txt", "a") as my_new_file:
            my_new_file.write("Enter line: " + new_line + '\n')
            my_new_file.write("Are there more lines (y/n)? " + try_again_new + '\n')
#           prompts user to input no, to determine when to stop asking 
        if try_again_new != "y": 
            break
#   break the infinite loop
    break
# end: