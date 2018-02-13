MINUS_ONE = -1
ONE = 1
ZERO = 0
c = ZERO

def printMessage(s):
    lines = s.splitlines()
    for line in lines:
        print('\t\t' + line)

def printDivider():
    print('=========================================================================================================')

def printDivider2():
    print('---------------------------------------------------------------------------------------------------------')

forLoop ='''for Statements\n
    for <variable> in <sequence>:
        <statements>
    else:
        <statements>'''
        
forLoop2 = '''for i in range(10):
    print(i+1)
'''

codeInformation = {'if Statements': {'syntax': '''if <expression>:
    <statements>
elif <expression>:
    <statements>
elif <expression>:
    <statements>
...
else:
    <statements>''',
'example': '''if MINUS_ONE > 0:
    printMessage('Possitive number')
elif MINUS_ONE == 0:
    printMessage('Zero')
else:
    printMessage('Negative number')'''},
'while Statements': {'syntax': '''while <expression>:
    <statements>
else:
    <statements>''',
'example': '''while c < 15:
    c += 1
    if c == 13:
        continue
    printMessage('Iteration #%d, c = %d' % (c, c))
else:
    printMessage('Code executed at the end of the loop by else')
    printMessage('Did you notice that 13 was avoided with the continue statement?')'''},
'for Statements': {'syntax': '''for <variable> in <sequence>:
    <statements>
else:
    <statements>''',
'example': '''for i in range(15):
    if i == 13 or i + 1 == 13:
        continue
    printMessage('Iteration #%d, i = %d' % (i + 1, i))
else:
    printMessage('Code executed at the end of loop by else')
    printMessage('Did you notice that 13 numbers were avoided with the continue statement?')'''},
}



printDivider()
print('\n' + 'Python 3.6' + '\n')
for stat in codeInformation:
    printDivider()
    print('\n' + stat + '\n')
    printDivider2()
    print('\n\tSyntax\n')
    printDivider2()
    print
    printMessage(codeInformation[stat]['syntax'])
    print
    printDivider2()
    print('\n\tCode example\n')
    printDivider2()
    print
    printMessage(codeInformation[stat]['example'])
    print
    printDivider2()
    print('\n\tResult\n')
    printDivider2()
    print
    exec(codeInformation[stat]['example'])
    print
    
    
