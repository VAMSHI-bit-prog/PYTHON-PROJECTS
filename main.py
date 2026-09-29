import numpy as np
students = np.array(["Vamsi" , "Vinay" , "geethu" , "habimunnisa" , "renusri"])
subjects = np.array(["MATH" , "SCIENCE" , "HISTORY"])
marks = np.array([
    [85, 90, 78],
    [70, 65, 80],
    [95, 92, 98],
    [60, 75, 68],
    [88, 84, 90]])

print(f"students: {students}")
print(f"sujects: {subjects}")
print(f"marks respectively: \n{marks}")

pass_average_marks = 75

total_marks = np.sum(marks,axis=1)
total_average = np.mean(marks, axis=1)
a = max(total_marks)
for i in range(len(students)):
    if total_marks[i] == a:
        Topper = students[i]

print("\n......Students performance......")
for i in range(len(students)):
    print(students[i])
    print(f"Total marks = {total_marks[i]}")
    print(f"Average marks = {total_average[i]}")

print(f"\nTopper of the list is {Topper}")

x = 0
y = 0

for i in range(len(students)):
    if total_average[i] < pass_average_marks:
        x+= 1
    else:
        y+= 1

print(f"\nThe number of students passed their test: {y}")
print(f"The number of students failed their test: {x}")

subject_average = np.mean(marks,axis = 0)

for i in range(len(subjects)):
    print("\nSubject wise class average:")
    print(f"subject: {subjects[i]}")
    print(f"Average marks: {subject_average[i]}")

sum = (np.sum(total_marks))/marks.size
print(f"\nOverall class average is: {sum}")