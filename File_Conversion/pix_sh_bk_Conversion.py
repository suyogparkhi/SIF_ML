ip = "235434211_RAW_PAN.pix"
output_txt = "output.txt"
output_sh = "activate.sh"
output_bk = "gcp-collection_RAW_PAN-GCP.bk"
sh_to_txt = "convert_script.txt"
bk_to_txt = "backup_data.txt"

with open(ip, 'rb') as file:
    data = file.read()

width = 640
height = 480
pix = 3
pixels = [data[i:i + pix] for i in range(0, len(data), pix)]

# Ensure that each value in pixels is an integer in the range 0-255
pixels = [int.from_bytes(pixel, byteorder='big') for pixel in pixels]

# Save pixel values to a text file
with open(output_txt, 'w') as txt_file:
    for pixel in pixels:
        txt_file.write(f"{pixel}\n")

# Read content from .sh file and save to .txt
with open(output_sh, 'r') as sh_file, open(sh_to_txt, 'w') as sh_txt_file:
    sh_txt_file.write(sh_file.read())

# Read content from .bk file and save to .txt
with open(output_bk, 'rb') as bk_file, open(bk_to_txt, 'w') as bk_txt_file:
    bk_txt_file.write(bk_file.read().decode('utf-8'))
