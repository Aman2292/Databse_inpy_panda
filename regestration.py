#Where Clause and Search condition in SQL

import pandas as pd

data = {'Name': ['omugale', 'wiz', 'aman', 'sanmay', 'suhesh'],
        'Email': ['omugale@gmail.com', 'wizard@gmail.com ', 'chaurasiyaaman110@gmail.com', 'sanmay123@gmail.com', 'suhesh@gmail.com'],
        'Pass': ['omug1010', 'wiz124wiz', 'aman98chaurasiya', 'sanm123', 'qewrtty12']}

df = pd.DataFrame(data)

result = df.loc[:, ['Name', 'Email', 'Pass']]

print(result)
print("\n")
result_query_1 = df.query('Name == "omugale"')

result_query_2 = df.query('Pass == "qewrtty12"')
print("Query 1 Result:")
print(result_query_1)
print("\n\n")

print("\nQuery 2 Result:")
print(result_query_2)
print("\n\n")