# Enconding definition for special characters
# -*- coding: utf-8 -*-

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

# Print Tool Function for formatting text
def printMessage(s=None):
    if s is None:
        print()
    else:
        lines = s.splitlines()
        for line in lines:
            print('\t' + line)

# Function to print a higher hierarchy divider
def printDivider():
    print('=========================================================================================================')

# Function to print a lower hierarchy divider
def printDivider2():
    print('---------------------------------------------------------------------------------------------------------')

# Function to execute and run the whole live code tutorial
def runLiveCodeTutorial(codeInfo):
    printDivider()
    print('\n' + 'Python 3.6' + '\n')
    printDivider()
    for topic in codeInfo:
        print('\n' + topic + '\n')
        printDivider2()
        print('\n\tPurpose & Syntax\n')
        printDivider2()
        print('\n')
        printMessage('Purpose:  ' + codeInfo[topic]['purpose'])
        print('\n')
        printMessage('Syntax:')
        print('\n')
        printMessage(codeInfo[topic]['syntax'])
        print('\n')
        printDivider2()
        print('\n\tCode example\n')
        printDivider2()
        print('\n')
        printMessage(codeInfo[topic]['example'])
        print('\n')
        printDivider2()
        print('\n\tResult\n')
        printDivider2()
        print('\n')
        exec(codeInfo[topic]['example'])
        print('\n')
        printDivider()

