
# Student Marks Matrix Analysis

# Input number of students and subjects
n = int(input("Enter number of students: "))
m = int(input("Enter number of subjects: "))

# Input student names
students = []
for i in range(n):
    name = input(f"Enter student {i+1} name: ")
    students.append(name)

# Input subject names
subjects = []
for j in range(m):
    sub = input(f"Enter subject {j+1} name: ")
    subjects.append(sub)

# Create marks matrix
marks = []

for i in range(n):
    row = []
    print(f"\nEnter marks for {students[i]}:")
    for j in range(m):
        mark = float(input(f"{subjects[j]}: "))
        row.append(mark)
    marks.append(row)

# Row-wise statistics
print("\n--- STUDENT WISE ANALYSIS ---")

totals = []
averages = []

for i in range(n):
    total = sum(marks[i])
    average = total / m

    totals.append(total)
    averages.append(average)

    print(students[i],
          "Total:", total,
          "Average:", round(average, 2))

# Column-wise statistics
print("\n--- SUBJECT WISE ANALYSIS ---")

subject_averages = []

for j in range(m):
    total = 0

    for i in range(n):
        total += marks[i][j]

    average = total / n
    subject_averages.append(average)

    print(subjects[j],
          "Total:", total,
          "Average:", round(average, 2))

# Find top performer
top_index = totals.index(max(totals))

print("\n--- TOP PERFORMER ---")
print("Student:", students[top_index])
print("Total Marks:", totals[top_index])
print("Average Marks:", round(averages[top_index], 2))

# Identify low-performing subjects
print("\n--- LOW PERFORMING SUBJECTS ---")

found = False

for j in range(m):
    if subject_averages[j] < 40:
        print(subjects[j],
              "Average:", round(subject_averages[j], 2))
        found = True

if not found:
    print("No low-performing subjects found.")

print("\nAnalysis Completed!")

