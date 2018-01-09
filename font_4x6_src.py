#!/usr/bin/env python3
# -*- coding: UTF8 -*-

font_4x6_src = {
  0x0020: # ' ' "\u0020"
   ("        ",
    "        ",
    "        ",
    "        ",
    "        ",
    "        "),

  0x0021: # '!' "\u0021"
   ("        ",
    "  ()    ",
    "  ()    ",
    "  ()    ",
    "        ",
    "  ()    "),

  0x0022: # '"' "\u0022"
   ("        ",
    "()  ()  ",
    "()  ()  ",
    "        ",
    "        ",
    "        "),

  0x0025: # '%' "\u0025"
   ("        ",
    "()      ",
    "    ()  ",
    "  ()    ",
    "()      ",
    "    ()  "),

  0x0027: # ''' "\u0027"
   ("        ",
    "  ()    ",
    "  ()    ",
    "        ",
    "        ",
    "        "),

  0x0028: # '(' "\u0028"
   ("        ",
    "  ()    ",
    "()      ",
    "()      ",
    "()      ",
    "  ()    "),

  0x0029: # ')' "\u0029"
   ("        ",
    "  ()    ",
    "    ()  ",
    "    ()  ",
    "    ()  ",
    "  ()    "),

  0x002A: # '*' "\u002A"
   ("        ",
    "        ",
    "()  ()  ",
    "  ()    ",
    "()  ()  ",
    "        "),

  0x002B: # '+' "\u002B"
   ("        ",
    "        ",
    "  ()    ",
    "()()()  ",
    "  ()    ",
    "        "),

  0x002C: # ',' "\u002C"
   ("        ",
    "        ",
    "        ",
    "        ",
    "  ()    ",
    "()      "),

  0x002D: # '-' "\u002D"
   ("        ",
    "        ",
    "        ",
    "()()()  ",
    "        ",
    "        "),

  0x002E: # '.' "\u002E"
   ("        ",
    "        ",
    "        ",
    "        ",
    "        ",
    "  ()    "),

  0x002F: # '/' "\u002F"
   ("        ",
    "        ",
    "    ()  ",
    "  ()    ",
    "()      ",
    "        "),

  0x0030: # '0' "\u0030"
   ("        ",
    "()()()  ",
    "()  ()  ",
    "()  ()  ",
    "()  ()  ",
    "()()()  "),

  0x0031: # '1' "\u0031"
   ("        ",
    "    ()  ",
    "  ()()  ",
    "    ()  ",
    "    ()  ",
    "    ()  "),

  0x0032: # '2' "\u0032"
   ("        ",
    "()()()  ",
    "    ()  ",
    "()()()  ",
    "()      ",
    "()()()  "),

  0x0033: # '3' "\u0033"
   ("        ",
    "()()()  ",
    "    ()  ",
    "()()()  ",
    "    ()  ",
    "()()()  "),

  0x0034: # '4' "\u0034"
   ("        ",
    "()  ()  ",
    "()  ()  ",
    "()()()  ",
    "    ()  ",
    "    ()  "),

  0x0035: # '5' "\u0035"
   ("        ",
    "()()()  ",
    "()      ",
    "()()()  ",
    "    ()  ",
    "()()()  "),

  0x0036: # '6' "\u0036"
   ("        ",
    "()()()  ",
    "()      ",
    "()()()  ",
    "()  ()  ",
    "()()()  "),

  0x0037: # '7' "\u0037"
   ("        ",
    "()()()  ",
    "    ()  ",
    "    ()  ",
    "    ()  ",
    "    ()  "),

  0x0038: # '8' "\u0038"
   ("        ",
    "()()()  ",
    "()  ()  ",
    "()()()  ",
    "()  ()  ",
    "()()()  "),

  0x0039: # '9' "\u0039"
   ("        ",
    "()()()  ",
    "()  ()  ",
    "()()()  ",
    "    ()  ",
    "()()()  "),

  0x003A: # ':' "\u003A"
   ("        ",
    "        ",
    "  ()    ",
    "        ",
    "  ()    ",
    "        "),

  0x003B: # ';' "\u003B"
   ("        ",
    "        ",
    "  ()    ",
    "        ",
    "  ()    ",
    "()      "),

  0x003C: # '<' "\u003C"
   ("        ",
    "    ()  ",
    "  ()    ",
    "()      ",
    "  ()    ",
    "    ()  "),

  0x003D: # '=' "\u003D"
   ("        ",
    "        ",
    "()()()  ",
    "        ",
    "()()()  ",
    "        "),

  0x003E: # '>' "\u003E"
   ("        ",
    "()      ",
    "  ()    ",
    "    ()  ",
    "  ()    ",
    "()      "),

  0x003F: # '?' "\u003F"
   ("        ",
    "()()()  ",
    "    ()  ",
    "  ()    ",
    "        ",
    "  ()    "),

  0x0040: # '@' "\u0040"
   ("        ",
    "()()()  ",
    "()  ()  ",
    "()()()  ",
    "        ",
    "        "),
  
  0x0041: # 'A' "\u0041"
   ("        ",
    "  ()()  ",
    "()  ()  ",
    "()()()  ",
    "()  ()  ",
    "()  ()  "),
   
  0x0042: # 'B' "\u0042"
   ("        ",
    "()()    ",
    "()  ()  ",
    "()()    ",
    "()  ()  ",
    "()()    "),
   
  0x0043: # 'C' "\u0043"
   ("        ",
    "  ()()  ",
    "()      ",
    "()      ",
    "()      ",
    "  ()()  "),
   
  0x0044: # 'D' "\u0044"
   ("        ",
    "()()    ",
    "()  ()  ",
    "()  ()  ",
    "()  ()  ",
    "()()    "),
   
  0x0045: # 'E' "\u0045"
   ("        ",
    "()()()  ",
    "()      ",
    "()()()  ",
    "()      ",
    "()()()  "),
   
  0x0046: # 'F' "\u0046"
   ("        ",
    "()()()  ",
    "()      ",
    "()()()  ",
    "()      ",
    "()      "),
   
  0x0047: # 'G' "\u0047"
   ("        ",
    "  ()()  ",
    "()      ",
    "()      ",
    "()  ()  ",
    "  ()()  "),
   
  0x0048: # 'H' "\u0048"
   ("        ",
    "()  ()  ",
    "()  ()  ",
    "()()()  ",
    "()  ()  ",
    "()  ()  "),
   
  0x0049: # 'I' "\u0049"
   ("        ",
    "()()()  ",
    "  ()    ",
    "  ()    ",
    "  ()    ",
    "()()()  "),
   
  0x004A: # 'J' "\u004A"
   ("        ",
    "()()()  ",
    "  ()    ",
    "  ()    ",
    "  ()    ",
    "()      "),
   
  0x004B: # 'K' "\u004B"
   ("        ",
    "()  ()  ",
    "()  ()  ",
    "()()    ",
    "()  ()  ",
    "()  ()  "),
   
  0x004C: # 'L' "\u004C"
   ("        ",
    "()      ",
    "()      ",
    "()      ",
    "()      ",
    "()()()  "),
   
  0x004D: # 'M' "\u004D"
   ("        ",
    "()  ()  ",
    "()()()  ",
    "()()()  ",
    "()  ()  ",
    "()  ()  "),
   
  0x004E: # 'N' "\u004E"
   ("        ",
    "()()    ",
    "()  ()  ",
    "()  ()  ",
    "()  ()  ",
    "()  ()  "),
   
  0x004F: # 'O' "\u004F"
   ("        ",
    "  ()    ",
    "()  ()  ",
    "()  ()  ",
    "()  ()  ",
    "  ()    "),
   
  0x0050: # 'P' "\u0050"
   ("        ",
    "()()()  ",
    "()  ()  ",
    "()()()  ",
    "()      ",
    "()      "),
   
  0x0051: # 'Q' "\u0051"
   ("        ",
    "  ()    ",
    "()  ()  ",
    "()  ()  ",
    "()  ()  ",
    "  ()()  "),
   
  0x0052: # 'R' "\u0052"
   ("        ",
    "()()    ",
    "()  ()  ",
    "()()    ",
    "()  ()  ",
    "()  ()  "),
   
  0x0053: # 'S' "\u0053"
   ("        ",
    "  ()()  ",
    "()      ",
    "  ()    ",
    "    ()  ",
    "()()    "),
   
  0x0054: # 'T' "\u0054"
   ("        ",
    "()()()  ",
    "  ()    ",
    "  ()    ",
    "  ()    ",
    "  ()    "),
   
  0x0055: # 'U' "\u0055"
   ("        ",
    "()  ()  ",
    "()  ()  ",
    "()  ()  ",
    "()  ()  ",
    "  ()()  "),
   
  0x0056: # 'V' "\u0056"
   ("        ",
    "()  ()  ",
    "()  ()  ",
    "()  ()  ",
    "()  ()  ",
    "  ()    "),
   
  0x0057: # 'W' "\u0057"
   ("        ",
    "()  ()  ",
    "()  ()  ",
    "()()()  ",
    "()()()  ",
    "()  ()  "),
   
  0x0058: # 'X' "\u0058"
   ("        ",
    "()  ()  ",
    "()  ()  ",
    "  ()    ",
    "()  ()  ",
    "()  ()  "),
   
  0x0059: # 'Y' "\u0059"
   ("        ",
    "()  ()  ",
    "()  ()  ",
    "  ()    ",
    "  ()    ",
    "  ()    "),
   
  0x005A: # 'Z' "\u005A"
   ("        ",
    "()()()  ",
    "    ()  ",
    "  ()    ",
    "()      ",
    "()()()  "),
   
  0x005B: # '[' "\u005B"
   ("        ",
    "()()    ",
    "()      ",
    "()      ",
    "()      ",
    "()()    "),
   
  0x005C: # '\' "\u005C"
   ("        ",
    "        ",
    "()      ",
    "  ()    ",
    "    ()  ",
    "        "),
   
  0x005D: # ']' "\u005D"
   ("        ",
    "  ()()  ",
    "    ()  ",
    "    ()  ",
    "    ()  ",
    "  ()()  "),
   
  0x005E: # '^' "\u005E"
   ("        ",
    "  ()    ",
    "()  ()  ",
    "        ",
    "        ",
    "        "),
   
  0x005F: # '_' "\u005F"
   ("        ",
    "        ",
    "        ",
    "        ",
    "        ",
    "()()()  "),
   
  0x0060: # '`' "\u0060"
   ("        ",
    "  ()    ",
    "    ()  ",
    "        ",
    "        ",
    "        "),

  0x0061: # 'a' "\u0061"
   ("        ",
    "()()    ",
    "    ()  ",
    "  ()()  ",
    "()  ()  ",
    "  ()()  "),
   
  0x0062: # 'b' "\u0062"
   ("        ",
    "()      ",
    "()      ",
    "()()    ",
    "()  ()  ",
    "()()    "),
   
  0x0063: # 'c' "\u0063"
   ("        ",
    "        ",
    "        ",
    "  ()()  ",
    "()      ",
    "  ()()  "),
   
  0x0064: # 'd' "\u0064"
   ("        ",
    "    ()  ",
    "    ()  ",
    "  ()()  ",
    "()  ()  ",
    "  ()()  "),
   
  0x0065: # 'e' "\u0065"
   ("        ",
    "        ",
    "  ()    ",
    "()  ()  ",
    "()()    ",
    "  ()()  "),
   
  0x0066: # 'f' "\u0066"
   ("        ",
    "    ()  ",
    "  ()    ",
    "  ()()  ",
    "  ()    ",
    "  ()    "),
   
  0x0067: # 'g' "\u0067"
   ("        ",
    "  ()()  ",
    "()  ()  ",
    "  ()()  ",
    "    ()  ",
    "  ()    "),
   
  0x0068: # 'h' "\u0068"
   ("        ",
    "()      ",
    "()      ",
    "()()    ",
    "()  ()  ",
    "()  ()  "),
   
  0x0069: # 'i' "\u0069"
   ("        ",
    "  ()    ",
    "        ",
    "  ()    ",
    "  ()    ",
    "  ()()  "),
   
  0x006A: # 'j' "\u006A"
   ("        ",
    "    ()  ",
    "        ",
    "    ()  ",
    "()  ()  ",
    "  ()    "),
   
  0x006B: # 'k' "\u006B"
   ("        ",
    "()      ",
    "()  ()  ",
    "()()    ",
    "()  ()  ",
    "()  ()  "),
   
  0x006C: # 'l' "\u006C"
   ("        ",
    "()()    ",
    "  ()    ",
    "  ()    ",
    "  ()    ",
    "()()()  "),
   
  0x006D: # 'm' "\u006D"
   ("        ",
    "        ",
    "        ",
    "()()    ",
    "()()()  ",
    "()  ()  "),
   
  0x006E: # 'n' "\u006E"
   ("        ",
    "        ",
    "        ",
    "()()    ",
    "()  ()  ",
    "()  ()  "),
   
  0x006F: # 'o' "\u006F"
   ("        ",
    "        ",
    "        ",
    "()()()  ",
    "()  ()  ",
    "()()()  "),
   
  0x0070: # 'p' "\u0070"
   ("        ",
    "        ",
    "()()()  ",
    "()  ()  ",
    "()()()  ",
    "()      "),
   
  0x0071: # 'q' "\u0071"
   ("        ",
    "        ",
    "  ()()  ",
    "()  ()  ",
    "  ()()  ",
    "    ()  "),
   
  0x0072: # 'r' "\u0072"
   ("        ",
    "        ",
    "        ",
    "  ()()  ",
    "()      ",
    "()      "),
   
  0x0073: # 's' "\u0073"
   ("        ",
    "        ",
    "()()    ",
    "()      ",
    "  ()    ",
    "()()    "),
   
  0x0074: # 't' "\u0074"
   ("        ",
    "  ()    ",
    "()()()  ",
    "  ()    ",
    "  ()    ",
    "    ()  "),
   
  0x0075: # 'u' "\u0075"
   ("        ",
    "        ",
    "        ",
    "()  ()  ",
    "()  ()  ",
    "  ()()  "),
   
  0x0076: # 'v' "\u0076"
   ("        ",
    "        ",
    "        ",
    "()  ()  ",
    "()  ()  ",
    "  ()    "),
   
  0x0077: # 'w' "\u0077"
   ("        ",
    "        ",
    "        ",
    "()  ()  ",
    "()()()  ",
    "()()()  "),
   
  0x0078: # 'x' "\u0078"
   ("        ",
    "        ",
    "        ",
    "()  ()  ",
    "  ()    ",
    "()  ()  "),
   
  0x0079: # 'y' "\u0079"
   ("        ",
    "        ",
    "        ",
    "()  ()  ",
    "  ()    ",
    "  ()    "),
   
  0x007A: # 'z' "\u007A"
   ("        ",
    "        ",
    "()()()  ",
    "  ()    ",
    "()      ",
    "()()()  "),
   
  0x007B: # '{' "\u007B"
   ("        ",
    "  ()()  ",
    "  ()    ",
    "()      ",
    "  ()    ",
    "  ()()  "),
   
  0x007C: # '|' "\u007C"
   ("        ",
    "  ()    ",
    "  ()    ",
    "  ()    ",
    "  ()    ",
    "  ()    "),
   
  0x007D: # '}' "\u007D"
   ("        ",
    "()()    ",
    "  ()    ",
    "    ()  ",
    "  ()    ",
    "()()    "),
   
  0x007E: # '~' "\u007E"
   ("        ",
    "  ()()  ",
    "()()    ",
    "        ",
    "        ",
    "        "),

  0x00B0: # '°' "\u00B0" (KOI8-R: 0x9C)
   ("        ",
    "  ()    ",
    "()  ()  ",
    "  ()    ",
    "        ",
    "        "),

  0x00B7: # '·' "\u00B7" (KOI8-R: 0x9E)
   ("        ",
    "        ",
    "        ",
    "  ()    ",
    "        ",
    "        "),
}

