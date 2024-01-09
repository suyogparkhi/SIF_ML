import os
from dbfread import DBF
from pyproj import Proj

def convert_file_to_txt(input_file, output_txt):
    # Determine the file type based on the extension
    file_extension = os.path.splitext(input_file)[1].lower()

    if file_extension == '.dbf':
        records = list(DBF(input_file))
        with open(output_txt, 'w') as txt:
            for record in records:
                txt.write(str(record) + '\n')
    elif file_extension == '.prj':
        with open(input_file, 'r') as prj, open(output_txt, 'w') as txt:
            txt.write(prj.read())
    else:
        # For other file types, read in binary mode and write as text
        with open(input_file, 'rb') as file, open(output_txt, 'w') as txt:
            txt.write(str(file.read()))


# Specify your file paths
dbf_file = "BAND.dbf"
prj_file = "BAND.prj"
shp_file = "BAND.shp"
shx_file = "BAND.shx"
# lst_file = "your_file.lst"
# fio_file = "your_file.fio"
# crt_file = "your_file.crt"

# Specify output text file names
dbf_txt1 = "dbf_output1.txt"
prj_txt1 = "prj_output1.txt"
shp_txt1 = "shp_output1.txt"
shx_txt1= "shx_output1.txt"
# lst_txt = "lst_output.txt"
# fio_txt = "fio_output.txt"
# crt_txt = "crt_output.txt"

# Convert each file to text
convert_file_to_txt(dbf_file, dbf_txt1)
convert_file_to_txt(prj_file, prj_txt1)
convert_file_to_txt(shp_file, shp_txt1)
convert_file_to_txt(shx_file, shx_txt1)
# convert_other_to_txt(lst_file, lst_txt)
# convert_other_to_txt(fio_file, fio_txt)
# convert_other_to_txt(crt_file, crt_txt)
