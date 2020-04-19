import json
import re

curdir = 'reference/jsonExamples'
file_path = curdir + '/链接.txt'

def preprocess(file_path):
    '''移除所有空格'''
    result = ''
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            result += line
    
    result = re.sub(r'\s+', '', result)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(result)

    print('file has been preprocessed')
    

def json_load(file_path):
    '''读取一个文本文件，返回一个字符串'''
    with open(file_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    return json_data

def find_by_re(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        line = file.readline()
        urls = re.findall(r'"adjunctUrl":".*?"', line)

    return urls

# 文档预处理
# preprocess(file_path)

# 正则表达匹配
links = find_by_re(file_path)
for link in links:
    print(link)

print(len(links))

# json匹配
# json_data = json_load(file_path)
# announcements = json_data['announcements']

# for announcement in announcements:
#     print(announcement['adjunctUrl'])

# print(len(announcements))