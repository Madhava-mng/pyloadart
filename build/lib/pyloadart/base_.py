#

from random import choice

R, G, Y, B, P, C, W, N, BR , I = (
    "\u001b[31m",
    "\u001b[32m",
    "\u001b[33m",
    "\u001b[34m",
    "\u001b[35m",
    "\u001b[36m",
    "\u001b[37m",
    "\u001b[0m",
    "\u001b[1m",
    "\u001b[7m",
    )

D = choice((R,B,G,Y,P))


TMP_INT = 0
ExceptionKeyboardInterrupt = False

def custom(current_value, expected_value, msg = '', theam = '?', unfilled = '.', number = True, color="W", end_with="[]" ,interval=1):
    """
    >>> pyloadart.custom(1, 10000, msg = 'text', theam = '#')

    >>> help(pyloadart)
    """
    try:
        global TMP_INT

        round_ = round((current_value/expected_value) * 100)

        unfilled = "\u001b[2m"+ unfilled[0] +"\u001b[0m"

        if(round_ == TMP_INT):
            return

        TMP_INT = round_

        if((round_%interval == 0 or round_ == 100) and (current_value <= expected_value)):

            if(number):
                print("\r{} {C}{B}  {:3}%{N} {C}{B}{}{N}{}{C}{B}{}{N}".format(msg, round_, end_with[0], (theam[0] * (round_//2)).ljust(50).replace(" ",unfilled), end_with[1], C = eval(color.upper()), B = BR, N = N, I = I), end='')
            else:
                print("\r{} {C}{B}{}{N}{}{C}{B}{}{N}".format(msg, end_with[0], (theam[0] * (round_//2)).ljust(50).replace(" ",unfilled), end_with[1], C = eval(color.upper()), B = BR, N = N), end='')
    except ExceptionKeyboardInterrupt and KeyboardInterrupt:
        print(f"{R}Error:{N} KeyboardInterrupt".ljust(len(pre_msg)+len(post_msg)))
        raise SystemExit()




def doted(current_value, expected_value, msg = '', unfilled = '-', number = True, color = 'W',end_with="[]", interval = 1):
    """
    >>> pyloadart.doted(current_value= 1, expected_value= 1000, msg='text')

    >>> help(pyloadart)
    """
    custom(current_value, expected_value, msg, chr(11044), unfilled, number, color,end_with, interval)



def bar(current_value, expected_value, msg = '',unfilled = '.', number = True, color = 'W', end_with="||", interval = 1):
    """
    >>> pyloadart.bar(current_value= 1, expected_value= 1000, msg='text')

    >>> help(pyloadart)
    """
    custom(current_value,expected_value, msg, chr(9608), unfilled, number, color,end_with, interval)



def box(current_value, expected_value, msg = '',unfilled = '.', number = True, color = 'W', end_with="[]", interval = 1):
    """
    >>> pyloadart.box(current_value= 1, expected_value= 1000, msg='text')

    >>> help(pyloadart)
    """
    custom(current_value,expected_value, msg, chr(8369), unfilled, number, color,end_with, interval)



def hash_(current_value, expected_value,msg = '', unfilled = '-', number = True, color = 'W',end_with="[]",interval = 1):
    """
    >>> pyloadart.hash_(current_value= 1, expected_value= 1000, msg='text')

    >>> help(pyloadart)
    """
    custom(current_value, expected_value, msg, "#", unfilled, number, color, end_with, interval)



def arrow(current_value, expected_value, msg = '',unfilled = '-', number = True, color = 'W',end_with="[]",interval = 1):
    """
    >>> pyloadart.arrow(current_value= 1, expected_value= 1000, msg='text')

    >>> help(pyloadart)
    """
    custom(current_value, expected_value, msg, chr(10146), unfilled, number, color,end_with, interval)

