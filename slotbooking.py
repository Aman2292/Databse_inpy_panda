import pandas as pd
data = {'FullName': ['Om-Ugale', 'Amit-Chaurasiya', 'Raj-Bose', 'Sanmay-Lahane', 'Sagar-Singh'],
        'Phone-no': [8975641234, 7894578946, 7894567842, 8755554694, 8889745761],
        'Address': ['Khamote', 'Vashi', 'Banglore', 'Ghansoli', 'Nerul'],
        'Age': [12, 25, 22, 18, 23],
        'Aadhar-Card': ['4567-8912-3456', '7894-1234-4562', '2225-4578-6454', '5555-4545-1236', '1234-5747-8581'],
        'Date-of-Birth': ['2012-08-06', '1999-02-22', '2002-12-22', '2005-06-25', '2001-01-05'],
        'Doctor-Category': ['cardiologist', 'cardiologist', 'dermatologist', 'pediatrician', 'pediatrician'],
        'Symptoms': ['pain-in-heart', 'pain-in-heart', 'Ringworm', 'Weight-gain', 'Weight-loss']}
        

df = pd.DataFrame(data)
result = df.loc[:, ['FullName', 'Phone-no', 'Address','Age','Aadhar-Card','Date-of-Birth','Doctor-Category', 'Symptoms']]
print(result)
print("\n")

#Aggregate Function (COUNT): Count the number of rows in the DataFrame.
row_count = df.shape[0]
print(f"Number of rows in the DataFrame: {row_count}")
print("\n")

#Filter (WHERE): Select rows where the Age is greater than 20.
result_filter = df[df['Age'] > 20]
print("Rows where Age is greater than 20:")
print(result_filter)
print("\n")

#Group By and Aggregate (GROUP BY, COUNT): Count the number of occurrences of each 'Doctor-Category'.
doctor_category_count = df.groupby('Doctor-Category').size().reset_index(name='Count')
print("Count of occurrences of each Doctor-Category:")
print(doctor_category_count)
print("\n")

#Sort (ORDER BY): Sort the DataFrame by 'Date-of-Birth' in ascending order.
sorted_df = df.sort_values(by='Date-of-Birth')
print("DataFrame sorted by Date-of-Birth:")
print(sorted_df)
print("\n")

