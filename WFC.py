import pandas as pd
import numpy as np

# 读取和解析第一个文件的函数
def parse_oxygen_coordinates(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    data = [line.strip().split() for line in lines[2:]]
    df = pd.DataFrame(data, columns=['Atom Number', 'X', 'Y', 'Z'])
    df[['X', 'Y', 'Z']] = df[['X', 'Y', 'Z']].astype(float)
    return df

# 读取和解析第二个文件的函数，特别注意处理逗号分隔的坐标数据
def parse_wannier_centers(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    data = []
    for line in lines[2:-1]:
        parts = line.strip().split()
        atom_number, projection, no = parts[:3]
        xyz = ' '.join(parts[3:6]).split(', ')  # 处理逗号分隔的坐标
        spread = parts[6]
        if len(xyz) == 3:
            data.append([atom_number, projection, no] + xyz + [spread])
    df = pd.DataFrame(data, columns=['Atom Number', 'Projection', 'NO.', 'X', 'Y', 'Z', 'Spread'])
    df[['NO.', 'X', 'Y', 'Z', 'Spread']] = df[['NO.', 'X', 'Y', 'Z', 'Spread']].astype(float)
    return df

# 解析两个文件
oxygen_df = parse_oxygen_coordinates('O_site.dat')  # 替换为实际文件路径
wannier_df = parse_wannier_centers('centre_site.dat')  # 替换为实际文件路径

# 合并数据框，基于原子编号
merged_df = pd.merge(wannier_df, oxygen_df, on='Atom Number', suffixes=('_Wannier', '_Atom'))

# 计算距离
merged_df['Distance'] = np.sqrt((merged_df['X_Wannier'] - merged_df['X_Atom'])**2 + 
                                (merged_df['Y_Wannier'] - merged_df['Y_Atom'])**2 + 
                                (merged_df['Z_Wannier'] - merged_df['Z_Atom'])**2)

# 输出到 CSV 文件
output_csv_path = 'atom_wannier_distances.csv'  # 替换为期望的输出文件路径
merged_df.to_csv(output_csv_path, index=False)

print(f"数据已成功保存到 {output_csv_path}")
