import psycopg2

db_params = {
    'host': 'lala',
    'database': 'lolo',
    'user': 'pandee',
    'password': 'chutiya'
}

def convert_file_to_txt(file_name):
    # line wise eak hi txt file me dalege to space bachegi and minhash efficiently kam karega
    txt_file_path = 'output.txt'

    with open(file_name, 'r') as data:
        content = data.read()

    with open(txt_file_path, 'w') as txt_file:
        txt_file.write(content)

connection = psycopg2.connect(**db_params)

cursor = connection.cursor()

cursor.execute("SELECT file_name FROM files")

file_names = cursor.fetchall()

for name in file_names:
    convert_file_to_txt(name[0])

cursor.close()
connection.close()
