#!/usr/bin/env python
print 'Got this" " %s" ' % raw_input()

import sys
data = sys.stdin.readline()[:-1]
love = sys.stdin.readline()[:-1]

print 'The meaning of life is ',data, int(data) * 2
print 'Love thots %s ' % love
