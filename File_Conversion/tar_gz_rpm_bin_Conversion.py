import os
import tarfile
import subprocess

def extract_tar_gz(file_path, extract_path):
    with tarfile.open(file_path, 'r:gz') as tar:
        tar.extractall(extract_path)

def extract_rpm(file_path, extract_path):
    # Use external tools rpm2cpio and cpio to extract RPM contents
    process = subprocess.Popen(['rpm2cpio', file_path], stdout=subprocess.PIPE)
    subprocess.Popen(['cpio', '-idmv', '-D', extract_path], stdin=process.stdout)

def process_file(input_file, output_file=None):
    _, file_extension = os.path.splitext(input_file)

    if file_extension == '.tar.gz':
        extract_path = 'extracted_folder'
        extract_tar_gz(input_file, extract_path)
        result = f"Extracted contents from {file_extension} file."

    elif file_extension == '.rpm':
        extract_path = 'extracted_folder'
        extract_rpm(input_file, extract_path)
        result = f"Extracted contents from {file_extension} file."

    elif file_extension in ('.bin', '.gz'):
        with open(input_file, 'rb') as binary_file:
            binary_data = binary_file.read()
        result = f"Processed content from {file_extension} file: {binary_data}"

    else:
        result = f"Unsupported file type: {file_extension}"

    # Append result to the output file if specified
    if output_file:
        with open(output_file, 'a') as output:
            output.write(result + '\n')

    return result

# Example usage with appending to a file
output_log_file = 'output_log.txt'

result_tar_gz = process_file('SR170158_ddn_showall_20210902-13_20_38.tar.gz', output_file=output_log_file)
result_rpm = process_file('example.rpm', output_file=output_log_file)
result_bin = process_file('example_binary_file.bin', output_file=output_log_file)

print(result_tar_gz)
print(result_rpm)
print(result_bin)
