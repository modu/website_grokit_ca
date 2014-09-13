
# Python Command-Line Parsing, Design Principles And Introspection

Python is such a useful language for small 'helper' applications that can be run from the command-line. However, even in a program as small as a 'command line parser/forwarder' (parses the command entered by the user and then run an appropriate function), it not immediately obvious what is the _right_ way to do things.

## What **NOT** to Do

Here is an example of a small script that I wrote in a hurry. It allows running a different command from a program depending on the first argument from the command line.

    import misc.hg_utils

    import sys

    if sys.argv[1] == 'st':
      misc.hg_utils.printHgFolders_st()
    elif sys.argv[1] == 'commit':
      misc.hg_utils.printHgFolders_commit()
    elif sys.argv[1] == 'push':
      misc.hg_utils.printHgFolders_push()
    else:
      raise Exception("Unknown command")

This is a very common pattern in code, especially amongst 'old' C coders that are used to long [switch-case structures](http://en.wikipedia.org/wiki/Switch-case#C.2C_C.2B.2B.2C_Java.2C_PHP.2C_ActionScript.2C_JavaScript).

It **bad** code because:

* If someone adds a function or change a function name in the *misc.hg_utils* module, the parser script (that might not be in the same directory) will have to be changed at the same time. This is a violation of the [Don't Repeat Yourself (DRY)](http://en.wikipedia.org/wiki/Don't_repeat_yourself) principle: "Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.".

* A lot of copy/paste is involved. Every existing command requires a new 'elif' cause.

## A Little Bit Better

This is just to illustrate that in python there are (handy) alternatives to switch-case statements. In this case I use a dictionary of string-functions to contain the available commands and their triggers. Since functions in python are first-class objects, this does not create the same type of problems that a _pointer to a function_ would in C (not type safe, the function needs to be static ...).

    import misc.hg_utils

    import sys

    commands = {
      'st': misc.hg_utils.printHgFolders_st,
      'commit': misc.hg_utils.printHgFolders_commit,
      'push': misc.hg_utils.printHgFolders_push
    }

    if len(sys.argv) < 1 or sys.argv[1] not in commands.keys():
      raise Exception("Unknown command. Try using: %s" % \
        commands.keys())
    else:
      cmd_args = sys.argv[1]
      print('Running with argument: %s' % cmd_args)
      functor = commands[cmd_args]
      functor()

But this solution, however better, still violated the DRY principle.

## Better

The solution is to put the commands description in the module itself:
    
    #file: hg_utils.py
    #[...] code before
    def get_commands():
      commands = {
        'st': command_printHgFolders_st,
        'commit': command_printHgFolders_commit,
        'push': command_printHgFolders_push  
      }
      return commands
    #[...] code after

The scrip then becomes:

    import misc.hg_utils

    import sys

    commands = misc.hg_utils.get_commands()

    if len(sys.argv) <= 1:
      raise Exception("No command-line argument provided, try using: %s" % \
      commands.keys())
    if sys.argv[1] not in commands.keys():
      raise Exception("Unknown command. Try using: %s" % \
        commands.keys())
    else:
      cmd_args = sys.argv[1]
      print('Running command: %s' % cmd_args)
      functor = commands[cmd_args]
      functor()

The 'parser/runner' script is now completely __independent__ from the module's code; it will never need to change in order to accomodate for new functions. This code is DRY-OK.

## Much Better (Current Solution, Thanks to 'A' For Pointing Out Improvements)

User '**A**' suggested using the [argparse module](http://docs.python.org/dev/library/argparse.html) in order to process the command-line arguments. This, however, requires a recent python distribution (had to upgrade mine): 3.2+ or 2.7.2+.

    import misc.hg_utils

    import sys
    import argparse

    commands = misc.hg_utils.get_commands()

    parser = argparse.ArgumentParser(description='Mercurial (hg) utils.')
    parser.add_argument('command', choices=commands.keys(), help='mercurial command')
    args = parser.parse_args()

    cmd_args = args.command
    print('Running command: %s' % cmd_args)
    functor = commands[cmd_args]
    functor()

This way is much simpler, and delegates the error handling and printing usage o a well designed module. When typing _python hgstero.py -h_ you now get:

    usage: hgstero.py [-h] {push,commit,st}

    Mercurial (hg) utils.

    positional arguments:
      {push,commit,st}  mercurial command

    optional arguments:
      -h, --help        show this help message and exit

## Introspection: Fancy Solution (Not Necessarily Better Because it Relies on 'Magic')

This one is a bit funkier and uses advances features of the python language. Let's say that we have a convention that all the commands in the module are globally visible functions and have a 'command_' prefix in the function's name.

Then one can use _introspection_ to gather all the commands and return them to the user.

    import misc.hg_utils

    import inspect

    def get_commands():
      module_members = inspect.getmembers(misc.hg_utils)

      commands = []
      for module_member in module_members:
        name = module_member[0]
        content = module_member[1]
        if inspect.isfunction( content ):
          if len(name) > 8 and name[0:8] == 'command_':
            commands.append(module_member)
      return commands
      
    for command in get_commands():      
      print(command)

The crux of the modification is the use of the _inspect_ module by calling: **inspect.getmembers(misc.hg_utils)**. This allows to check the content of the module, and then to gather all the functions using **inspect.isfunction( content )**.
      
This is what is returned to the user:

    ('command_printHgFolders', <function command_printHgFolders at 0x0000000001FB96C8>)
    ('command_printHgFolders_commit', <function command_printHgFolders_commit at 0x0000000001FB97C8>)
    ('command_printHgFolders_push', <function command_printHgFolders_push at 0x0000000001FB9848>)
    ('command_printHgFolders_st', <function command_printHgFolders_st at 0x0000000001FB9748>)

The problem with something like that is that it relies on convention. If one coder is not aware of it, he might name a function *command_getRootPasswordAndBankAccountNumber()* that should not be accessible to the command-line version (did you notice that there is one more function listed than with the previous example?).

I prefer to not use solutions like this because they involve 'magic': nice usage of the language that are beautiful to the original coder but not to future coders that might not be aware of all the 'tricks' that the senior coder had in its basket when coding the application -- easily leading to disaster.

Still, it is nice to know how it _could_ be done.
