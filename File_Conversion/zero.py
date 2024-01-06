path = 'file.0'
txt_file_path = 'output6.txt'

with open(path, 'r') as data:
    cont = data.read()

with open(txt_file_path, 'w') as txt_file:
    txt_file.write(cont)