def f1(s):
    retv = ""
    for i in range(4):
        retv += "()" if s[i * 2] != " " else "  "
    return '"' + retv + '"'

def f2(s):
    retv = 0
    for i in range(4):
        if s[i * 2] != " ":
            retv |= 0x8 >> i
    return "%02X" % retv

def f3(s):
    retv = ""
    for i in range(3):
        retv += "1, " if s[i * 2] != " " else "0, "
    retv += "1" if s[3 * 2] != " " else "0"
    return '(' + retv + ')'

v = 2 # 1, 2, 3, 4 or 5

if v == 1: # demo mode
    print("font_4x6_src = {")

    for k, v in font_4x6_src.items():
        print("  0x%04X:   # '%s'" % (k, chr(k)))
     
        print('   (' + f1(v[0]) + ',')
        for i in range(1, 5):
            print('    ' + f1(v[i]) + ',')
        print('    ' + f1(v[5]) + ')')
        print()

    print("}")

elif v == 2: # compact mode (bytearrays)
    print("font_4x6 = {")

    for k, v in font_4x6_src.items():
        str = '  0x%04X: b"' % k
        for i in range(6):
            str += '\\x' + f2(v[i]) 
        str += '", # \'' + chr(k) + "'"
        print(str)
    
    print("}")

elif v == 3: # matrix mode
    print("font_4x6 = {")
    
    for k, v in font_4x6_src.items():
        print("  0x%04X: # '%s'" % (k, chr(k)))
     
        print('   (' + f3(v[0]) + ',')
        for i in range(1, 5):
            print('    ' + f3(v[i]) + ',')
        print('    ' + f3(v[5]) + ')')
        print()

    print("}")

elif v == 4: # matrix SORT mode 
    print("font_4x6_short = (")
    
    for k in range(ord(b"'"), ord(b'~') + 1):
        v = font_4x6_src[k]
        print("  # '%s' = '\\x%02X'" % (chr(k), k))
        print('   (' + f3(v[0]) + ',')
        for i in range(1, 5):
            print('    ' + f3(v[i]) + ',')
        print('    ' + f3(v[5]) + ')')
        print()

    print(")")

elif v == 5: # super COMPACT mode (bytearrays)
    print("font_4x6_compact = (")

    for k in range(ord(b"'"), ord(b'~') + 1):
        v = font_4x6_src[k]

        str = '  b"'
        for i in range(6):
            str += '\\x' + f2(v[i]) 
        str += '", # \'' + chr(k) + ("' = '\\x%02X'" % k)
        print(str)
    
    print(")")
