# Enconding definition for special characters
# -*- coding: utf-8 -*-
print('\u256D' + 7 * (12 * '\u2500' + '\u252C') + 12 * '\u2500' + '\u256E')
print('\u2502' + 4 * ('    Code    \u2502   Symbol   \u2502'))
print('\u251C' + 7 * (12 * '\u2500' + '\u253C') + 12 * '\u2500' + '\u2524')
def printRange(interval):
    for i in range(interval[0], interval[1]):
        if (i + 1) % 4 == 0:
    #         print('\u2502' + ' ' * int((12-len(str('%04X' % i)))/2) + '%04X' % i +
    #             ' ' * int(12 - len(str('%04X' % i)) - int((12-len(str('%04X' % i)))/2)) +
    #             '\u2502')
    #     else:
    #         print('\u2502' + ' ' * int((12-len(str('%04X' % i)))/2) + '%04X' % i +
    #             ' ' * int(12 - len(str('%04X' % i)) - int((12-len(str('%04X' % i)))/2)) +
    #             '\u2502     ', end='')
            print('\u2502' + ' ' * 4 + '%04X' % i + ' ' * 4 + '\u2502     ' + chr(i) + '      \u2502')
        else:
            print('\u2502' + ' ' * 4 + '%04X' % i + ' ' * 4 + '\u2502     ' +  chr(i) + '      ', end='')

printRange([0x0020, 0x0080])
printRange([0x00A0, 0xFFF0])
print('\uFF97')







#     t = '\u256D\u2500\u2500\u2500'
#     m = '\u2502 ' + s[0] + ' '
#     b = '\u2570\u2500\u2500\u2500'
#     for i in range(1, len(s)):
#         t += '\u252C\u2500\u2500\u2500'
#         m += '\u2502 ' + s[i] + ' '
#         b += '\u2534\u2500\u2500\u2500'
#     t += '\u256E'
#     m += '\u2502'
#     b += '\u256F'
