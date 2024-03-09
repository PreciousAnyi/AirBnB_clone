#!/usr/bin/python3
"""console module"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for HBNB project.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program using EOF
        """
        print()
        return True

    def emptyline(self):
        """
        Override default behavior when the user enters an empty line.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