# Dictionary with all topic information about the live code tutorial
codeInformation = {
'range() function':
{
'purpose':
'''\
Generates arithmetic progressions as sequences of numbers to be used on iterations.
''',
'syntax':
'''\
* Generates a sequence 0...n-1:                      range(n)
* Generates a sequence n...m-1:                      range(n, m)
* Generates a sequence n...m-1 with k steps:         range(n, m, k)
''',
'example':
'''\
printMessage('Zero to n-1 sequence:\\t\\t\\t\\t' + str(list(range(10))))
printMessage('n to m-1 sequence:\\t\\t\\t\\t\\t' + str(list(range(5, 10))))
printMessage('n to m-1 sequence with k step:\\t\\t' + str(list(range(-10, -100, -20))))
'''
},
'Strings':
{
'purpose':
'''\
Sequence of characters usually enclosed between quotes to be used mostly as text.
''',
'syntax':
'''\
* Single quotes:            'Use "single" quotes to print double quotes or escape with \\, \', \"'
* Double quotes:            "Use 'double' quotes to print single quotes or escape with \\, \', \""
* Triple single quotes:     \'\'\'Triple quotes (either single or double)
                           for multiple lines\'\'\'
* Triple double quotes:     \"\"\"Triple quotes
                                  maintain spacing
                                      on th multiple lines
                                          like tabs\"\"\"
* Backslash (\):            Escape characters use backslash (\\n), to escape them, double it (\\\\)
* Concat & repeat:          Strings can be concatenated with + and repeated n times with *
* Concatenate:              Strings next to each other in a sequence are automatically concatenated
* Slicing:                  Strings can be subscripted (indexed) or sliced forwards and backwards

        +---+---+---+---+---+---+   <stringname>[[start included]:[end excluded]]
        | P | y | t | h | o | n |
        +---+---+---+---+---+---+   if start is not specified it means from the very beginning
        0   1   2   3   4   5   6
       -6  -5  -4  -3  -2  -1   N   if end is not specified it means until the very end

        + Strings are unmutable, they cannot be changed (can be copied and copies modified)

* Built-in function str():  With built-in function str(), a number can be converted to string
* Built-in function len():  With built-in function len(), the length of a string can be found
''',
'example':
'''\
# Examples of String uses, quotes, slicing, concatenation and characteristics
printMessage('Escaping double quotes inside string:\\t\\t\\t\\t\\t\\t' + '\"Yes\", he said.')
printMessage('Double quotes inside string:\\t\\t\\t\\t\\t\\t\\t\\t' + '"No!", he said.')
printMessage('Double quotes & single quotes inside string:\\t\\t\\t\\t' + \'\'\'\"Isn\'t it?\", she asked.\'\'\')
printMessage('Escaping escape characters:\\t\\t\\t\\t\\t\\t\\t\\t\\t' +
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
'Lists':
{
'purpose':
'''\
Compound data type used to group a comma-separated sequence of values between square brackets.
''',
'syntax':
'''\
* Creation with elements:     <list_name> = [[element1,] [element2,] ...]
* Concatenate:                Lists can be concatenated with +
* Slicing:                    Lists can be subscripted (indexed) or sliced like strings
* Built-in function len()     With the built-in function len(), the length of a list can be found
Nesting:                    Lists can be nested in whatever dimensions desired
* Contents:                   Lists can contain any type of elements even mixed ones
* Built-in function str():    With built-in function str() other objects can be converted to lists

        + Lists unlike strings, are mutable, anything can be changed on them
''',
'example':
'''\
# Examples of List uses, slicing, concatenation and characteristics
odd_digits = [1, 3, 5, 7, 9]
printMessage('Simple list defined with elements:\\t\\t\\todd_digits = ' + str(odd_digits))
printMessage('Concatenated lists:\\t\\t\\t\\t\\t\\t\\t' + str(PY_LIST + odd_digits))
printMessage('Slicing lists forward & backwards:\\t\\t\\tPair:  ' + str(DIGIT_LIST[0:9:2]) +
            ' Odd:  ' + str(DIGIT_LIST[-9::2]))
printMessage('Length of list %s:\\t\\t\\t\\t' % odd_digits + str(len(odd_digits)))
printMessage('Nested lists of slices of DIGIT_LIST:\\t\\t' + str([DIGIT_LIST[0:2], DIGIT_LIST[2:4],
            DIGIT_LIST[4:6],DIGIT_LIST[6:8],DIGIT_LIST[8:]]))
printMessage('List with different types of elements:\\t\\t' + str(['Python', 3.14, DIGIT_LIST[0:9:2],
            7, 'X']))
printMessage('Converting a range to a list:\\t\\t\\t\\t' + str(list(range(10))))
'''
},
'if Statement':
{
'purpose':
'''\
Branch statement to control the flow of code based on boolean conditions.
''',
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
'while Statement':
{
'purpose':
'''\
Loop statement which executes and iterates as long as a condition remains true.
''',
'syntax':
'''\
while <expression>:
    <statements>
else:
    <statements>
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
'for Statement':
{
'purpose':
'''\
Loop statement which executes and iterates over the items of a sequence on its order.
''',
'syntax':
'''\
for <variable> in <sequence>:
    <statements>
else:
    <statements>
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
'pass Statement':
{
'purpose':
'''\
Synctactic filler statement that does nothing for other statements and structures
          when no action is required.
''',
'syntax':
'''\
pass
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
'Function Definition':
{
'purpose':
'''\
Define subroutines and blocks of code to be invoked on demand and repeatedly.
''',
'syntax':
'''\
def <function name>([keyword_arg1[ = default_value1][, keyword_arg2[ = default_value2]] ...]):
    <statements>

        + If a default value is specified for an argument, that argument becomes optional.
    
        + Arguments with no default value are required.
        
        + An argument can be specified positionally or with a keyword.
    
        + Arguments can be specified positionally but only before any keyword argument is used.
        
        + A function can be invoked with an arbitrary number of arguments in a list (*args).

def <function name>(*args):
    <statements>
''',
'example':
'''\
# Function to print only even values of Fibonacci sequence of digits
def fibonacciEvenNumbers(n):
    seq = {}
    for i in DIGIT_LIST:
        if fibonacci(i) % 2 == 0:
            seq['Digit %d' % i] = fibonacci(i)
    return seq
printMessage('Fibonacci even of digits:\\t' + str(fibonacciEvenNumbers(9)))

# Function that receives any number of arguments (strings expected) and returns them concatenated
def x(*args):
    sep = ' '
    return sep.join(args)
printMessage(x('"Those', 'who', 'can', 'imagine', 'anything,', 'can', 'create', 'the',
            'impossible."', '-', 'Alan', 'Turing'))
'''
},
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

# Print Tool Function for formatting text
def printMessage(s=None):
    if s is None:
        print()
    else:
        lines = s.splitlines()
        for line in lines:
            print('\\t\\t' + line)

# Function to print a higher hierarchy divider
def printDivider():
    print('==============================================================================
    ===========================')

# Function to print a lower hierarchy divider
def printDivider2():
    print('------------------------------------------------------------------------------
    ---------------------------')

# Function to execute and run the whole live code tutorial
def runLiveCodeTutorial(codeInfo):
    printDivider()
    print('\\n' + 'Python 3.6' + '\\n')
    printDivider()
    for topic in codeInfo:
        print('\\n' + topic + '\\n')
        printDivider2()
        print('\\n\tPurpose & Syntax\\n')
        printDivider2()
        print('\\n')
        printMessage('Purpose:  ' + codeInfo[topic]['purpose'])
        print('\\n')
        printMessage('Syntax:')
        print('\\n')
        printMessage(codeInfo[topic]['syntax'])
        print('\\n')
        printDivider2()
        print('\\n\tCode example\\n')
        printDivider2()
        print('\\n')
        printMessage(codeInfo[topic]['example'])
        print('\\n')
        printDivider2()
        print('\\n\tResult\\n')
        printDivider2()
        print('\\n')
        exec(codeInfo[topic]['example'])
        print('\\n')
        printDivider()
''',
'example':
'''\
# Prints a list with the factorial of the digits on DIGIT_LIST
seq = []
for d in DIGIT_LIST:
    seq.append(factorial(d))
printMessage('Factorials of digits in DIGIT_LIST:\\t\\t\\t\\t' + str(seq))
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
'''
},
}

# Main function to run the live code tutorial
runLiveCodeTutorial(codeInformation)


