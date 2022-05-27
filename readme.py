from re import findall
from time import localtime, strftime

counter_line = 15 - 1

dt = strftime("%B %d, %Y @ %I:%M %p", localtime())

with open('README.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

temp = findall(r'\d+', lines[counter_line])
num = list(map(int, temp))
num[0] += 1
lines[counter_line] = f' 📮 Commit Counter: {num[0]} ({dt})\n'

with open('README.md', 'w', encoding='utf-8') as f:
    f.writelines(lines)