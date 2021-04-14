from re import findall
from time import localtime, strftime

dt = strftime("%B %d, %Y @ %I:%M %p", localtime())

with open('README.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

temp = findall(r'\d+', lines[29])
num = list(map(int, temp))
num[0] += 1
lines[29] = f'Updated {num[0]} times, last update at {dt}\n'

with open('README.md', 'w', encoding='utf-8') as f:
    f.writelines(lines)