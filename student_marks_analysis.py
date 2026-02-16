import numpy as np
#student names
students = np.array(['tom','sam','john','tony','josh'])
# marks matrix , rows student , column subject
marks = np.array([[67,78,88],
                  [77,87,82],
                  [56,88,92],
                  [89,91,93],
                  [86,73,89]])
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
