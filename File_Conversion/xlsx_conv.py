import pandas as pd

xlsx_file_path = 'a.xlsx'
txt_file_path = 'output2.txt'

df = pd.read_excel(xlsx_file_path)

df.to_csv(txt_file_path, sep='\t', index=False)
