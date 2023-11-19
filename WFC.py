import pandas as pd
import numpy as np

# A function that reads and parses the first file
def parse_oxygen_coordinates(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    data = [line.strip().split() for line in lines[2:]]
    df = pd.DataFrame(data, columns=['Atom Number', 'X', 'Y', 'Z'])
    df[['X', 'Y', 'Z']] = df[['X', 'Y', 'Z']].astype(float)
    return df

# A function that reads and parses the second file, paying special attention to working with comma-separated coordinate data
def parse_wannier_centers(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    data = []
    for line in lines[2:-1]:
        parts = line.strip().split()
        atom_number, projection, no = parts[:3]
        xyz = ' '.join(parts[3:6]).split(', ')  # Handles comma-separated coordinates
        spread = parts[6]
        if len(xyz) == 3:
            data.append([atom_number, projection, no] + xyz + [spread])
    df = pd.DataFrame(data, columns=['Atom Number', 'Projection', 'NO.', 'X', 'Y', 'Z', 'Spread'])
    df[['NO.', 'X', 'Y', 'Z', 'Spread']] = df[['NO.', 'X', 'Y', 'Z', 'Spread']].astype(float)
    return df

# parses two files
oxygen_df = parse_oxygen_coordinates('O_site.dat')  # Replace with the actual file path
wannier_df = parse_wannier_centers('centre_site.dat')  # Replace with the actual file path

# Merge data boxes, based on atomic numbers
merged_df = pd.merge(wannier_df, oxygen_df, on='Atom Number', suffixes=('_Wannier', '_Atom'))

# Calculate the distance between the atom and the Wannnier function centre
merged_df['Distance'] = np.sqrt((merged_df['X_Wannier'] - merged_df['X_Atom'])**2 + 
                                (merged_df['Y_Wannier'] - merged_df['Y_Atom'])**2 + 
                                (merged_df['Z_Wannier'] - merged_df['Z_Atom'])**2)

# Output CSV file
output_csv_path = 'atom_wannier_distances.csv'  # Replace with the desired output file path
merged_df.to_csv(output_csv_path, index=False)

print(f"The data was saved to {output_csv_path}")
