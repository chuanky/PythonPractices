import os

file = os.path.exists('a/b')

print(file)
cwd = os.getcwd()
os.makedirs(cwd + '/a/b')