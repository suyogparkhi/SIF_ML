sp = 'table.sql'
txt_file_path = 'output5.txt'

with open(sp, 'r') as sp_file:
    data = sp_file.read()

with open(txt_file_path, 'w') as txt_file:
    txt_file.write(data)
