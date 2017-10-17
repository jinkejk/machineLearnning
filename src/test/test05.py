#!/usr/bin/env python3
#命令行运行
import sys

from test.test04 import _private


def test():
    args = sys.argv
    if len(args) == 1:
        print("one",args[0])
    elif len(args) == 2:
        print("two",args[1])
    else:
        print('more',args)

if __name__ == '__main__':
    test()

print('test04', _private(3))


