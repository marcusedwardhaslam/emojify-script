#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import sys

emoji_list = [
    '👌',
    '👏',
    '😂',
    '😛',
    '💯',
    '😤',
    '😩',
    '🤔',
    '👀',
]


def emojify(raw_str):
    rtn = ''
    for char in raw_str:
        insert_emoji = bool(random.getrandbits(1))  # boolean insert switch
        tmp = ' %s  ' % emoji_list[random.randint(
            0,
            len(emoji_list) - 1
        )] if insert_emoji and char == ' ' else char
        rtn += tmp
    return rtn

def main(args):
    try:
        emojid = str(args[1])
    except IndexError:
        print('No arguments, exiting...')
        exit(1)
    print(emojify(emojid))

if __name__ == '__main__':
    main(sys.argv)
