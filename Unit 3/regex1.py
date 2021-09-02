# -*- coding: utf-8 -*-

import sys; args = sys.argv[1:]
idx = int(args[0])-30



myRegexLst = [
  r"/^0$|^100$|^101$/", #30
  r"/^[01]*$/",
  r"/[02468]$/m",
  r"/\w*[aeiou]\w*[aeiou]\w*/i",
  r"/^0$|^[1][01]*[0]$/",
  r"/^[01]*110[01]*$/", #35
  r"/^.{2,4}$/s",
  r"/^\d{3}\s*-?\s*\d\d\s*-?\s*\d{4}$/",
  r"/^.*?d\w*\b/mi",
  r"/^[01]?$|^0[01]*0$|^1[01]*1$/" #39
  ]



if idx < len(myRegexLst):
  print(myRegexLst[idx])