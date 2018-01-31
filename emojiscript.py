#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import sys

emoji_list = [
    '👌', '👏', '😂', '😛', '💯',
    '😤', '😩', '🤔', '👀', '😳',
    '😜', '💩', '👻', '💪', '😏'
]


def emojify(raw_str):
    return ''.join([' %s ' % emoji_list[random.randint(
        0,
        len(emoji_list) - 1
    )] if random.getrandbits(1) and char == ' ' else char for char in raw_str])


def main(args):
    try:
        emojid = str(args[1])
    except IndexError:
        print('No arguments, exiting...')
        exit(1)
    except ValueError:
        print('Argument was not a sequence of characters, exiting...')
        exit(1)

    print(emojify(emojid))

if __name__ == '__main__':
    main(sys.argv)
