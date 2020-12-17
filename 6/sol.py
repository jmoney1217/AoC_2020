#!/usr/bin/env python3
import sys


with open(sys.argv[1], 'r') as ifp:
    lines = [x.strip() for x in ifp.readlines()]

lines.append('')

answer = 0

chars = [x for x in 'abcdefghijklmnopqrstuvwxyz']
group_unions = []
group_union = set()
group_intersections = []
group_intersection = set(chars)
for line in lines:
    if not line:
        group_unions.append(group_union)
        group_intersections.append(group_intersection)
        group_union = set()
        group_intersection = set(chars)
    else:
        person = set([x for x in line])
        group_union = group_union.union(person)
        group_intersection = group_intersection.intersection(person)

tot = sum([len(x) for x in group_unions])

print('Part 1 Answer: {}'.format(tot))

tot = sum([len(x) for x in group_intersections])

print('Part 2 Answer: {}'.format(tot))
