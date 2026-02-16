import numpy as np

n = int(input("enter number of student:"))
s = int(input("enter number of subject:"))

student = []
mark_list = []

for i in range(n):
  name = input(f"\nstudent name {i+1} : ")
  student.append(name)

  student_marks = []
  for j in range(s):
    while True:
        mark = int(input(f"\nenter marks of subject {j+1} : "))

        if 0 <= mark <= 100:
          student_marks.append(mark)
          break
        else:
          print("Marks must be between 0 and 100. Try again")

  mark_list.append(student_marks)

students = np.array(student)
marks = np.array(mark_list)

print("original matrix:")
print(marks)

# row-wise total
total_marks = np.sum(marks,axis=1)
print("\ntotal marks:",total_marks)

# row-wise average
average_marks = np.mean(marks,axis=1)
print("\naverage marks:",average_marks)

# column-wise average
subject_average = np.mean(marks,axis=0)
print("\nsubject average:",subject_average)

# toper & lower
toper_index = np.argmax(average_marks)
lower_index = np.argmin(average_marks)

print("toper:",students[toper_index])
print("lowscorer:",students[lower_index])

print("\nGrades:")
for i in range(len(students)):
  avg = average_marks[i]
  if avg >= 90:
    grade = "A+"
  elif avg >= 80:
    grade = "A"
  elif avg >= 70:
    grade = "B"
  elif avg >= 60:
    grade = "C"
  else:
    grade = "D"

  print(students[i], ":", grade)
