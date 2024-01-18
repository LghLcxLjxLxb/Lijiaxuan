import chardet
import os

def detect_encoding(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            rawdata = f.read()
        result = chardet.detect(rawdata)
        return result['encoding']
    else:
        return None

file_path = r'C:\Users\lenovo\Desktop\VScode\Python\lianjia_2.csv'  
encoding = detect_encoding(file_path)
if encoding:
    print(f"The encoding of the file is: {encoding}")
else:
    print("File not found or path is incorrect.")
