from re import findall
from time import localtime, strftime

counter_line = 2

# get current time and format
dt = strftime("%B %d, %Y @ %I:%M %p", localtime())

# open file
with open('README.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# get line
line = findall(r'\d+', lines[counter_line])
print(line)
# find numbers in line
num = list(map(int, line))
# counter +1
num[2] += 1
lines[counter_line] = f'        📮 Commit Counter: <a href="https://github.com/Javascript-void0/Javascript-void0/commits/main">#{num[2]}</a> ({dt})\n'

with open('README.md', 'w', encoding='utf-8') as f:
    f.writelines(lines)

f.close()