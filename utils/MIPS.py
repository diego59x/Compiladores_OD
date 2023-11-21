def insertStrings(strings, ints, code):
    code = f'   .globl class_main_Main\n'+code
    code = f'.text\n'+code
    for i in range(len(strings)):
        code = f'   string{i}: .asciiz {strings[i]}\n'+code
    code = insertInts(ints, code)
    code = f'.data\n'+code
    return code

def insertInts(ints, code):
    for i in range(len(ints)):
        code = f'   {ints[i][0]}: .word {ints[i][1]}\n'+code
    return code

def inheritClasses(inherited, code):
    for inheritedClass in inherited:
        f = open(f'libs/{inheritedClass}.txt', "r")
        code += f'{f.read()}\n'
    
    return code
