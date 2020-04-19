import re

def compress_txt(txt_file):
    output = ''
    with open(txt_file, 'r') as file:
        for line in file.readlines():
            l = re.sub(r"\s+", "", line)
            output += l

    return output


txt_file = 'reference/pdfMiner/results/announcement.txt'
compressed_file = 'reference/pdfMiner/results/announcement_compressed.txt'

# with open(compressed_file, 'w') as file:
#     file.write(compress_txt(txt_file))

with open(compressed_file, 'r') as file:
    for line in file.readlines():
        print(line.find("刘秋香") != -1)
