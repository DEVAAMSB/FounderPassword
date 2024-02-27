import random

def password_maker(upper:bool=True, lower:bool=True, num:bool=True, syms:bool=True, length:int=20):
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase_letters = uppercase_letters.lower()
    numbers = '0123456789'
    symbols = '~!@#$%^&*()_+=-:;.,/\\\'" '

    refrence = ''

    if upper:
        refrence += uppercase_letters

    if lower:
        refrence += lowercase_letters

    if num:
        refrence += numbers
    
    if syms:
        refrence += symbols

    if refrence != '':
        password =  ''.join(random.sample(refrence, length))

    else:
        password = 'At least one of the options must be checked'


    print(len(refrence))
    return password


password_maker()