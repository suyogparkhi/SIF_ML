import csv

def read_csv_file_columns(file_path, output_file=None):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader, None)
        rows = list(csv_reader)

        result = format_columns(header, rows)

        # Append result to the output file if specified
        if output_file:
            with open(output_file, 'a') as output:
                output.write(result + '\n')

        return result

def format_columns(header, rows):
    result = ""

    if header:
        result += f"Headers: {header}\n"

        for col_index, col_name in enumerate(header):
            result += f"Column {col_index + 1} ({col_name}): "
            result += ', '.join(row[col_index] for row in rows) + '\n'

    return result

# Example usage with appending to a file for printing columns from a CSV file
input_csv_file = 'dset_diabetes.csv'
output_log_file = 'output_log6.txt'

result_text = read_csv_file_columns(input_csv_file, output_file=output_log_file)
print(result_text)
