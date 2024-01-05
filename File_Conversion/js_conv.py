log_file_path = 'a.js'
txt_file_path = 'output1.txt'

with open(log_file_path, 'r') as log_file:

    log_contents = log_file.read()

with open(txt_file_path, 'w') as txt_file:

    txt_file.write(log_contents)
