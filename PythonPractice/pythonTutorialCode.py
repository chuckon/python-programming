MINUS_ONE = -1
ONE = 1
ZERO = 0
PY = 'PYTHON'
LONG_WORD = 'supercalifragilisticexpialidocious'
DIGIT_LIST = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
PY_LIST = ['P', 'Y', 'T', 'H', 'O', 'N']

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def printMessage(s=None):
    if s is None:
        print()
    else:
        lines = s.splitlines()
        for line in lines:
            print('\t\t' + line)

def printDivider():
    print('=========================================================================================================')

def printDivider2():
    print('---------------------------------------------------------------------------------------------------------')

codeInformation = {
'if Statement':
{
'syntax':
'''\
if <expression>:
    <statements>
elif <expression>:
    <statements>
elif <expression>:
    <statements>
...
else:
    <statements>
''',
'example':
'''\
if MINUS_ONE > 0:
    printMessage('Possitive number')
elif MINUS_ONE == 0:
    printMessage('Zero')
else:
    printMessage('Negative number')
'''
},
'while Statement':
{
'syntax':
'''\
while <expression>:
    <statements>
else:
    <statements>
''',
'example':
'''\
c = ZERO
while c < 15:
    c += 1
    if c == 13:
        continue
    printMessage('Iteration #%d, c = %d' % (c, c))
else:
    printMessage('Code executed at the end of the loop by else')
    printMessage('Did you notice that 13 was avoided with the continue statement?')
'''
},
'for Statement':
{
'syntax':
'''\
for <variable> in <sequence>:
    <statements>
else:
    <statements>
''',
'example':
'''\
for i in range(15):
    if i == 13 or i + 1 == 13:
        continue
    printMessage('Iteration #%d, i = %d' % (i + 1, i))
else:
    printMessage('Code executed at the end of loop by else')
    printMessage('Did you notice that 13 numbers were avoided with the continue statement?')
'''
},
'Strings':
{
'syntax':
'''\
Single quotes:          'Use "single" quotes to print double quotes or escape with \\, \', \"'
Double quotes:          "Use 'double' quotes to print single quotes or escape with \\, \', \""
Triple single quotes:   \'\'\'Triple quotes (either single or double)
                        for multiple lines\'\'\'
Triple double quotes:   \"\"\"Triple quotes
                                    maintain spacing
                                        on th multiple lines
                                            like tabs\"\"\"
Backslash (\):          Escape characters use backslash (\\n), to escape them, double it (\\\\)
Concat & repeat:        Strings can be concatenated with + and repeated n times with *
Concatenate:            Strings next to each other in a sequence are automatically concatenated
Slicing:                Strings can be subscripted (indexed) or sliced forwards and backwards

        +---+---+---+---+---+---+   <stringname>[[start included]:[end excluded]]
        | P | y | t | h | o | n |
        +---+---+---+---+---+---+   if start is not specified it means from the very beginning
        0   1   2   3   4   5   6
       -6  -5  -4  -3  -2  -1       if end is not specified it means until the very end
       
       Strings are unmutable, they cannot be changed (can be copied and copies modified)

Built-in function str:  With the built-in function str(), a number can be converted to string
Built-in function len:  With the built-in function len(), the length of a string can be found

''',
'example':
'''\
printMessage('\"Yes\", he said.')
printMessage('"No!", he said.')
printMessage(\'\'\'\"Isn\'t it?\", she asked.\'\'\')
printMessage('\Library\Frameworks\Python.framework\Versions\\\\3.6\\\\bin\python')
printMessage('WHA' + 5 * 'KA')
printMessage('WHA'                    'KA' 'KA' 'KA' 'KA' 'KA')
printMessage(PY[0:2] + ' ' + PY[4:6] + ' ' + PY[-6:-4] + ' ' + PY[-2:])
printMessage('The lenght of string "' + LONG_WORD + '" is ' + str(len(LONG_WORD)))
'''
},
'Lists':
{
'syntax':
'''\
Creation with elements: <list_name> = [[element1,] [element2,] ...]
Concatenate:            Lists can be concatenated with +
Slicing:                Lists can be subscripted (indexed) or sliced like strings
Built-in function len:  With the built-in function len(), the length of a list can be found
Nesting:                Lists can be nested in whatever dimensions desired
Contents:               Lists can contain any type of elements even mixed ones
       
       Lists unlike strings, are mutable, anything can be changed on them 
''',
'example':
'''\
odd_digits = [1, 3, 5, 7, 9]
printMessage(str(odd_digits))
printMessage(str(PY_LIST + DIGIT_LIST))
printMessage()
'''
},
}



printDivider()
print('\n' + 'Python 3.6' + '\n')
printDivider()
for stat in codeInformation:
    print('\n' + stat + '\n')
    printDivider2()
    print('\n\tSyntax\n')
    printDivider2()
    print('\n')
    printMessage(codeInformation[stat]['syntax'])
    print('\n')
    printDivider2()
    print('\n\tCode example\n')
    printDivider2()
    print('\n')
    printMessage(codeInformation[stat]['example'])
    print('\n')
    printDivider2()
    print('\n\tResult\n')
    printDivider2()
    print('\n')
    exec(codeInformation[stat]['example'])
    print('\n')
    printDivider()

