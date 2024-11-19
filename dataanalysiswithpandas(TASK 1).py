import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
print(df.head())
print(df.describe()) #give the columns that consist of numbers.

mv = df.isnull().sum()
print(mv) #gives the missing values in each columns.

avg= df['Age'].mean()#gives the average of a specific column;
print("Average of the Age is : ",{avg})

uniqueval = df['Age'].nunique()#gives the total number of unique values in a specified column

print("unique values in age are:", {uniqueval})

eng_empl = df[df['Department']=='Engineering'] #gives the details of the employee that are in the engineering department
print(eng_empl)

max_salary = df['Salary'].max()
max_salary_emp = df[df['Salary']==max_salary]
print(max_salary_emp) #gives the salary of the employee who is the highest paid

dep_count = df['Department'].value_counts()
print(dep_count) #gives the count of all the departments in the deparment column

sort = df.sort_values(by ='Age',ascending=False)
print(sort)#sort the data in desending order based on the age column

df['Experience']=df['Age'].apply (lambda x:'Senior' if x>=30 else 'Junior')
print(df) #adds a new column named experience based on the conditon of age

#DATA VISUALIZATION

plt.figure(figsize=(8,8))
plt.pie(dep_count,labels=dep_count.index,autopct='%1.1f%%',startangle=140)
plt.title('dept')
plt.show()
