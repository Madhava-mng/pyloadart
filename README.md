# pyloadart
It displays loding like structure in loopy statement (package)

```bash

   pyloadart
        |
        |-- function
        |      |
        |      |-- bar()
        |      |-- arrow()
        |      |-- doted()
        |      |-- hash_()
        |      |-- custom()
        |      |-- loop
        |            |
        |            |-- box()
        |            |-- arrow()
        |            |-- clock()
        |            |-- doted()
        |            |-- custom()
        |            |-- inwords()
        |            |-- outwords()
        |
        |-- asign
        |      |
        |      |-- ExceptionKeyboardInterrupt
        |      |-- loop
        |            |-- ExceptionKeyboardInterrupt
        |
        |-- version
        |      |__ v0.0.1
        |
        |-- author
        |      |_ Madhava-mng
        |
        |__  The End. Nandrigal...!
```

```python

  >>> import pyloadart as pla
  >>> for i in range(500000):
  ...     pla.arrow(i, 500000, msg='banner\\t')
  banner  100% [➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢]
```

    Function:
        ➢ bar
        ➢ arrow
        ➢ doted
        ➢ hash_
        ➢ custom

    Assign:
        ➢ ExceptionKeyboardInterrupt = False/True


    Arg:
        ➢ current_value   =>  (int)  number
        ➢ expected_value  =>  (int)  number
        ➢ theam           =>  (str)  Inside loders "#" or "➢" ...
                                     only in custom
        ➢ msg             =>  (str)  print the message before loaders
        ➢ unfilled        =>  (str)  Fill this char with unfilled areas
        ➢ number          =>  (Bool) for hide persentage sign and number
        ➢ color           =>  (str)  W   => white
                                   R   => red
                                   B   => blue
                                   G   => green
                                   Y   => yellow
                                   P   => pink like     code: \\033[35m
                                   D   => disco
                                the colors displayed according your terminal
                                color scheam
        ➢ end_with        =>  (str)  end with chars default "[]"
                                   [0] => starts with
                                   [1] => ends with
        ➢ interval        =>  (int)  set intervel to print the loader
                                   To wavering the speed of the program



    Examples:

```python
  >>> import pyloadart as pla
  >>>
  >>> for i in range(500000):
  ...     pla.arrow(i, 500000, msg='banner \\t')
  banner   100% [➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢]

  >>> for i in range(500000):
  ...     pla.arrow(i, 500000, msg='banner2\\t', unfilled='-')
  banner2   85% [➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢----------]

  >>> for i in range(500000):
  ...     pla.arrow(i, 500000, msg='banner3\\t\\t', number=False)
  banner3       [➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢]

  >>> for i in range(500000):
  ...     pla.arrow(i, 500000, msg='banner\\t', endwith="()", unfilled='-')
  banner4   67% (➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢➢-------------------------)


  >>> for i in range(500000):
  ...     pla.custom(i, 500000, msg='banner5\\t', endwith="()", theam="@")
  banner5   68% (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@--------------------------)

  Exception
  >>> pla.ExceptionKeyboardInterrupt = True
```

   ➢ bar, dotted, hash_  all are similear to arrow.
   ➢ Some ascii values are not suported by some terminals, use custom function
     for that kind of issues.

   loop:

     Functions:
        ➢ box
        ➢ arrow
        ➢ doted
        ➢ clock
        ➢ inwords
        ➢ outwords
        ➢ custom

    Assign:
        ➢ ExceptionKeyboardInterrupt = False/True

    Arg:
        ➢ interval        =>  (int)  set intervel to print the loader
                                   To wavering the speed of the program

        ➢ pre_msg         =>  (str) display the message before loader
        ➢ post_msg        =>  (str) display the message after loader
        ➢ color           =>  (str)  W   => white
                                   R   => red
                                   B   => blue
                                   G   => green
                                   Y   => yellow
                                   P   => pink like     code: \\033[35m
                                   D   => disco
                                the colors displayed according your terminal
                                color scheam
        ➢ theam           => (list) list of char you want to disply
                                    theam = ("\\", "|", "-", "|", "/", "-")
                                    only in custom

    Examples:

```python
     >>> import pyloadart as pla
     >>> while (True):
     ...     pla.loop.box(10, pre_msg = "something loading")
     something loading  ⠽
     >>> while (True):
     ...     pla.loop.box(10, post_msg = "something loading")
     ⠽ something loading

     Exception
     >>> pla.loop.ExceptionKeyboardInterrupt = True
```
