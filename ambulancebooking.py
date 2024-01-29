#Intrigity Constraints SQL queries

import pandas as pd
data = {'FullName': ['Om-Ugale', 'Amit-Chaurasiya', 'Raj-Bose', 'Sanmay-Lahane', ''],
        'Phone-no': [8975641234, 7894578946, 8975641234, 8755554694, 8889745761],
        'Address': ['Khamote', 'Vashi', 'Banglore', 'Ghansoli', 'Nerul'],
        'Time': [12.5,8.25,-22.49,18.27,-10.43] }

df = pd.DataFrame(data)
result = df.loc[:, ['FullName', 'Phone-no', 'Address','Time']]
print(result)
print("\n")

duplicate_phone_numbers = df[df.duplicated(subset=['Phone-no'])]
if not duplicate_phone_numbers.empty:
    print("Warning: Duplicate phone numbers found.")
    print(duplicate_phone_numbers)
    print("\n")

negative_time_values = df[df['Time'] < 0]
if not negative_time_values.empty:
    print("Error: Negative time values found.")
    print(negative_time_values)
    print("\n")

missing_full_names = df[df['FullName'].isnull()]
if not missing_full_names.empty:
    print("Error: Missing values in FullName.")
    print(missing_full_names)
    print("\n")