#!/usr/bin/env python3
import sys


def split_list(a_list):
    half = len(a_list) // 2
    return a_list[:half], a_list[half:]


def reduce(data, code):
    action = code[0]
    left, right = split_list(data)
    if action in ['L', 'F']:
        if len(code) == 1:
            return left[0]
        return reduce(left, code[1:])
    elif action in ['R', 'B']:
        if len(code) == 1:
            return right[0]
        return reduce(right, code[1:])
    else:
        raise Exception('WTF')


with open(sys.argv[1], 'r') as ifp:
    lines = [x.strip() for x in ifp.readlines()]

answer = 0
answers = []
for line in lines:
    rows = [x for x in range(128)]
    cols = [x for x in range(8)]
    row = reduce(rows, line[:7])
    col = reduce(cols, line[7:])
    value = row * 8 + col
    answer = max(answer, value)
    answers.append(value)

print('Part 1 Answer: {}'.format(answer))

answers = sorted(answers)
answer = 0
while True:
    if answer not in answers and answer - 1 in answers and answer + 1 in answers:
        print('Part 2 Answer: {}'.format(answer))
        break
    answer += 1
