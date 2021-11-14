from re import findall
from time import localtime, strftime

dt = strftime("%B %d, %Y @ %I:%M %p", localtime())

with open('README.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

temp = findall(r'\d+', lines[3])
num = list(map(int, temp))
num[0] += 1
lines[3] = f' 📮 Commit Counter: {num[0]} ({dt})\n'

with open('README.md', 'w', encoding='utf-8') as f:
    f.writelines(lines)