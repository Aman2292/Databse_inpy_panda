import pandas as pd
data = {'FullName': ['Priya','Rajendra','Aishwarya','Meera','Siddharth'],
        'Phone-no': [8975641234, 7894578946, 7894567842, 8755554694, 8889745761],
        'Address': ['Khamote', 'Vashi', 'Banglore', 'Ghansoli', 'Nerul'],
        'Reports': ['Blood-test','X-Ray','Sonography','Memography','Urine-Test',],
        'Aadhar-Card': ['4567-8912-3456', '7894-1234-4562', '2225-4578-6454', '5555-4545-1236', '1234-5747-8581'],
        'Date-of-Birth': ['2012-08-06', '1999-02-22', '2002-12-22', '2005-06-25', '2001-01-05'],}

df = pd.DataFrame(data)
result = df.loc[:, ['FullName', 'Phone-no', 'Address','Reports','Aadhar-Card','Date-of-Birth']]
print(result)
print("\n")

#  Select rows where Reports is 'X-Ray'
query_1_result = df[df['Reports'] == 'X-Ray']
print("Query 1 Result:")
print(query_1_result)
print("\n")

#  Select rows where Age is greater than 30
query_2_result = df[df['Date-of-Birth'] < '2000-01-01']
print("Query 2 Result:")
print(query_2_result)
print("\n")

#  Count the occurrences of each type of report
report_counts = df['Reports'].value_counts().reset_index(name='Count')
print("Query 3 Result:")
print(report_counts)
print("\n")

# Select rows where Address contains 'Ghan'
query_4_result = df[df['Address'].str.contains('Ghan')]
print("Query 4 Result:")
print(query_4_result)
print("\n")