import os

file_stat = os.stat('text_file.txt')
print(file_stat.st_size)