# -*- coding: utf-8 -*-

import sys

s = sys.argv[1]
# s= "Arisa Chue"

print("#1: " + s[2])
print("#2: " + s[4])
print("#3: " + str(len(s)))
print("#4: " + s[0])
print("#5: " + s[len(s)-1])
print("#6: " + s[len(s)-2])
print("#7: " + s[3: 8])
print("#8: " + s[-5:])
print("#9: " + s[2:])
print("#10: " + s[0::2])
print("#11: " + s[1::3])
print("#12: " + s[::-1])
print("#13: " + str(s.index(" ")))
print("#14: " + s[:-1])
print("#15: " + s[1:])
print("#16: " + s.lower())
print("#17: " + str(s.split()))
print("#18: " + str(len(s.split())))
print("#19: " + str(list(s)))
print("#20: " + "".join(sorted(s)))
print("#21: " + s.split(" ")[0])
print("#22: " + str(s == s[::-1]))