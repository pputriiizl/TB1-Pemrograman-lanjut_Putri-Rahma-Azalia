import re

with open('matrix.txt','r') as file:
    lines = file.readlines()

firts_input = lines[0].rstrip().split()
n = int(firts_input[0])
m = int(firts_input[1])

matrix = lines[1:]
encoded_list = list(zip(*matrix))
encoded_string = ''.join([''.join(item) for item in encoded_list])
pat = r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])+\b'
print(re.sub(pat,r' ',encoded_string))