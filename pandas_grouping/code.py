import pandas as pd

df = pd.DataFrame({
    'Student': ['A','B','C','D','E','F','G','H'],
    'Department': ['CSE','CSE','ECE','ECE','CSE','ECE','CSE','ECE'],
    'Gender': ['F','M','F','M','M','F','F','M'],
    'Marks': [85,72,91,65,78,88,95,70],
    'Attendance': [92,81,96,72,85,90,98,75]
})

# 1. Average marks for each department
dept_avg_marks = df.groupby('Department')['Marks'].mean()

print("1. Average marks by department:")
print(dept_avg_marks)


# 2. Average marks for each Department + Gender
group_avg = df.groupby(
    ['Department', 'Gender']
)['Marks'].mean()

print("\n2. Average marks by Department and Gender:")
print(group_avg)


# 3. Student with highest marks in each department
top_students = df.loc[
    df.groupby('Department')['Marks'].idxmax()
]

print("\n3. Highest marks in each department:")
print(top_students)


# 4. Students whose marks are above department average
department_average = df.groupby(
    'Department'
)['Marks'].transform('mean')

above_average = df[
    df['Marks'] > department_average
]

print("\n4. Students above department average:")
print(above_average)


# 5. Department with highest average attendance
attendance_avg = df.groupby(
    'Department'
)['Attendance'].mean()

print("\n5. Average attendance:")
print(attendance_avg)

print(
    "\nDepartment with highest average attendance:",
    attendance_avg.idxmax()
)