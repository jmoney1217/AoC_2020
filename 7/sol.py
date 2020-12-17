#!/usr/bin/env python3
import sys, re

def find_all_containing_bags(data, color, all_colors=None):
    all_colors = set([color])
    for bag, subs in data.items():
        if color in subs:
            all_colors = all_colors.union(find_all_containing_bags(data, bag, all_colors))
    return all_colors

def count_all_nested_bags(data, color):
    total = 1
    for sub, count in data[color].items():
        total += count * count_all_nested_bags(data, sub)
    return total

regex1 = re.compile('(.*?) bags contain (.*)')
regex2 = re.compile('(?:no other|(\d+) (\S+ \S+)) bag')

with open(sys.argv[1], 'r') as ifp:
    lines = [x.strip() for x in ifp.readlines()]

answer = 0

data = {}
for line in lines:
    print(line)
    bag, nested = regex1.match(line).groups()
    print(bag)
    print(nested)
    bags = regex2.findall(nested)
    subs = {}
    for y, x in bags:
        try:
            subs[x] = int(y)
        except ValueError:
            pass

    data[bag] = subs

all_colors = find_all_containing_bags(data, 'shiny gold')
all_colors.remove('shiny gold')

print('Answer 1: {}'.format(len(all_colors)))

total = count_all_nested_bags(data, 'shiny gold')
print('Answer 2: {}'.format(total - 1))


