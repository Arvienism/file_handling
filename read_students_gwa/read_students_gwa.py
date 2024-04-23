# start:
#   create a text file that contains 20 students name and their gwa
#   read the text file
with open("read_students_gwa/students_gwa.txt", "r") as f:
    students = f.readlines() 
#   initialize variables for the name and gwa of the highest student
highest_student= ""
max_gwa = 1
#   create a loop to find the highest gwa and name
for info in students:
    name, gwa = info.split() #split the name and gwa from text file
    gwa = float(gwa) #convert string to float
#       check if the student's gwa is the highest
#   print the student with highest gwa in a "MAANGAS WAY" or "wow factor effect"