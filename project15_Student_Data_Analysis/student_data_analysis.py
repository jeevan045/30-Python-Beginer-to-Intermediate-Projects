import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students_50.csv")

print(df.head())
print(df.describe())

avg_marks = df[['Math','Science','English']].mean()
print("Average Marks:\n", avg_marks)

df['Total'] = df[['Math','Science','English']].sum(axis=1)
top_student = df.loc[df['Total'].idxmax()]
print("Top Student:\n", top_student['Name'], "with total marks", top_student['Total'])

avg_marks.plot(kind='bar', title='Average Marks per Subject')
plt.ylabel("Marks")
plt.show()

df.plot(x='Name', y=['Math','Science','English'], kind='bar', title='Student Marks Comparison')
plt.ylabel("Marks")
plt.show()
