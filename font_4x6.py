#!/usr/bin/env python3
# -*- coding: UTF8 -*-

font_4x6 = {
  0x0020: b"\x00\x00\x00\x00", # ' '
  0x0021: b"\x00\x1D\x00\x00", # '!'
  0x0022: b"\x18\x00\x18\x00", # '"'
  0x0023: b"\x0E\x1B\x0E\x00", # '#'
  0x0024: b"\x0D\x1F\x16\x00", # '$'
  0x0025: b"\x12\x04\x09\x00", # '%'
  0x0026: b"\x0A\x15\x0B\x00", # '&'
  0x0027: b"\x00\x18\x00\x00", # '''
  0x0028: b"\x0E\x11\x00\x00", # '('
  0x0029: b"\x00\x11\x0E\x00", # ')'
  0x002A: b"\x0A\x04\x0A\x00", # '*'
  0x002B: b"\x04\x0E\x04\x00", # '+'
  0x002C: b"\x01\x02\x00\x00", # ','
  0x002D: b"\x04\x04\x04\x00", # '-'
  0x002E: b"\x00\x01\x00\x00", # '.'
  0x002F: b"\x02\x04\x08\x00", # '/'
  0x0030: b"\x1F\x11\x1F\x00", # '0'
  0x0031: b"\x00\x08\x1F\x00", # '1'
  0x0032: b"\x17\x15\x1D\x00", # '2'
  0x0033: b"\x15\x15\x1F\x00", # '3'
  0x0034: b"\x1C\x04\x1F\x00", # '4'
  0x0035: b"\x1D\x15\x17\x00", # '5'
  0x0036: b"\x1F\x15\x17\x00", # '6'
  0x0037: b"\x10\x10\x1F\x00", # '7'
  0x0038: b"\x1F\x15\x1F\x00", # '8'
  0x0039: b"\x1D\x15\x1F\x00", # '9'
  0x003A: b"\x00\x0A\x00\x00", # ':'
  0x003B: b"\x01\x0A\x00\x00", # ';'
  0x003C: b"\x04\x0A\x11\x00", # '<'
  0x003D: b"\x0A\x0A\x0A\x00", # '='
  0x003E: b"\x11\x0A\x04\x00", # '>'
  0x003F: b"\x18\x13\x1C\x00", # '?'
  0x0040: b"\x1C\x14\x1C\x00", # '@'
  0x0041: b"\x0F\x14\x1F\x00", # 'A'
  0x0042: b"\x1F\x15\x0A\x00", # 'B'
  0x0043: b"\x0E\x11\x11\x00", # 'C'
  0x0044: b"\x1F\x11\x0E\x00", # 'D'
  0x0045: b"\x1F\x15\x15\x00", # 'E'
  0x0046: b"\x1F\x14\x14\x00", # 'F'
  0x0047: b"\x0E\x11\x13\x00", # 'G'
  0x0048: b"\x1F\x04\x1F\x00", # 'H'
  0x0049: b"\x11\x1F\x11\x00", # 'I'
  0x004A: b"\x11\x1E\x10\x00", # 'J'
  0x004B: b"\x1F\x04\x1B\x00", # 'K'
  0x004C: b"\x1F\x01\x01\x00", # 'L'
  0x004D: b"\x1F\x0C\x1F\x00", # 'M'
  0x004E: b"\x1F\x10\x0F\x00", # 'N'
  0x004F: b"\x0E\x11\x0E\x00", # 'O'
  0x0050: b"\x1F\x14\x1C\x00", # 'P'
  0x0051: b"\x0E\x11\x0F\x00", # 'Q'
  0x0052: b"\x1F\x14\x0B\x00", # 'R'
  0x0053: b"\x09\x15\x12\x00", # 'S'
  0x0054: b"\x10\x1F\x10\x00", # 'T'
  0x0055: b"\x1E\x01\x1F\x00", # 'U'
  0x0056: b"\x1E\x01\x1E\x00", # 'V'
  0x0057: b"\x1F\x06\x1F\x00", # 'W'
  0x0058: b"\x1B\x04\x1B\x00", # 'X'
  0x0059: b"\x18\x07\x18\x00", # 'Y'
  0x005A: b"\x13\x15\x19\x00", # 'Z'
  0x005B: b"\x1F\x11\x00\x00", # '['
  0x005C: b"\x08\x04\x02\x00", # '\'
  0x005D: b"\x00\x11\x1F\x00", # ']'
  0x005E: b"\x08\x10\x08\x00", # '^'
  0x005F: b"\x01\x01\x01\x00", # '_'
  0x0060: b"\x00\x10\x08\x00", # '`'
  0x0061: b"\x12\x15\x0F\x00", # 'a'
  0x0062: b"\x1F\x05\x02\x00", # 'b'
  0x0063: b"\x02\x05\x05\x00", # 'c'
  0x0064: b"\x02\x05\x1F\x00", # 'd'
  0x0065: b"\x06\x0B\x05\x00", # 'e'
  0x0066: b"\x00\x0F\x14\x00", # 'f'
  0x0067: b"\x08\x15\x1E\x00", # 'g'
  0x0068: b"\x1F\x04\x03\x00", # 'h'
  0x0069: b"\x00\x16\x01\x00", # 'i'
  0x006A: b"\x02\x01\x16\x00", # 'j'
  0x006B: b"\x1F\x04\x0B\x00", # 'k'
  0x006C: b"\x00\x1E\x01\x00", # 'l'
  0x006D: b"\x07\x06\x03\x00", # 'm'
  0x006E: b"\x07\x04\x03\x00", # 'n'
  0x006F: b"\x07\x05\x07\x00", # 'o'
  0x0070: b"\x0F\x0A\x0E\x00", # 'p'
  0x0071: b"\x04\x0A\x0F\x00", # 'q'
  0x0072: b"\x03\x04\x04\x00", # 'r'
  0x0073: b"\x0D\x0B\x00\x00", # 's'
  0x0074: b"\x08\x1E\x09\x00", # 't'
  0x0075: b"\x06\x01\x07\x00", # 'u'
  0x0076: b"\x06\x01\x06\x00", # 'v'
  0x0077: b"\x07\x03\x07\x00", # 'w'
  0x0078: b"\x05\x02\x05\x00", # 'x'
  0x0079: b"\x04\x03\x04\x00", # 'y'
  0x007A: b"\x0B\x0D\x09\x00", # 'z'
  0x007B: b"\x04\x1B\x11\x00", # '{'
  0x007C: b"\x00\x1F\x00\x00", # '|'
  0x007D: b"\x11\x1B\x04\x00", # '}'
  0x007E: b"\x08\x18\x10\x00", # '~'
  0x00B0: b"\x08\x14\x08\x00", # '°'
  0x00B4: b"\x00\x08\x10\x00", # '´'
  0x00B7: b"\x00\x04\x00\x00", # '·'
}

def f(v, y):
    retv = ""
    for i in range(4):
        retv += "()" if (v[i] & (0x20 >> y)) != 0 else "  "
    return '"' + retv + '"'

if True: # demo mode
    print("font_4x6_src = {")

    for k, v in font_4x6.items():
        print("  0x%04X:   # '%s'" % (k, chr(k)))
     
        print('  (' + f(v, 0) + ',')
        for i in range(1, 5):
            print('   ' + f(v, i) + ',')
        print('   ' + f(v, 5) + ')')
        print()

    print("}")

