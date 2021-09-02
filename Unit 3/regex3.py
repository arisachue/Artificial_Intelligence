# -*- coding: utf-8 -*-

import sys; args = sys.argv[1:]
idx = int(args[0])-50


myRegexLst = [
  r"/\w*(\w)\w*\1\w*/i", #50(\w*(\w)*)*\2\w*, (\w*(\w)*)\1\w*
  r"/\w*(\w)(\w*\1){3}\w*/i",
  r"/^([01]|(0|1)[01]*\2)$/",
  r"/\b(?=\w*cat)\w{6}\b/i",
  r"/\b(?=\w*bri)(?=\w*ing)\w{5,9}\b/i",
  r"/\b(?!\w*cat)\w{6}\b/i", # 55
  r"/\b(?!\w*(\w)\w*\1)\w+/i",
  r"/^(?![01]*10011)[01]*$/",
  r"/(?=\w*([aeiou])(?!\1)[aeiou])\w*/i",
  r"/^(?![01]*(101|111))[01]*$/i" # 59
  ]


if idx < len(myRegexLst):
  print(myRegexLst[idx])