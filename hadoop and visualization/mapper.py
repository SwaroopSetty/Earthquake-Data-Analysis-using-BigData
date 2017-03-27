#!/usr/bin/python

import sys
from csv import reader

for line in reader(sys.stdin):

    data = line
    if len(data) == 36:
     time, lat, a, b, c, d, e, f, g, h, temp, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, bb, cc, dd, ee, ff, gg, hh = data
     print '{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}'.format(time, g, temp, k, m, o, q, s, u, w, y, aa, cc)