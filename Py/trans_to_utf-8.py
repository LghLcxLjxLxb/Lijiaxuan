import pandas as pd

# 读取 CSV 文件
file_path = r'C:\Users\lenovo\Desktop\VScode\Python\lianjia_1.csv'  
data = pd.read_csv(file_path, encoding='utf-8-sig') # 使用 utf-8-sig 编码格式读取文件，去除 BOM

# 将数据另存为 UTF-8 编码格式（不带 BOM）
data.to_csv('utf8_without_BOM.csv', index=False, encoding='utf-8')  # 不使用 utf-8-sig 保存为普通的 UTF-8 编码格式
