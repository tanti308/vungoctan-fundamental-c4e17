subjects=['CompSci','Physics','Maths','Stats','Accounting','Economics','Management','CommLaw','Music','Sociology','Law','InfSys','x']
# students = [
#     ("John", ["CompSci", "Physics"]),
#     ("Vusi", ["Maths", "CompSci", "Stats"]),
#     ("Jess", ["CompSci", "Accounting", "Economics", "Management"]),
#     ("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),
#     ("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])]
subjects.remove("Physics")
subjects.pop()
print(subjects)
# Count how many students are taking CompSci
# counter = 0
# for (name, subjects) in students:
#     if "CompSci" in subjects:
#         counter += 1
#
# print("The number of students taking CompSci is", counter)
