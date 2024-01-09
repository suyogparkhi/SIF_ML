import os
import psycopg2
from psycopg2 import sql
from config import config

# Define the file_types list
file_types = [
    {'table_name': 'text', 'file_extension': '.txt'},
    {'table_name': 'pdf', 'file_extension': '.pdf'},
    {'table_name': 'log', 'file_extension': '.log'},
    {'table_name': 'csv', 'file_extension': '.csv'},
    {'table_name': 'bin', 'file_extension': '.bin'},
    {'table_name': 'bk', 'file_extension': '.bk'},
    {'table_name': 'cfg', 'file_extension': '.cfg'},
    {'table_name': 'dbf', 'file_extension': '.dbf'},
    {'table_name': 'gz', 'file_extension': '.gz'},
    {'table_name': 'js', 'file_extension': '.js'},
    {'table_name': 'prj', 'file_extension': '.prj'},
    {'table_name': 'rpm', 'file_extension': '.rpm'},
    {'table_name': 'sh', 'file_extension': '.sh'},
    {'table_name': 'shp', 'file_extension': '.shp'},
    {'table_name': 'shx', 'file_extension': '.shx'},
    {'table_name': 'sql', 'file_extension': '.sql'},
    {'table_name': 'xlsx', 'file_extension': '.xlsx'},
]


folder_path_1 = 'C:\\Users\\ekans\\OneDrive\\Documents\\SIF 2023\\dataset1\\folder-1'
folder_path_2 = 'C:\\Users\\ekans\\OneDrive\\Documents\\SIF 2023\\dataset1\\folder-2'

def insert_file_paths(connection, folder_path, file_type, column_name):
    try:
        crsr = connection.cursor()

        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(file_type['file_extension']):
                    file_path = os.path.join(root, file)

                    query = sql.SQL("INSERT INTO files.{} ({}) VALUES (%s);").format(
                        sql.Identifier(file_type['table_name']),
                        sql.Identifier(column_name)
                    )
                    crsr.execute(query, (file_path,))
                    connection.commit()

                    print(f"File path added to database: {file_path}")

    except (Exception, psycopg2.DatabaseError) as error:
        return error

    finally:
        crsr.close()

def insert_files_for_folder(connection, folder_path, file_types, column_name):
    for file_type in file_types:
        insert_file_paths(connection, folder_path, file_type, column_name)


# MAIN Function
if __name__ == "__main__":
    connection = psycopg2.connect(**config())

    try:
        # Insert paths for folder 1
        insert_files_for_folder(connection, folder_path_1, file_types, 'f1')

        # Insert paths for folder 2
        insert_files_for_folder(connection, folder_path_2, file_types, 'f2')

    finally:
        if connection is not None:
            connection.close()
            print('Database connection terminated.')
