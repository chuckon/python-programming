# Enconding definition for special characters
# -*- coding: utf-8 -*-

# **************************************************************************************************
#'topic':
#{
#'purpose':
#'''\
#''',
#'syntax':
#'''\
#''',
#'example':
#'''\
#'''
#},

# Negative, zero and positive constants
MINUS_ONE = -1
ONE = 1
ZERO = 0

# Short example string
PY = 'PYTHON'

# Long example string
LONG_WORD = 'supercalifragilisticexpialidocious'

# Digit list
DIGIT_LIST = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Character list
PY_LIST = ['P', 'Y', 'T', 'H', 'O', 'N']

# Recursive Factorial function
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)

# Recursive Sumation function
def sumation(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + sumation(n - 1)

# Recursive Fibonacci Number function
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Recursive Fibonacci Sequence function
def fibonacciSequence(n):
    seq = []
    for i in range(n + 1):
        seq.append(fibonacci(i))
    return seq

# Function that returns the syntax intervals in a message
def getSyntaxIntervals(lines):
    l = []
    s = None
    m = None
    for i in range(len(lines)):
        if len(lines[i]) > 0:
            if lines[i][0] == '|':
                s = i
                lines[i] = lines[i][1:]
                m = len(lines[i])
                if lines[i][len(lines[i]) - 1] == '|':
                    lines[i] = lines[i][:len(lines[i]) - 1]
                    m = len(lines[i])
                    l.append([s, i, m])
                    s = None
            elif lines[i][len(lines[i]) - 1] == '|':
                lines[i] = lines[i][:len(lines[i]) - 1]
                l.append([s, i, m])
                s = None
            elif s != None:
                if len(lines[i]) > m:
                    m = len(lines[i])
    return l

# Print Tool Function for formatting a line of text
def printMessageLine(line=None):
    if line is None:
        print()
    else:
        print('\t' + line)

# Print Tool Function for formatting text
def printMessage(s=None):
    if s is None:
        print()
    else:
        lines = s.splitlines()
        syntaxIntervals = getSyntaxIntervals(lines)
        for i in range(len(lines)):
            if len(syntaxIntervals) > 0:
                if i == syntaxIntervals[0][0]:
                    printMessageLine((int((95 - syntaxIntervals[0][2]) / 2) - 4) * ' ' + '\u256D' +
                                     (syntaxIntervals[0][2] + 8) * '\u2500' + '\u256E')
                    printMessageLine((int((95 - syntaxIntervals[0][2]) / 2) - 4) * ' ' + '\u2502' +
                                     (syntaxIntervals[0][2] + 8) * ' ' + '\u2502')
                    printMessageLine((int((95 - syntaxIntervals[0][2]) / 2) - 4) * ' ' + '\u2502' +
                                     4 * ' ' + lines[i] + (syntaxIntervals[0][2] - len(lines[i])) *
                                     ' ' + 4 * ' ' + '\u2502')
                    if syntaxIntervals[0][0] == syntaxIntervals[0][1]:
                        printMessageLine((int((95 - syntaxIntervals[0][2]) / 2) - 4) * ' ' +
                                         '\u2502' + (syntaxIntervals[0][2] + 8) * ' ' + '\u2502')
                        printMessageLine((int((95 - syntaxIntervals[0][2]) / 2) - 4) * ' ' +
                                         '\u2570' + (syntaxIntervals[0][2] + 8) * '\u2500' +
                                         '\u256F')
                        syntaxIntervals.pop(0)
                elif i > syntaxIntervals[0][0] and i < syntaxIntervals[0][1]:
                    printMessageLine((int((95 - syntaxIntervals[0][2]) / 2) - 4) * ' ' + '\u2502' +
                                     4 * ' ' + lines[i] + (syntaxIntervals[0][2] - len(lines[i])) *
                                     ' ' + 4 * ' ' + '\u2502')
                elif i == syntaxIntervals[0][1]:
                    printMessageLine((int((95 - syntaxIntervals[0][2]) / 2) - 4) * ' ' + '\u2502' +
                                     4 * ' ' + lines[i] + (syntaxIntervals[0][2] - len(lines[i])) *
                                     ' ' + 4 * ' ' + '\u2502')
                    printMessageLine((int((95 - syntaxIntervals[0][2]) / 2) - 4) * ' ' + '\u2502' +
                                     (syntaxIntervals[0][2] + 8) * ' ' + '\u2502')
                    printMessageLine((int((95 - syntaxIntervals[0][2]) / 2) - 4) * ' ' + '\u2570' +
                                     (syntaxIntervals[0][2] + 8) * '\u2500' + '\u256F')
                    syntaxIntervals.pop(0)
                else:
                    printMessageLine(lines[i])
            else:
                printMessageLine(lines[i])

# Function to print a higher hierarchy divider
def printDivider():
    print(105 * '\u2550')

# Function to print a lower hierarchy divider
def printDivider2():
    print(105 * '\u2500')

# Function to print the header of the code tutorial
def printHeader():
    printDivider()
    print('\n' + '\u27F0 Python 3.6' + '\n')
    printDivider()

# Function to format a string in a cube format
def cubeMessage(s):
    if len(s) > 20:
        s = s.split()[0]
    s = s.upper()
    t = '\u256D\u2500\u2500\u2500'
    m = '\u2502 ' + s[0] + ' '
    b = '\u2570\u2500\u2500\u2500'
    for i in range(1, len(s)):
        t += '\u252C\u2500\u2500\u2500'
        m += '\u2502 ' + s[i] + ' '
        b += '\u2534\u2500\u2500\u2500'
    t += '\u256E'
    m += '\u2502'
    b += '\u256F'
    return (t, m, b)

# Function to print all code topics
def printCodeTopics(codeInfo):
    for topic in codeInfo:
        t, m, b = cubeMessage(topic)
        print('\n' + ' ' * (len(topic) + 3) + t)
        print('\u25BD ' + topic + ' ' + m)
        print(' ' * (len(topic) + 3) + b + '\n')
        printDivider2()
        print('\n\t\u2318 Purpose & Syntax\n')
        printDivider2()
        print('\n')
        printMessage('\u25C9 Purpose:  ' + codeInfo[topic]['purpose'])
        print('\n')
        printMessage('\u25C9 Syntax:')
        print('\n')
        printMessage(codeInfo[topic]['syntax'])
        print('\n')
        printDivider2()
        print('\n\t\u2318 Code example\n')
        printDivider2()
        print('\n')
        printMessage(codeInfo[topic]['example'])
        print('\n')
        printDivider2()
        print('\n\t\u2318 Result\n')
        printDivider2()
        print('\n')
        exec(codeInfo[topic]['example'])
        print('\n')
        printDivider()

# Function to execute and run the whole live code tutorial
def runLiveCodeTutorial():
    printHeader()
    printCodeTopics(codeInformation)

# Dictionary with all topic information about the live code tutorial
codeInformation = {
# **************************************************************************************************
'range() function':
{
'purpose':
'''\
Generates arithmetic progressions as sequences of numbers to be used on iterations.
''',
'syntax':
'''\
\t\u23E3 Generates a sequence 0...n-1:

|range(n)|

\t\u23E3 Generates a sequence n...m-1:

|range(n, m)|

\t\u23E3 Generates a sequence n...m-1 with k steps:

|range(n, m, k)|
''',
'example':
'''\
printMessage('Zero to n-1 sequence:\\t\\t\\t\\t' + str(list(range(10))))
printMessage('n to m-1 sequence:\\t\\t\\t\\t' + str(list(range(5, 10))))
printMessage('n to m-1 sequence with k step:\\t\\t' + str(list(range(-10, -100, -20))))
'''
},
# **************************************************************************************************
'Strings2':
{
'purpose':
'''\
Sequence of characters usually enclosed between quotes to be used mostly as text.
''',
'syntax':
'''\
\t\u23E3 Single quotes:\t\t\t\t'Use "single" quotes to print double quotes or
\t\t\t\t\t\t\t\tescape with \\, \', \"'
\t\u23E3 Double quotes:\t\t\t\t"Use 'double' quotes to print single quotes or
\t\t\t\t\t\t\t\tescape with \\, \', \""
\t\u23E3 Triple single quotes:\t\t\'\'\'Triple quotes (either single or double)
\t\t\t\t\t\t\t\tfor multiple lines\'\'\'
\t\u23E3 Triple double quotes:\t\t\"\"\"Triple quotes
\t\t\t\t\t\t\t\t\t\tmaintain spacing
\t\t\t\t\t\t\t\t\t\t\ton th multiple lines
\t\t\t\t\t\t\t\t\t\t\t\tlike tabs\"\"\"
\t\u23E3 Backslash (\):\t\t\t\tEscape characters use backslash (\\n), to escape them,
\t\t\t\t\t\t\t\tdouble it (\\\\)
\t\u23E3 Concatenate & repeat:\t\tStrings can be concatenated with + and repeated n times with *

|<string_1> + <string_2> + ... + <m> * <string_N>|

\t\u23E3 Concatenate:\t\t\t\tStrings next to each other in a sequence are automatically
\t\t\t\t\t\t\t\tconcatenated

|<string_1> <string_2> <string_3> ... <string_N>|

\t\u23E3 Slicing:\t\t\t\t\tStrings can be subscripted (indexed) or sliced forwards and
\t\t\t\t\t\t\t\tbackwards

|<string>[ [start_included[:end_excluded[:step]]] ]|

\t\u23E3 String methods and common operations:
\t\t\u2724 <string_1> in <string_2>:\t\tReturn TRUE if the string is within the string,
\t\t\t\t\t\tFALSE otherwise
\t\t\u2724 <item> not in <list>:\t\t\tReturn TRUE if the item is not in the list, FALSE otherwise
\t\t\u2724 .append(<item>):\t\t\t\tAppend an item to the end of the list


\t\t+---+---+---+---+---+---+
\t\t\u2502 P \u2502 y \u2502 t \u2502 h \u2502 o \u2502 n \u2502
\t\t+---+---+---+---+---+---+\tif start is not specified it means from the very beginning
\t\t0   1   2   3   4   5   6
\t   -6  -5  -4  -3  -2  -1   N\tif end is not specified it means until the very end

\t\t\u27F9 Strings are immutable, they cannot be changed (can be copied and copies modified)

\t\u23E3 Built-in function str():\tWith built-in function str(), a number and mostly any other type
\t\t\t\t\t\t\t\tof object can be converted to strings (no object returns an empty string)

|str([object])|

\t\u23E3 Built-in function len():\tWith built-in function len(), the length of a string can be found

|len(<string_name>)|
''',
'example':
'''\
# Examples of String uses, quotes, slicing, concatenation and characteristics
printMessage('Escaping double quotes inside string:\\t\\t\\t\\t\\t\\t' + '\"Yes\", he said.')
printMessage('Double quotes inside string:\\t\\t\\t\\t\\t\\t\\t\\t' + '"No!", he said.')
printMessage('Double quotes & single quotes inside string:\\t\\t\\t\\t' +
            \'\'\'\"Isn\'t it?\", she asked.\'\'\')
printMessage('Escaping escape characters:\\t\\t\\t\\t\\t\\t\\t\\t' +
            '\Library\...\Versions\\\\3.6\\\\bin\python')
printMessage('Concatenating (+) & multiplying (*) strings:\\t\\t\\t\\t' + 'WHA' + 5 * 'KA')
printMessage('Concatenating consecutive strings:\\t\\t\\t\\t\\t\\t\\t' 'WHA'
            'KA' 'KA' 'KA' 'KA' 'KA')
printMessage('Slicing strings (\\'%s\\') forward & backwards:\\t\\t\\t\\t' % PY +
            PY[0:2] + ' ' + PY[4:6] + ' ' + PY[-6:-4] + ' ' + PY[-2:])
printMessage('Length of string \\'%s\\':\\t\\t' % LONG_WORD + 'The lenght of the string is ' +
            str(len(LONG_WORD)))
'''
},
# **************************************************************************************************
'Lists':
{
'purpose':
'''\
Compound data type to group a comma-separated sequence of values between square brackets.
''',
'syntax':
'''\
\t\u23E3 Creation with items:\t\tLists can be defined as an empty list (just []) or with its items

|<list_name> = [ [item1[, item2,]] ... ]|

\t\u23E3 Concatenate:\t\t\t\tLists can be concatenated with +

|<list_1> + <list_2> + ... + <list_N>|

\t\u23E3 Slicing:\t\t\t\t\tLists can be subscripted (indexed) or sliced like strings
\t\u23E3 Built-in function len():\tWith the built-in function len(), the length of a list
\t\t\t\t\t\t\t\tcan be found
\t\u23E3 Nesting:\t\t\t\t\tLists can be nested in whatever dimensions desired
\t\u23E3 Contents:\t\t\t\t\tLists can contain any type of items even mixed ones
\t\u23E3 Built-in function list():\tWith built-in function list() other objects can be
\t\t\t\t\t\t\t\tconverted to lists (no object returns an empty list)

|list([object])|

\t\t\u27F9 Lists unlike strings, are mutable, anything can be changed on them

\t\u23E3 List methods and common operations:
\t\t\u2724 <item> in <list>:\t\t\tReturn TRUE if the item is in the list, FALSE otherwise
\t\t\u2724 <item> not in <list>:\t\t\tReturn TRUE if the item is not in the list, FALSE otherwise
\t\t\u2724 .append(<item>):\t\t\t\tAppend an item to the end of the list
\t\t\u2724 .extend(<iterable>):\t\t\tExtend the list by appending the iterable items
\t\t\u2724 .insert(<position>, <item>):\t\tInsert an item at a given position
\t\t\u2724 .remove(<item>):\t\t\t\tRemove the first occurrence of an item in the list
\t\t\u2724 .pop([position]):\t\t\t\tRemove the last item of the list or the one at index
\t\t\u2724 .clear():\t\t\t\t\t\tRemove all items from the list
\t\t\u2724 .index(<item>[, start[, end]]):\tReturn zero-base index of the first item occurrence
\t\t\u2724 .count(<item>):\t\t\t\t\tReturn the number of occurrences of the item in the list
\t\t\u2724 .sort([key=<value>[,
\t\t\treverse=<value>]]):\t\t\tSort ascending the items in the list
\t\t\u2724 .reverse():\t\t\t\t\t\tReverse the order of the items of the list in place
\t\t\u2724 .copy():\t\t\t\t\t\tReturn a shallow copy of the list
\t\u23E3 List comprehensions:\t\tBrackets containing an expression followed by a for clause, then
\t\t\t\t\t\t\t\tzero or more for or if clauses.  They can be nested.
''',
'example':
'''\
# Examples of List uses, slicing, concatenation and characteristics
fruits = ['orange', 'apple', 'pear']
tropical_fruits = ('mango', 'banana', 'pineapple')
printMessage('Simple list defined with items:\\t\\t\\tfruits = ' + str(fruits))
printMessage('Concatenated lists:\\t\\t\\t\\t\\t\\t' + str(PY_LIST + fruits))
printMessage('Slicing lists forward & backwards:\\t\\t\\tPair:  ' + str(DIGIT_LIST[0:9:2]) +
            ' Odd:  ' + str(DIGIT_LIST[-9::2]))
printMessage('Nested lists of slices of DIGIT_LIST:\\t\\t' + str([DIGIT_LIST[0:2], DIGIT_LIST[2:4],
            DIGIT_LIST[4:6],DIGIT_LIST[6:8],DIGIT_LIST[8:]]))
printMessage('List with different types of items:\\t\\t' + str(['Python', 3.14, DIGIT_LIST[0:9:2],
            7, 'X']))
printMessage('Converting a range to a list:\\t\\t\\t\\t' + str(list(range(10))))
fruits.append('tangerine')
printMessage('Append another fruit:\\t\\t\\t\\t\\t\\t' + str(fruits))
fruits.extend(tropical_fruits)
printMessage('Extend list with a tuple:\\t\\t\\t\\t\\t[\\'' + '\\', \\''.join(fruits[:5]) + '\\',' +
            '\\n\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t \\'' + '\\', \\''.join(fruits[5:]) + '\\']')
fruits.insert(4, 'apple')
printMessage('Insert another fruit at position 4:\\t\\t[\\'' + '\\', \\''.join(fruits[:5]) +
            '\\',' + '\\n\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t \\'' + '\\', \\''.join(fruits[5:]) + '\\']')
printMessage('Count of apples:\\t\\t\\t\\t\\t\\t\\t' + str(fruits.count('apple')))
printMessage('First index of apples between 3 & 6:\\t\\t' + str(fruits.index('apple', 3, 6)))
fruits.remove('apple')
printMessage('Remove first occurrence of item \\'apple\\':\\t[\\'' + '\\', \\''.join(fruits[:5]) +
            '\\',' + '\\n\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t \\'' + '\\', \\''.join(fruits[5:]) + '\\']')
fruits.pop(4)
printMessage('Pop of item at position 4:\\t\\t\\t\\t\\t[\\'' + '\\', \\''.join(fruits[:5])
            + '\\',' + '\\n\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t \\'' + '\\', \\''.join(fruits[5:]) +
            '\\']')
fruits.pop()
fruits.pop()
printMessage('Pop of last item twice:\\t\\t\\t\\t\\t' + str(fruits))
printMessage('Length of list fruits:\\t\\t\\t\\t\\t' + str(len(fruits)))
fruits.sort()
printMessage('Ascending sorted list:\\t\\t\\t\\t\\t' + str(fruits))
fruits.reverse()
printMessage('Reversed list:\\t\\t\\t\\t\\t\\t\\t' + str(fruits))
copy_fruits = fruits.copy()
printMessage('Copied list into another variable:\\t\\t\\t' + str(copy_fruits))
copy_fruits.clear()
printMessage('Copied list items cleared:\\t\\t\\t\\t\\t' + str(copy_fruits))
printMessage('Matrix created with list comprenhension:\\t' + str([[i + j for i in range(4)]
            for j in range(1, 10, 4)]))
'''
},
# **************************************************************************************************
'Tuples':
{
'purpose':
'''\
Compound data type to group a comma-separated sequence of values between parenthesis.
''',
'syntax':
'''\
|<tuple_name> = [(][item1[, item2,]] ... [)]|

\t\u23E3 Concatenate:\t\t\t\tTuples can be concatenated with +

|<tuple_1> + <tuple_2> + ... + <tuple_N>|

\t\u23E3 Slicing:\t\t\t\t\tTuples can be subscripted (indexed) or sliced like strings
\t\u23E3 Built-in function len():\tWith the built-in function len(), the length of a tuple
\t\t\t\t\t\t\t\tcan be found
\t\u23E3 Nesting:\t\t\t\t\tTuples can be nested in whatever dimensions desired
\t\u23E3 Contents:\t\t\t\t\tTuples can contain any type of items even mixed ones
\t\u23E3 Built-in function tuple():\tWith built-in function tuple() other objects can be
\t\t\t\t\t\t\t\tconverted to tuples (no object returns an empty tuple)

|tuple([object])|

\t\t\u27F9 Tuples are immutable, they cannot be changed (can be copied and copies modified)

\t\u23E3 Lists methods:
\t\t\u2724 .append(<item>):\t\t\t\tAppend an item to the end of the list
\t\t\u2724 .extend(<iterable>):\t\t\tExtend the list by appending the iterable items
\t\t\u2724 .insert(<position>, <item>):\t\tInsert an item at a given position
\t\t\u2724 .remove(<item>):\t\t\t\tRemove the first occurrence of an item in the list
\t\t\u2724 .pop([position]):\t\t\t\tRemove the last item of the list or the one at index
\t\t\u2724 .clear():\t\t\t\t\t\tRemove all items from the list
\t\t\u2724 .index(<item>[, start[, end]]):\tReturn zero-base index of the first item occurrence
\t\t\u2724 .count(<item>):\t\t\t\t\tReturn the number of occurrences of the item in the list
\t\t\u2724 .sort([key=<value>[,
\t\t\treverse=<value>]]):\t\t\tSort ascending the items in the list
\t\t\u2724 .reverse():\t\t\t\t\t\tReverse the order of the items of the list in place
\t\t\u2724 .copy():\t\t\t\t\t\tReturn a shallow copy of the list
\t\u23E3 List comprehensions:\t\tBrackets containing an expression followed by a for clause, then
\t\t\t\t\t\t\t\tzero or more for or if clauses.  They can be nested.
''',
'example':
'''\
'''
},
# **************************************************************************************************
'Sets':
{
'purpose':
'''\
''',
'syntax':
'''\
''',
'example':
'''\
'''
},
# **************************************************************************************************
'Dictionaries':
{
'purpose':
'''\
''',
'syntax':
'''\
''',
'example':
'''\
'''
},
# **************************************************************************************************
'if Statement':
{
'purpose':
'''\
Branch statement to control the flow of code based on boolean conditions.
''',
'syntax':
'''\
|if <expression>:
    <statements>
elif <expression>:
    <statements>
elif <expression>:
    <statements>
...
else:
    <statements>|
''',
'example':
'''\
# Evaluates if a randomly generated number is possitive, negative or zero
import random
n = random.randint(-1,1)
printMessage('Generated value, n = %d' % n)
if n > 0:
    printMessage('n is a possitive number')
elif n == 0:
    printMessage('n is equal to zero')
else:
    printMessage('n is a negative number')
'''
},
# **************************************************************************************************
'while Statement':
{
'purpose':
'''\
Loop statement which executes and iterates as long as a condition remains true.
''',
'syntax':
'''\
|while <expression>:
    <statements>
else:
    <statements>|
''',
'example':
'''\
# While Loop to iterate 15 times and print the value of each iteration skipping 13th
c = ZERO
while c < 15:
    c += 1
    if c == 13:
        continue
    printMessage('Iteration #%d, c = %d' % (c, c))
else:
    printMessage('Code executed at the end of the loop by else')
    printMessage('Notice that 13 was avoided with the continue statement')
'''
},
# **************************************************************************************************
'for Statement':
{
'purpose':
'''\
Loop statement which executes and iterates over the items of a sequence on its order.
''',
'syntax':
'''\
|for <variable> in <sequence>:
    <statements>
else:
    <statements>|
''',
'example':
'''\
# For Loop to iterate 15 times and print the value of each iteration skipping 13th
for i in range(15):
    if i == 13 or i + 1 == 13:
        continue
    printMessage('Iteration #%d, i = %d' % (i + 1, i))
else:
    printMessage('Code executed at the end of loop by else')
    printMessage('Notice that 13 numbers were avoided with the continue statement')
'''
},
# **************************************************************************************************
'pass Statement':
{
'purpose':
'''\
Synctactic filler statement that does nothing for other statements and structures
          when no action is required.
''',
'syntax':
'''\
|pass|
''',
'example':
'''\
#Function defined that does nothing and if structure that executes it
def whateverFunction():
    printMessage('Function is called, but does nothing but to print this message')
    pass
if 0:
    pass
else:
    whateverFunction()
'''
},
# **************************************************************************************************
'try Statement':
{
'purpose':
'''\
Remove objects from memory like items in lists or lists itselves.
''',
'syntax':
'''\
|del <object>|

\t\t\u27F9 There is no other way to remove an item from a list given its index.
\t\t\u27F9 The pop() function returns the value that is being removed.
''',
'example':
'''\
'''
},
# **************************************************************************************************
'Function Definition':
{
'purpose':
'''\
Define subroutines and blocks of code to be invoked on demand and repeatedly.
''',
'syntax':
'''\
|def <function_name>([keyw_arg1[ = default_value1][, keyw_arg2[ = default_value2]] ...]):
    <statements>|

        \u27F9 If a default value is specified for an argument, that argument becomes optional.
        \u27F9 Arguments with no default value are required.
        \u27F9 An argument can be specified positionally or with a keyword.
        \u27F9 Arguments can be specified positionally but only before any keyword argument is used.
        \u27F9 A function can be invoked with an arbitrary number of arguments in a list (*args).

|def <function_name>(*args):
    <statements>|
''',
'example':
'''\
# Function to calculate the area of different geometric figures
import math
def area(n, r1 = 0, r2 = 0, l = 0, h = 0, a = 0, b = 0, d1 = 0, d2 = 0):
    global math
    if ((n == 0 and (r1 == 0 and r2 == 0)) or
            (n == 3 and (h == 0 or b == 0)) or
            (n == 4 and l == 0 and ((a == 0 or b == 0) and h == 0) and (d1 == 0 or d2 == 0)) or
            (n > 4 and l == 0) or (n == 1 or n == 2)):
        return 0
    else:
        if n == 0:
            if r2 != 0:
                pass
                return r1 * r2 * math.pi
            else:
                return r1 ** 2 * math.pi
        elif n == 3:
            return b * h / 2
        elif n == 4:
            if l != 0:
                return l ** 2
            elif a == 0 and (b != 0 and h != 0):
                return b * h
            elif a != 0 and b != 0 and h != 0:
                return (a + b) * h / 2
            elif d1 != 0 and d2 != 0:
                return d1 * d2 / 2
        elif n > 4:
            return n * l ** 2 / (4 * math.tan(math.pi/n))
printMessage('Area of a circle of radius 3:\\t\\t\\t\\t\\t\\t%.2f' % area(0, 3))
printMessage('Area of a ellipse of radiuses 2 & 4:\\t\\t\\t\\t%.2f' % area(0, 2, 4))
printMessage('Area of a triangle of base 8 and height 6:\\t\\t\\t%.2f' % area(3, b = 8, h = 6))
printMessage('Area of a square of side 5:\\t\\t\\t\\t\\t\\t%.2f' % area(4, 0, 0, 5))
printMessage('Area of a quadrilateral of base 6 & height 4:\\t\\t%.2f' % area(4, b = 6, h = 4))
printMessage('Area of a trapezoid of bases 4 & 6 and height 5:\\t%.2f' %
            area(4, a = 4, b = 6, h = 5))
printMessage('Area of a kite of diagonals 6 & 8:\\t\\t\\t\\t\\t%.2f' % area(4, d1 = 6, d2 = 8))
# Function that receives any number of arguments (strings expected) and returns them concatenated
def concatN(*args):
    sep = ' '
    return sep.join(args)
printMessage(concatN('"Those', 'who', 'can', 'imagine', 'anything,', 'can', 'create', 'the',
            'impossible."', '-', 'Alan', 'Turing'))
'''
},
# **************************************************************************************************
'del Statement':
{
'purpose':
'''\
Remove objects from memory like items in lists or lists itselves.
''',
'syntax':
'''\
|del <object>|

\t\t\u27F9 There is no other way to remove an item from a list given its index.
\t\t\u27F9 The pop() function returns the value that is being removed.
''',
'example':
'''\
try:
    fruits = ['mango', 'banana', 'pineapple', 'orange', 'apple', 'pear']
    del fruits[1]
    printMessage('Remove item at position 1:\\t\\t\\t\\t\\t\\t\\t' + str(fruits))
    del fruits[2:]
    printMessage('Remove items at position 2 and on:\\t\\t\\t\\t\\t' + str(fruits))
    del fruits
    printMessage('Remove the list fruits:\\t\\t\\t' + str(fruits))
except NameError as exc:
    printMessage('List does not longer exist, error displayed:\\t\\t' + str(exc))
'''
},
# **************************************************************************************************
'Appendix:  Variables and functions used':
{
'purpose':
'''\
Show the variables and functions used to run this live code tutorial.
''',
'syntax':
'''\
# Negative, zero and positive constants
MINUS_ONE = -1
ONE = 1
ZERO = 0

# Short example string
PY = 'PYTHON'

# Long example string
LONG_WORD = 'supercalifragilisticexpialidocious'

# Digit list
DIGIT_LIST = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Character list
PY_LIST = ['P', 'Y', 'T', 'H', 'O', 'N']

# Recursive Factorial function
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Recursive Sumation function
def sumation(n):
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)

# Recursive Fibonacci Number function
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Recursive Fibonacci Sequence function
def fibonacciSequence(n):
    seq = []
    for i in range(n + 1):
        seq.append(fibonacci(i))
    return seq

# Function that returns the syntax intervals in a message
def getSyntaxIntervals(lines):
    l = []
    s = None
    m = None
    for i in range(len(lines)):
        if len(lines[i]) > 0:
            if lines[i][0] == '|':
                s = i
                lines[i] = lines[i][1:]
                m = len(lines[i])
                if lines[i][len(lines[i]) - 1] == '|':
                    lines[i] = lines[i][:len(lines[i]) - 1]
                    m = len(lines[i])
                    l.append([s, i, m])
                    s = None
            elif lines[i][len(lines[i]) - 1] == '|':
                lines[i] = lines[i][:len(lines[i]) - 1]
                l.append([s, i, m])
                s = None
            elif s != None:
                if len(lines[i]) > m:
                    m = len(lines[i])
    return l

# Print Tool Function for formatting a line of text
def printMessageLine(line=None):
    if line is None:
        print()
    else:
        print('\\t' + line)

# Print Tool Function for formatting text
def printMessage(s=None):
    if s is None:
        print()
    else:
        lines = s.splitlines()
        syntaxIntervals = getSyntaxIntervals(lines)
        for i in range(len(lines)):
            if len(syntaxIntervals) > 0:
                if i == syntaxIntervals[0][0]:
                    printMessageLine((int((95 - syntaxIntervals[0][2]) / 2) - 4) * ' ' + '\\u256D' +
                                     (syntaxIntervals[0][2] + 8) * '\\u2500' + '\\u256E')
                    printMessageLine((int((95 - syntaxIntervals[0][2]) / 2) - 4) * ' ' + '\\u2502' +
                                     (syntaxIntervals[0][2] + 8) * ' ' + '\\u2502')
                    printMessageLine((int((95 - syntaxIntervals[0][2]) / 2) - 4) * ' ' + '\\u2502' +
                                     4 * ' ' + lines[i] + (syntaxIntervals[0][2] - len(lines[i])) *
                                     ' ' + 4 * ' ' + '\\u2502')
                    if syntaxIntervals[0][0] == syntaxIntervals[0][1]:
                        printMessageLine((int((95 - syntaxIntervals[0][2]) / 2) - 4) * ' ' +
                                         '\\u2502' + (syntaxIntervals[0][2] + 8) * ' ' + '\\u2502')
                        printMessageLine((int((95 - syntaxIntervals[0][2]) / 2) - 4) * ' ' +
                                         '\\u2570' + (syntaxIntervals[0][2] + 8) * '\\u2500' +
                                         '\\u256F')
                        syntaxIntervals.pop(0)
                elif i > syntaxIntervals[0][0] and i < syntaxIntervals[0][1]:
                    printMessageLine((int((95 - syntaxIntervals[0][2]) / 2) - 4) * ' ' + '\\u2502' +
                                     4 * ' ' + lines[i] + (syntaxIntervals[0][2] - len(lines[i])) *
                                     ' ' + 4 * ' ' + '\\u2502')
                elif i == syntaxIntervals[0][1]:
                    printMessageLine((int((95 - syntaxIntervals[0][2]) / 2) - 4) * ' ' + '\\u2502' +
                                     4 * ' ' + lines[i] + (syntaxIntervals[0][2] - len(lines[i])) *
                                     ' ' + 4 * ' ' + '\\u2502')
                    printMessageLine((int((95 - syntaxIntervals[0][2]) / 2) - 4) * ' ' + '\\u2502' +
                                     (syntaxIntervals[0][2] + 8) * ' ' + '\\u2502')
                    printMessageLine((int((95 - syntaxIntervals[0][2]) / 2) - 4) * ' ' + '\\u2570' +
                                     (syntaxIntervals[0][2] + 8) * '\\u2500' + '\\u256F')
                    syntaxIntervals.pop(0)
                else:
                    printMessageLine(lines[i])
            else:
                printMessageLine(lines[i])

# Function to print a higher hierarchy divider
def printDivider():
    print(105 * '\\u2550')

# Function to print a lower hierarchy divider
def printDivider2():
    print(105 * '\\u2500')

# Function to print the header of the code tutorial
def printHeader():
    printDivider()
    print('\\n' + '\\u27F0 Python 3.6' + '\\n')
    printDivider()

# Function to format a string in a cube format
def cubeMessage(s):
    if len(s) > 20:
        s = s.split()[0]
    s = s.upper()
    t = '\\u256D\\u2500\\u2500\\u2500'
    m = '\\u2502 ' + s[0] + ' '
    b = '\\u2570\\u2500\\u2500\\u2500'
    for i in range(1, len(s)):
        t += '\\u252C\\u2500\\u2500\\u2500'
        m += '\\u2502 ' + s[i] + ' '
        b += '\\u2534\\u2500\\u2500\\u2500'
    t += '\\u256E'
    m += '\\u2502'
    b += '\\u256F'
    return (t, m, b)

# Function to print all code topics
def printCodeTopics(codeInfo):
    for topic in codeInfo:
        t, m, b = cubeMessage(topic)
        print('\n' + ' ' * (len(topic) + 3) + t)
        print('\u25BD ' + topic + ' ' + m)
        print(' ' * (len(topic) + 3) + b + '\n')
        printDivider2()
        print('\\n\\t\\u2318 Purpose & Syntax\\n')
        printDivider2()
        print('\\n')
        printMessage('\\u25C9 Purpose:  ' + codeInfo[topic]['purpose'])
        print('\\n')
        printMessage('\\u25C9 Syntax:')
        print('\\n')
        printMessage(codeInfo[topic]['syntax'])
        print('\\n')
        printDivider2()
        print('\\n\\t\\u2318 Code example\\n')
        printDivider2()
        print('\\n')
        printMessage(codeInfo[topic]['example'])
        print('\\n')
        printDivider2()
        print('\\n\\t\\u2318 Result\\n')
        printDivider2()
        print('\\n')
        exec(codeInfo[topic]['example'])
        print('\\n')
        printDivider()

# Function to execute and run the whole live code tutorial
def runLiveCodeTutorial():
    printHeader()
    printCodeTopics(codeInformation)
''',
'example':
'''\
# Instance of one topic example to be used with the main function
topic_example = {
'<topic_example>':
{
'purpose':
'<Description_of_the_purpose_of_the_code_topic>',
'syntax':
'|<Synctactic_description_of_the_code_topic>|',
'example':
'printMessage("<Code_example_of_the_code_topic>")'
},
}

# Prints a list with the factorial of the digits on DIGIT_LIST
seq = []
for d in DIGIT_LIST:
    seq.append(factorial(d))
printMessage('Factorials of digits in DIGIT_LIST:\\t\\t\\t' + str(seq))
printDivider2()
# Prints a list with the sumation of the digits on DIGIT_LIST
seq = []
for d in DIGIT_LIST:
    seq.append(sumation(d))
printMessage('Sumation of digits in DIGIT_LIST:\\t\\t\\t\\t' + str(seq))
printDivider2()
# Prints a list with the Fibonacci number of the digits on DIGIT_LIST
seq = []
for d in DIGIT_LIST:
    seq.append(fibonacci(d))
printMessage('Fibonacci numbers of digits in DIGIT_LIST:\\t\\t' + str(seq))
printCodeTopics(topic_example)
'''
},
# **************************************************************************************************
'Strings':
{
'purpose':
'''\
Sequence of characters usually enclosed between quotes to be used mostly as text.
''',
'syntax':
'''\
\t\u23E3 Single quotes:\t\t\t\t'Use "single" quotes to print double quotes or
\t\t\t\t\t\t\t\tescape with \\, \', \"'
\t\u23E3 Double quotes:\t\t\t\t"Use 'double' quotes to print single quotes or
\t\t\t\t\t\t\t\tescape with \\, \', \""
\t\u23E3 Triple single quotes:\t\t\'\'\'Triple quotes (either single or double)
\t\t\t\t\t\t\t\tfor multiple lines\'\'\'
\t\u23E3 Triple double quotes:\t\t\"\"\"Triple quotes
\t\t\t\t\t\t\t\t\t\tmaintain spacing
\t\t\t\t\t\t\t\t\t\t\ton th multiple lines
\t\t\t\t\t\t\t\t\t\t\t\tlike tabs\"\"\"
\t\u23E3 Backslash (\):\t\t\t\tEscape characters use backslash (\\n), to escape them,
\t\t\t\t\t\t\t\tdouble it (\\\\)
\t\u23E3 Concatenate:\t\t\t\tStrings next to each other in a sequence are automatically
\t\t\t\t\t\t\t\tconcatenated

|<string_1> <string_2> <string_3> ... <string_N>|


\t\u23E3 String methods and common operations:
\t\t\u2724 Operator in:\t\t\tReturn TRUE if a string is within the other, FALSE otherwise

|<string_1> in <string_2>|

\t\t\u2724 Opertor not in:\t\t\tReturn TRUE if a string is not within the other, FALSE otherwise

|<string_1> not in <string_2>|

\t\t\u2724 Operator +:\t\t\t\tConcatenate two or more strings into one

|<string_1> + <string_2> + ... + <string_N>|

\t\t\u2724 Operator *:\t\t\t\tConcatenate a string n times into one

|<n> * <string>|

\t\t\u2724 Indexing:\t\t\t\tReturn the character on the position specified by the index

|<string>[<index>]|

\t\u23E3 Slicing:\t\t\t\t\tStrings can be subscripted (indexed) or sliced forwards and
\t\t\t\t\t\t\t\tbackwards

|<string_name>[ [start_included[:end_excluded[:step]]] ]|

\t\t\u2724 <string>[ [start[:end[:step]]] ]:\tSubscript (index) or slice a string whether
\t\t\t\t\t\t\t\t\t\t\tforward or backwards
\t\t\u2724 .append(<item>):\t\t\t\t\tAppend an item to the end of the list


\t\t\u256D\u2500\u2500\u2500\u252C\u2500\u2500\u2500\u252C\u2500\u2500\u2500\u252C\u2500\u2500\
\u2500\u252C\u2500\u2500\u2500\u252C\u2500\u2500\u2500\u256E
\t\t\u2502 P \u2502 y \u2502 t \u2502 h \u2502 o \u2502 n \u2502
\t\t\u251C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\
\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2524\
\tif start is not specified it means from the very beginning
\t\t0   1   2   3   4   5   6
\t   -6  -5  -4  -3  -2  -1   N\tif end is not specified it means until the very end

\t\t\u27F9 Strings are immutable, they cannot be changed (can be copied and copies modified)

\t\u23E3 Built-in function str():\tWith built-in function str(), a number and mostly any other type
\t\t\t\t\t\t\t\tof object can be converted to strings
\t\t\t\t\t\t\t\t(no object returns an empty string)

|str([object])|

\t\u23E3 Built-in function len():\tWith built-in function len(), the length of a string can be found

|len(<string_name>)|
''',
'example':
'''\
# Examples of String uses, quotes, slicing, concatenation and characteristics
printMessage('Escaping double quotes inside string:\\t\\t\\t\\t\\t\\t' + '\"Yes\", he said.')
printMessage('Double quotes inside string:\\t\\t\\t\\t\\t\\t\\t\\t' + '"No!", he said.')
printMessage('Double quotes & single quotes inside string:\\t\\t\\t\\t' +
\'\'\'\"Isn\'t it?\", she asked.\'\'\')
printMessage('Escaping escape characters:\\t\\t\\t\\t\\t\\t\\t\\t' +
'\Library\...\Versions\\\\3.6\\\\bin\python')
printMessage('Concatenating (+) & multiplying (*) strings:\\t\\t\\t\\t' + 'WHA' + 5 * 'KA')
printMessage('Concatenating consecutive strings:\\t\\t\\t\\t\\t\\t\\t' 'WHA'
'KA' 'KA' 'KA' 'KA' 'KA')
printMessage('Slicing strings (\\'%s\\') forward & backwards:\\t\\t\\t\\t' % PY +
PY[0:2] + ' ' + PY[4:6] + ' ' + PY[-6:-4] + ' ' + PY[-2:])
printMessage('Length of string \\'%s\\':\\t\\t' % LONG_WORD + 'The lenght of the string is ' +
str(len(LONG_WORD)))
'''
},
}

# Main function to run the live code tutorial
runLiveCodeTutorial()
