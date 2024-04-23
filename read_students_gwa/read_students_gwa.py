# start:
from art import *
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
    if gwa <= max_gwa:
        max_gwa = gwa
        highest_student = name
#   print the student with highest gwa in a "MAANGAS WAY" or "wow factor effect"
title = text2art("Student with highest GWA")
print(title)
student_name = text2art(highest_student, font="block")
print(student_name)
student_gwa = text2art("{:.2f}".format(max_gwa))
print(student_gwa)