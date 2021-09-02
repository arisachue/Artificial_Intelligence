# -*- coding: utf-8 -*-

val = [("b", 2), ("d", 4), ("a", 1), ("c", 3)]
min_error = sorted(val, key=lambda c: c[1])
print(min_error)