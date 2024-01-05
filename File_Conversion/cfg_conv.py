cfg_file_path = 'a.cfg'
txt_file_path = 'output3.txt'

with open(cfg_file_path, 'r') as cfg_file:
    cfg_content = cfg_file.read()

with open(txt_file_path, 'w') as txt_file:
    txt_file.write(cfg_content)
