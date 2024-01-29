import pandas as pd
data = {'FullName': ['Om-Ugale', 'Amit-Chaurasiya', 'Raj-Bose', 'Sanmay-Lahane', 'Sagar-Singh'],
        'Phone-no': [8975641234, 7894578946, 7894567842, 8755554694, 8889745761],
        'Address': ['Khamote', 'Vashi', 'Banglore', 'Ghansoli', 'Nerul'],
        'Medicine': ['Aspirin (Acetylsalicylic Acid)','Amoxicillin','Levothyroxine','Lisinopril','Ibuprofen',],
        'Aadhar-Card': ['4567-8912-3456', '7894-1234-4562', '2225-4578-6454', '5555-4545-1236', '1234-5747-8581'],
        'Date-of-Birth': ['2012-08-06', '1999-02-22', '2002-12-22', '2005-06-25', '2001-01-05'],}

df = pd.DataFrame(data)
result = df.loc[:, ['FullName', 'Phone-no', 'Address','Medicine','Aadhar-Card','Date-of-Birth']]
print(result)
print("\n")
#  CONCATENATION
result['Full_Info'] = df['FullName'] + ' lives at ' + df['Address']
print("Concatenation Result:")
print(result[['FullName', 'Address', 'Full_Info']])
print("\n")

# LENGTH
result['Medicine_Length'] = df['Medicine'].str.len()
print("Medicine Length Result:")
print(result[['Medicine', 'Medicine_Length']])
print("\n")

#  UPPER CASE
result['Upper_Name'] = df['FullName'].str.upper()
print("Upper Case Name Result:")
print(result[['FullName', 'Upper_Name']])
print("\n")

#  SPLIT
result['Address_Split'] = df['Address'].str.split('-')
print("Address Split Result:")
print(result[['Address', 'Address_Split']])
print("\n")
