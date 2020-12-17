#!/usr/bin/env python3
import sys, re

regex1 = re.compile('(\S+) ((?:[\+\-])\S+)')

with open(sys.argv[1], 'r') as ifp:
    lines = [x.strip() for x in ifp.readlines()]

answer = 0

ops = []
for line in lines:
    # print(line)
    match = regex1.match(line)
    op = match.group(1)
    num = int(match.group(2))
    ops.append((op, num))
ops.append(('end', 0))

def play(ops):
    played = []
    index = 0
    acc = 0

    while index not in played:
        played.append(index)
        op, num = ops[index]
        # print('play {}: {} {}'.format(index, op, num))
        if op == 'acc':
            acc += num
            index += 1
        elif op == 'jmp':
            index += num
        elif op == 'nop':
            index += 1
        elif op == 'end':
            return acc
        else:
            raise Exception('wtf')
    raise Exception(acc)

try:
    play(ops)
except Exception as e:
    print('Answer 1: {}'.format(e))
else:
    print('NO INFINITE LOOP WTF')
    sys.exit(1)


index = 0
while index < len(ops):
    testops = [ x for x in ops ]
    if testops[index][0] == 'nop':
        testops[index] = ('jmp', testops[index][1])
        try:
            print('Answer 2: {}'.format(play(testops)))
            print('Changed {} from nop to jmp'.format(index))
            sys.exit(0)
        except Exception as e:
            pass
    index += 1

index = 0
while index < len(ops):
    testops = [ x for x in ops ]
    if testops[index][0] == 'jmp':
        testops[index] = ('nop', testops[index][1])
        try:
            print('Answer 2: {}'.format(play(testops)))
            print('Changed {} from jmp to nop'.format(index))
            sys.exit(0)
        except Exception as e:
            pass
    index += 1

print('WTF')
sys.exit(1)

