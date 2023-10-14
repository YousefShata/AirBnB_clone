#!/usr/bin/python3
"""
Command interpreter to control models
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNB class
    """
    prompt = '(hbnb) '
    
    def do_quit(self, line):
        """
        Quit the cmd
        """
        return True

    def do_EOF(self, line):
        """
        End of File
        """
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
