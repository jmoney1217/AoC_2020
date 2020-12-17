#!/usr/bin/env python3
import sys


def validate(preamble, value):
    for i in preamble:
        for j in preamble:
            if (i + j) == value:
                return True
    return False

with open(sys.argv[1], 'r') as ifp:
    data = [int(x.strip()) for x in ifp.readlines()]

answer = 0

preamble_len = 25
index = preamble_len + 1
while index < len(data):
    preamble = data[index-preamble_len:index]
    if not validate(preamble, data[index]):
        answer = data[index]
        break
    index += 1

print('Answer 1: {}'.format(answer))

index = 0
answer2 = 0
for index in range(len(data)):
    sumlist = []
    index2 = index
    while True:
        tempsum = sum(sumlist)
        if tempsum == answer:
            # print('SUMLIST: {}'.format(sumlist))
            answer2 = min(sumlist) + max(sumlist)
            break
        elif tempsum > answer:
            break
        else:
            sumlist.append(data[index2])
            index2 += 1
    if answer2:
        break

print('Answer 2: {}'.format(answer2))






