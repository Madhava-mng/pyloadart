
CONST_INT = 0
THEAM_INDEX = 0
ExceptionKeyboardInterrupt = False

def custom(interval = 4, pre_msg='', post_msg='', theam=("\\", "|", "-", "|", "/", "-"), color='N'):
    from pyloadart.base_ import R,B,G,Y,W,P,I,C,BR,N,D
    try:
        global CONST_INT
        global THEAM_INDEX

        if(THEAM_INDEX == len(theam)):
            THEAM_INDEX = 0

        if(CONST_INT%interval== 0):

            print("\r{} {C}{}{N} {}".format(
                pre_msg, theam[THEAM_INDEX], post_msg,C=eval(color.upper()), N=N
                ), end='')
            THEAM_INDEX += 1

        CONST_INT += 1
    except  ExceptionKeyboardInterrupt and KeyboardInterrupt:
        print(f"{R}Error:{N} KeyboardInterrupt".ljust(len(pre_msg)+len(post_msg)))
        raise SystemExit()




def box(interval = 5, pre_msg='' , post_msg='', color='N'):
    theam = ("⠏", "⠟", "⠽","⠷", "⠧")
    custom(interval, pre_msg, post_msg, theam, color)

def arrow(interval = 5, pre_msg='' , post_msg='', color='N'):
    theam = [(chr(10146)*x).ljust(5) for x in range(1,6)]
    custom(interval, pre_msg, post_msg, theam, color)

def clock(interval = 5, pre_msg='' , post_msg='', color='N'):
    theam = ["↻", "⟳","↻", "⥁"]
    custom(interval, pre_msg, post_msg, theam, color)

def doted(interval = 5, pre_msg='' , post_msg='', color='N'):
    theam = ["•", "⦿", "⦾", "○"]
    custom(interval, pre_msg, post_msg, theam, color)

def outwords(interval = 5, pre_msg='' , post_msg='', color='N'):
    theam = [
        "        ",
        "        ",
        "   ⪡⪢   ",
        "  ⪡  ⪢  ",
        " ⪡    ⪢ ",
        "⪡      ⪢"
        ]
    custom(interval, pre_msg, post_msg, theam, color)

def inwords(interval = 5, pre_msg='' , post_msg='', color='N'):
    theam = [
        "⪢      ⪡",
        " ⪢    ⪡ ",
        "  ⪢  ⪡  ",
        "   ⪢⪡   ",
        "        ",
        "        "
        ]
    custom(interval, pre_msg, post_msg, theam, color)

